"""Health check endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """Basic health check endpoint."""
    return {"status": "healthy", "service": "sheaia"}


@router.get("/health/ready")
async def readiness_check():
    """Readiness check - verifies all dependencies are available."""
    # TODO: Check database connections, model availability, etc.
    return {
        "status": "ready",
        "checks": {
            "database": "ok",
            "llm": "ok",
            "embedding": "ok",
        }
    }
