from fastapi import (
    APIRouter,
    BackgroundTasks,
    Body,
    Depends,
    HTTPException,
    Request,
    UploadFile,
    status,
)
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from back.app import oauth2_scheme
from back.config.models import User, UserInDB
from back.utils import get_current_user, hash_password

router = APIRouter()


@router.get("/")
async def home():
    """
    Home page.
    """
    return {"message": "Hello World!"}


@router.get("/login")
async def login(login_data: OAuth2PasswordRequestForm = Depends()):
    """
    Redirect to login portal.
    """
    user = UserInDB.get(login_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    hashed_password = hash_password(login_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "scope": user.scope}


@router.get("/logout")
async def logout():
    """
    Logout current user.
    """
    return {"message": "Logout"}


@router.get("/token")
async def get_token(
    token: str = Depends(oauth2_scheme),
):
    """
    Get auth token.
    """
    return {"token": token}


@router.get("/user")
async def get_user(
    current_user: User = Depends(get_current_user),
):
    """
    Get current user.
    """
    return current_user
