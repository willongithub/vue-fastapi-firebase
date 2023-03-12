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
