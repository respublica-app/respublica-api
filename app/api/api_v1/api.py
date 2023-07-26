from fastapi import APIRouter

from app.api.api_v1.endpoints import template, profile

api_router = APIRouter()
api_router.include_router(template.router, prefix="/template", tags=["temp"])
api_router.include_router(profile.router, prefix="/profile", tags=["profile"])