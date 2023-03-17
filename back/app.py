from fastapi import FastAPI

from back.routes.content import router as content
from back.routes.index import router as index
from back.routes.manage import router as manage


api = FastAPI()

api.include_router(index, tags=["index"], prefix="")
api.include_router(content, tags=["content"], prefix="/content")
api.include_router(manage, tags=["manage"], prefix="/manage")
