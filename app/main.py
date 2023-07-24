from fastapi import FastAPI, Response

from app.api.api_v1.api import api_router

app = FastAPI(
    title="res:publica API",
    description="API d'accès aux services de res:publica",
    version="0.1.0-alpha",

)
app.title = "res:publica API"
app.description = "API d'accès aux services de res:publica"
app.contact = {
    "name": "Charles P. (Hébergeur)",
    "email": "aeris@aeris-one.fr"
}
app.version = "0.1.0-alpha"

# Redirection vers la documentation
@app.get("/", include_in_schema=False)
async def root():
    return Response(status_code=302, headers={"Location": "/docs"})

@app.get("/health", include_in_schema=False)
async def health():
    return {"status": "ok"}

app.include_router(api_router, prefix="/v1")