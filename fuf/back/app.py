from fastapi import FastAPI

from back.routes.index import router as index
from back.routes.content import router as content
from back.routes.manage import router as manage

app = FastAPI()

app.include_router(index, tags=["index"], prefix="")
app.include_router(content, tags=["content"], prefix="/content")
app.include_router(manage, tags=["manage"], prefix="/manage")
