from pydantic_settings import BaseSettings
from pathlib import Path

# This gives us the root of the project (MINDTRACK_AI folder)
BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    # ── App ──────────────────────────────────────────
    APP_NAME: str = "MindTrack AI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    API_PREFIX: str = "/api/v1"

    # ── Security ─────────────────────────────────────
    SECRET_KEY: str = "change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # ── Database ──────────────────────────────────────
    DATABASE_URL: str = f"sqlite:///{BASE_DIR}/data/mindtrack.db"

    # ── ML Paths ──────────────────────────────────────
    MODEL_DIR: str = str(BASE_DIR / "models")
    DATA_DIR: str = str(BASE_DIR / "data" / "processed")

    class Config:
        env_file = ".env"
        case_sensitive = True


# Single instance used across entire project
settings = Settings()