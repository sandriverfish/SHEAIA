"""SHEAIA CLI commands."""

import logging
import sys

import uvicorn

from sheaia.config import get_settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def serve():
    """Start the API server."""
    settings = get_settings()
    
    logger.info(f"Starting SHEAIA server on {settings.api.host}:{settings.api.port}")
    
    uvicorn.run(
        "sheaia.api:app",
        host=settings.api.host,
        port=settings.api.port,
        reload=settings.api.reload,
        workers=settings.api.workers if not settings.api.reload else 1,
    )


def download_models():
    """Download required models."""
    logger.info("Model download functionality - to be implemented")
    logger.info("Please manually download models to the models/ directory:")
    logger.info("  - LLM: Qwen2.5-14B-Instruct-GGUF (Q4_K_M)")
    logger.info("  - Embedding: BAAI/bge-m3")


def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("SHEAIA CLI")
        print("Usage: python -m sheaia.cli <command>")
        print("")
        print("Commands:")
        print("  serve           Start the API server")
        print("  download-models Download required models")
        return
    
    command = sys.argv[1]
    
    if command == "serve":
        serve()
    elif command == "download-models":
        download_models()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
