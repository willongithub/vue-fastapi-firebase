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
from fastapi.security import OAuth2PasswordBearer
from back.utils import common_parameters
from back.config.models import UserIn, User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()


@router.post("/users/", response_model=User, summary="Signup user")
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
