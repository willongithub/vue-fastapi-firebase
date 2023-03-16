from pydantic import BaseSettings


class Settings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8848
    DEBUG_MODE: bool = True

    class Config:
        # `.env.prod` takes priority over `.env`
        env_file = ".env.dev", ".env.prod"
