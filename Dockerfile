# SHEAIA Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY pyproject.toml README.md ./
RUN pip install --no-cache-dir -e .

# Copy application code
COPY sheaia/ ./sheaia/
COPY config/ ./config/

# Create data directories
RUN mkdir -p data models

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "-m", "sheaia.cli", "serve"]
