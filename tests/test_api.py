"""Tests for API endpoints."""

import pytest
from fastapi.testclient import TestClient

from sheaia.api import app


@pytest.fixture
def client():
    """Create test client."""
    return TestClient(app)


class TestHealthEndpoints:
    """Tests for health check endpoints."""
    
    def test_health_check(self, client):
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "sheaia"
    
    def test_readiness_check(self, client):
        response = client.get("/health/ready")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ready"


class TestChatEndpoints:
    """Tests for chat endpoints."""
    
    def test_chat_basic(self, client):
        response = client.post("/api/v1/chat", json={
            "message": "Hello, SHEAIA!"
        })
        assert response.status_code == 200
        data = response.json()
        assert "response" in data
        assert "conversation_id" in data
    
    def test_chat_with_language(self, client):
        response = client.post("/api/v1/chat", json={
            "message": "你好",
            "language": "zh-CN"
        })
        assert response.status_code == 200
        data = response.json()
        assert "response" in data
    
    def test_chat_empty_message(self, client):
        response = client.post("/api/v1/chat", json={
            "message": ""
        })
        assert response.status_code == 422  # Validation error
