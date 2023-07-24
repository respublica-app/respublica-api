from fastapi import APIRouter, Depends

from app.api import deps

router = APIRouter()


@router.get("/")
async def root(user: dict = Depends(deps.get_user)):
    return {"message": user}
