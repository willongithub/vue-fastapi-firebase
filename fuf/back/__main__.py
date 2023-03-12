from fastapi import FastAPI
import uvicorn
from back.routes.index import router as index
from back.routes.content import router as content
from back.routes.manage import router as manage

app = FastAPI()

app.include_router(index, tags=["index"], prefix="")
app.include_router(content, tags=["content"], prefix="/content")
app.include_router(manage, tags=["manage"], prefix="/manage")

def create_app():
    uvicorn.run(
        
    )
        "back:app",
        host=0.0.0.0,
        port=8848,
        reload=True
    )