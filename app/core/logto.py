from jose import jwt
import requests
import base64

from pydantic import BaseModel, ValidationError, AnyHttpUrl

from app.core.config import settings


class User(BaseModel):
    id: str
    email: str | None = None
    username: str | None = None
    phone: str | None = None
    name: str | None = None
    avatar: AnyHttpUrl | None = None


class LogtoManagement():
    def __init__(self):
        self.client_id = settings.LOGTO_MANAGEMENT_M2M_CLIENT_ID
        self.client_secret = settings.LOGTO_MANAGEMENT_M2M_SECRET

        try:
            self.oidc_config = requests.get(settings.OAUTH2_WELL_KNOWN_URL, timeout=10).json()
            self.jwks = requests.get(self.oidc_config["jwks_uri"], timeout=10).json()
            self.token_url = self.oidc_config["token_endpoint"]
        except requests.exceptions.RequestException as exc:
            raise Exception("Could not fetch OIDC configuration") from exc

        self.token = self.refresh_token()

    def refresh_token(self):
        basic_auth = f"{self.client_id}:{self.client_secret}"
        basic_auth = basic_auth.encode("utf-8")
        basic_auth = base64.b64encode(basic_auth)

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {basic_auth.decode('utf-8')}"
        }

        data = {
            "grant_type": "client_credentials",
            "resource": "https://default.logto.app/api",
            "scope": "all"
        }

        try:
            response = requests.post(self.token_url, headers=headers, data=data, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as exc:
            raise Exception("Could not fetch Management API access token") from exc

        # ensure token is valid
        if not self.check_token(response.json()["access_token"]):
            raise Exception("Invalid Management API access token received")

        return response.json()["access_token"]

    def check_token(self, token=None):
        if token is None:
            token = self.token

        try:
            jwt.decode(
                token,
                self.jwks,
                algorithms=self.oidc_config["id_token_signing_alg_values_supported"],
                audience="https://default.logto.app/api",
                issuer=self.oidc_config["issuer"]
            )
        except jwt.JWTError:
            return False
        return True

    def get_token(self):
        if not self.check_token():
            self.token = self.refresh_token()
        return self.token

    def get_user(self, user_id):
        token = self.get_token()

        headers = {
            "Authorization": f"Bearer {token}"
        }

        url = f"{settings.LOGTO_MANAGEMENT_URL}/users/{user_id}"

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as exc:
            print(exc)
            print(self.token)
            raise Exception("Could not fetch user data") from exc

        return User(
            id=response.json()["id"],
            email=response.json()["primaryEmail"],
            username=response.json()["username"],
            phone=response.json()["primaryPhone"],
            name=response.json()["name"],
            avatar=response.json()["avatar"]
        )
