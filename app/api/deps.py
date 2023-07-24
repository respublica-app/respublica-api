from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2
from jose import JWTError, ExpiredSignatureError, jwt

# We're using OAuth2 for authentication with authorization code flow
oauth2_scheme = OAuth2(
    flows={
        "implicit": {
            "authorizationUrl": "https://auth.respublica.aeris-one.fr/oidc/auth",
            "scopes": {
                "openid": "OpenID Connect",
                "profile": "Informations de profil",
                "email": "Adresse e-mail",
                "read:flow": "Accès aux flux",


            }
        }
    }
)

jwk_set = {"keys":[{"kty":"EC","use":"sig","kid":"6s-Vul-i4ScuHx-AJP-ha_rdhjU2ocWGgYX2NZNtclQ","alg":"ES384","crv":"P-384","x":"3p6qU3gbMyxoB6Bmk4936eh3tDLkCSnJT8SnaH-ZHaoSHLrTaTXYZd-3K8MKr7jZ","y":"YLZcBLVkvXp-GUjfjViftp_hEVK3BQElpTQhkGfeCdICeyk0EORtfVuVJJeoeL5i"}]}

def get_user(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = jwt.decode(token, jwk_set, algorithms=["HS256"])
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")

    return payload


def has_permission(user: dict, permission: str) -> bool:
    return permission in user.get("scopes", [])
