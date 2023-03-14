from fastapi import (
    APIRouter,
    BackgroundTasks,
    Body,
    HTTPException,
    Request,
    status,
    UploadFile,
    Depends,
)
from fastapi.responses import JSONResponse, HTMLResponse
from back.utils import common_parameters
from back.config.model import UserIn, UserOut

router = APIRouter()


@router.post("/users/", response_model=UserOut, summary="Signup user")
async def add_user(
    user: UserIn = Body(
        example={
            "username": "string",
            "group": "string",
            "password": "string",
        }
    )
):
    """
    Create an User with all the information:
    - **username**: username
    - **group**: user group
    - **password**: user password
    """
    return user


@router.get("/users/")
async def read_items(commons: dict = Depends(common_parameters)):
    return {"q": commons.q, "skip": commons.skip, "limit": commons.limit}
