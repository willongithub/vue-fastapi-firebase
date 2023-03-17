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
from fastapi.security import OAuth2PasswordBearer

from back.config.models import Item
from back.utils import common_parameters

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()


@router.post("/items/", response_model=Item, summary="Create item")
async def create_item(
    token: str = Depends(oauth2_scheme),
    item: Item = Body(
        example={
            "name": "string",
            "description": "string",
            "tag": "string",
        }
    ),
):
    """
    Create an item with all the information:
    - **name**: each item must have a name
    - **description**: a long description
    - **tag**: a unique tag strings for this item
    """
    return item


@router.get("/items/")
async def read_items(
    token: str = Depends(oauth2_scheme),
    commons: dict = Depends(common_parameters),
):
    return {"q": commons.q, "skip": commons.skip, "limit": commons.limit}
