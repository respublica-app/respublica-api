import fastapi.security.oauth2
import requests

from app.core.config import settings


class OAuth2(fastapi.security.oauth2.OAuth2):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        try:
            self.oidc_config = requests.get(settings.OAUTH2_WELL_KNOWN_URL, timeout=10).json()
            self.jwks = requests.get(self.oidc_config["jwks_uri"], timeout=10).json()
        except requests.exceptions.RequestException as exc:
            raise Exception("Could not fetch OIDC configuration") from exc

        self.flows = {
            "implicit": {
                "authorizationUrl": self.oidc_config["authorization_endpoint"],
                "scopes": {
                    "openid": "OpenID Connect",
                    "profile": "Informations de profil",
                    "email": "Adresse e-mail",
                    "read:flow": "Accès aux flux (lecture seule)",
                    "read:law": "Accès aux API des dossiers législatifs (lecture seule)",
                    "read:parliament": "Accès aux API des données des assemblées (lecture seule)",
                    "read:survey": "Accès aux API des enquêtes (lecture seule)",
                    "write:survey": "Permet de répondre aux enquêtes",
                    "read:argument": "Accès aux API des débats (lecture seule)",
                    "write:argument": "Permet de participer aux débats",
                    "read:self": "Accès en lecture à son propre profil",
                    "write:self": "Accès en écriture à son propre profil",
                    "read:admin": "Accès en lecture aux API administration",
                    "write:admin": "Accès en écriture aux API administration"
                }
            }
        }
