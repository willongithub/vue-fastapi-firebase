from fastapi import (
    APIRouter,
    BackgroundTasks,
    Body,
    HTTPException,
    Request,
    status,
    UploadFile,
)
from fastapi.responses import JSONResponse, HTMLResponse

router = APIRouter()


@router.get("/")
async def root():
    """
    Landing page.
    """
    return {"message": "Hello World"}


@router.get("/login")
async def login():
    """
    Redirect to login portal.
    """
    return {"message": "Login"}


@router.get("/logout")
async def login():
    """
    Logout current user.
    """
    return {"message": "Logout"}


@router.get("/token")
async def token():
    """
    Get auth token.
    """
    return {"message": "Authenticate"}
