from datetime import datetime, timedelta

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
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from back.config.models import User, UserInDB
from back.utils import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    authenticate_user,
    create_access_token,
    get_current_user,
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
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
    user = authenticate_user(login_data.username, login_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token}


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
