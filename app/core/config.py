from typing import Any, Dict, List, Optional

from pydantic import AnyHttpUrl, PostgresDsn, EmailStr, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    # Server
    SERVER_NAME: str = "respublica-api"
    SERVER_HOST: AnyHttpUrl = "http://localhost:8000"

    # Environment
    ENVIRONMENT: str = "development"
    @field_validator("ENVIRONMENT")
    def validate_environment(cls, v: str) -> str:
        if v not in ["development", "production"]:
            raise ValueError("ENVIRONMENT must be 'development' or 'production'")
        return v


    # CORS
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:8000", "http://127.0.0.1:8000"]

    # Database
    # Optional for now, but will be required in the future
    POSTGRES_DSN: Optional[PostgresDsn] = None

    # OAuth2
    OAUTH2_WELL_KNOWN_URL: AnyHttpUrl
    OAUTH2_M2M_CLIENT_ID: str
    OAUTH2_M2M_CLIENT_SECRET: str
    OAUTH2_AUDIENCE: str = "https://api.respublica.aeris-one.fr"

    # Contact
    CONTACT_EMAIL: Optional[EmailStr] = None
    CONTACT_NAME: Optional[str] = None

settings = Settings()
