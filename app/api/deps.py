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
