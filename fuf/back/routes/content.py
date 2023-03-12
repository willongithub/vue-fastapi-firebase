from fastapi import (
    APIRouter,
    BackgroundTasks,
    Body,
    HTTPException,
    Request,
    status,
    UploadFile,
)
from fastapi.responses import JSONResponse, HTMLResponse, Depends
from back.config.model import Item

router = APIRouter()


async def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@router.post("/items/", response_model=Item, summary="Create item")
async def create_item(
    item: Item = Body(
        example={
            "name": "string",
            "description": "string",
            "tag": "string",
        }
    )
):
    """
    Create an item with all the information:
    - **name**: each item must have a name
    - **description**: a long description
    - **tag**: a unique tag strings for this item
    """
    return item


@router.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return {"q": commons.q, "skip": commons.skip, "limit": commons.limit}
