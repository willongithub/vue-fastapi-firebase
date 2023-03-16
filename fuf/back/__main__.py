import uvicorn
from back.config.settings import Settings


settings = Settings()

uvicorn.run(
    "back.app:api",
    host=settings.HOST,
    port=settings.PORT,
    reload=settings.DEBUG_MODE,
)
