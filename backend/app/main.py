from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.init_db import initialize_database
from app.core.config import settings


# ==========================================
# Create FastAPI Application
# ==========================================

app = FastAPI(
    title=settings.APP_NAME,
    description=(
        "An Agentic Hybrid RAG System "
        "for Organizational Intelligence"
    ),
    version="1.0.0",
    debug=settings.DEBUG,
)


# ==========================================
# CORS Configuration
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8501",  # Streamlit
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# Root Endpoint
# ==========================================

@app.get("/", tags=["System"])
async def root():
    """
    Root endpoint.
    """

    return {
        "message": "Welcome to OrgPulse AI",
        "status": "running",
        "environment": settings.APP_ENV,
    }


# ==========================================
# Health Check
# ==========================================

@app.get("/health", tags=["System"])
async def health_check():
    """
    Health check endpoint.
    """

    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "environment": settings.APP_ENV,
    }


# ==========================================
# Application Startup
# ==========================================

@app.on_event("startup")
async def startup_event():

    print("=" * 50)
    print(f"🚀 {settings.APP_NAME} is starting...")
    print(f"Environment: {settings.APP_ENV}")

    # Initialize database
    initialize_database()

    print("=" * 50)


# ==========================================
# Application Shutdown
# ==========================================

@app.on_event("shutdown")
async def shutdown_event():
    """
    Runs when the application shuts down.
    """

    print(f"🛑 {settings.APP_NAME} is shutting down...")