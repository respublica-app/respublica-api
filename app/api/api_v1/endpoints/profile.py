from fastapi import APIRouter, Security, HTTPException, status
from typing import Annotated

from app.api import deps

router = APIRouter()


@router.get("/")
async def profile_get(userdata: Annotated[deps.TokenData, Security(deps.get_user, scopes=["read:self"])]):
    user_id = userdata.user_id

    try:
        user_data = deps.management_access.get_user(user_id)
    except Exception as exc:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not fetch user data"
        )

    return user_data.model_dump()

