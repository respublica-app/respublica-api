from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title="res:publica API",
    description="API d'accès aux services de res:publica",
    version="0.1.0-alpha",
    contact={
        "name": settings.CONTACT_NAME,
        "email": settings.CONTACT_EMAIL
    }
)

# If development, add the production server to docs
if settings.ENVIRONMENT == "development":
    app.servers = [
        {
            "url": settings.SERVER_HOST,
            "description": "Serveur de développement"
        },
        {
            "url": "https://api.respublica.aeris-one.fr",
            "description": "Serveur de production"
        }
    ]


# CORS
origins = [origin.scheme +"://"+ origin.host + ":" + str(origin.port) for origin in settings.BACKEND_CORS_ORIGINS]
print(origins)
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

# Redirection vers la documentation
@app.get("/", include_in_schema=False)
async def root():
    return Response(status_code=302, headers={"Location": "/docs"})

@app.get("/health", include_in_schema=False)
async def health():
    return {"status": "ok"}

app.include_router(api_router, prefix="/v1")