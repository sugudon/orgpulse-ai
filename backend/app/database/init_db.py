from sqlalchemy import text

from app.database.connection import Base, engine


def initialize_database():
    """
    Initialize PostgreSQL database.

    - Enables pgvector extension
    - Creates all database tables
    """

    try:
        # Enable pgvector extension
        with engine.begin() as connection:
            connection.execute(
                text(
                    "CREATE EXTENSION IF NOT EXISTS vector"
                )
            )

        # Import models before creating tables
        # This ensures SQLAlchemy registers all models.
        import app.database.models  # noqa: F401

        # Create tables
        Base.metadata.create_all(bind=engine)

        print("=" * 50)
        print("✅ Database initialized successfully")
        print("✅ pgvector extension enabled")
        print("✅ Tables created successfully")
        print("=" * 50)

    except Exception as error:
        print("=" * 50)
        print("❌ Database initialization failed")
        print(f"Error: {error}")
        print("=" * 50)

        raise


if __name__ == "__main__":
    initialize_database()