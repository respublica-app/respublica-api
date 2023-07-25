from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2
from jose import JWTError, ExpiredSignatureError, jwt

# We're using OAuth2 for authentication with implicit flow
oauth2_scheme = OAuth2(
    flows={
        "implicit": {
            "authorizationUrl": "https://auth.respublica.aeris-one.fr/oidc/auth",
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
)


def get_user(token: str = Depends(oauth2_scheme)) -> dict:
    return token


def has_permission(user: dict, permission: str) -> bool:
    return permission in user.get("scopes", [])
