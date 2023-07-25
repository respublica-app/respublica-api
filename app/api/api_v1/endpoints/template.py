from fastapi import APIRouter, Depends, Security
from typing import Annotated

from app.api import deps

router = APIRouter()


@router.get("/")
async def root(userdata: Annotated[deps.TokenData, Security(deps.get_user, scopes=["read:self"])]):
    return {"message": userdata.model_dump()}
