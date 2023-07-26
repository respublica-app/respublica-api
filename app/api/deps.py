from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import SecurityScopes

from pydantic import BaseModel, ValidationError

from jose import JWTError, ExpiredSignatureError, jwt

from app.core.config import settings
from app.core.oauth2 import OAuth2

# We're using OAuth2 for authentication with implicit flow
oauth2_scheme = OAuth2()


class TokenData(BaseModel):
    user_id: str | None = None
    scopes: list[str] = []


def get_user(
        security_scopes: SecurityScopes,
        token: Annotated[str, Depends(oauth2_scheme)]
) -> dict:
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )

    if token.startswith("Bearer "):
        token = token[7:]
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token type"
        )
    try:
        algorithms = oauth2_scheme.oidc_config["id_token_signing_alg_values_supported"]
        payload = jwt.decode(
            token,
            oauth2_scheme.jwks,
            algorithms=algorithms,
            audience=str(settings.OAUTH2_AUDIENCE),
            issuer=oauth2_scheme.oidc_config["issuer"]
        )
        token_scopes = payload.get("scope", "").split(" ")
        print(token_scopes)
        token_data = TokenData(scopes=token_scopes, user_id=payload.get("sub"))

    except (JWTError, ValidationError):
        raise credentials_exception

    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions" + " (missing " + scope + ")",
                headers={"WWW-Authenticate": authenticate_value},
            )

    return token_data