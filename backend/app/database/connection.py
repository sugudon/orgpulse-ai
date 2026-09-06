from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings


# ==========================================
# Database URL
# ==========================================

DATABASE_URL = settings.get_database_url()


# ==========================================
# SQLAlchemy Engine
# ==========================================

engine = create_engine(
    DATABASE_URL,
    echo=settings.DEBUG,
    pool_pre_ping=True,
)


# ==========================================
# Database Session
# ==========================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# ==========================================
# Base Model
# ==========================================

class Base(DeclarativeBase):
    """
    Base class for all database models.
    """

    pass


# ==========================================
# Database Dependency
# ==========================================

def get_db():
    """
    Provides a database session.

    Used as a FastAPI dependency.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ==========================================
# Database Health Check
# ==========================================

def check_database_connection() -> bool:
    """
    Check whether PostgreSQL is reachable.
    """

    try:
        with engine.connect() as connection:
            connection.execute("SELECT 1")

        return True

    except Exception as error:
        print(f"Database connection error: {error}")
        return False