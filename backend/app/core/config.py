from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central application configuration.

    Values are loaded from the .env file.
    Environment variables override .env values.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ==========================================
    # Application
    # ==========================================

    APP_NAME: str = "OrgPulse AI"
    APP_ENV: str = "development"
    DEBUG: bool = True

    # ==========================================
    # LLM Providers
    # ==========================================

    # OpenAI
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_MODEL: Optional[str] = None

    # Groq
    GROQ_API_KEY: Optional[str] = None
    GROQ_MODEL: Optional[str] = None

    # Ollama
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: Optional[str] = None

    # ==========================================
    # Embeddings
    # ==========================================

    EMBEDDING_MODEL: str = (
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    # ==========================================
    # PostgreSQL + pgvector
    # ==========================================

    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "orgpulse"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: Optional[str] = None

    DATABASE_URL: Optional[str] = None

    # ==========================================
    # RAG Configuration
    # ==========================================

    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 150

    VECTOR_TOP_K: int = 10
    BM25_TOP_K: int = 10
    RERANK_TOP_K: int = 5

    HYBRID_VECTOR_WEIGHT: float = 0.6
    HYBRID_BM25_WEIGHT: float = 0.4

    # ==========================================
    # Reranker
    # ==========================================

    RERANKER_MODEL: str = (
        "cross-encoder/ms-marco-MiniLM-L-6-v2"
    )

    # ==========================================
    # File Upload
    # ==========================================

    UPLOAD_DIR: str = "uploads"
    MAX_FILE_SIZE_MB: int = 20

    # ==========================================
    # FastAPI
    # ==========================================

    FASTAPI_HOST: str = "0.0.0.0"
    FASTAPI_PORT: int = 8000

    # ==========================================
    # Streamlit
    # ==========================================

    STREAMLIT_API_URL: str = "http://localhost:8000"

    # ==========================================
    # Helper Methods
    # ==========================================

    def get_database_url(self) -> str:
        """
        Return the configured database URL.

        If DATABASE_URL is not explicitly provided,
        build it from PostgreSQL environment variables.
        """

        if self.DATABASE_URL:
            return self.DATABASE_URL

        password = self.POSTGRES_PASSWORD or ""

        return (
            f"postgresql+psycopg://"
            f"{self.POSTGRES_USER}:{password}"
            f"@{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )

    def validate_hybrid_weights(self) -> bool:
        """
        Validate hybrid retrieval weights.

        Vector weight + BM25 weight should equal 1.
        """

        total = (
            self.HYBRID_VECTOR_WEIGHT
            + self.HYBRID_BM25_WEIGHT
        )

        return abs(total - 1.0) < 0.001


@lru_cache
def get_settings() -> Settings:
    """
    Return a cached application settings instance.
    """

    settings = Settings()

    if not settings.validate_hybrid_weights():
        raise ValueError(
            "HYBRID_VECTOR_WEIGHT + "
            "HYBRID_BM25_WEIGHT must equal 1.0"
        )

    return settings


# Global settings instance
settings = get_settings()