import pytest
from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "backend"))
)
from main import app


client = TestClient(app)


# Test health endpoint
def test_health():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


# Test document search endpoint (assumes docs/chunks are loaded)
def test_document_search():
    response = client.get("/api/v1/document/search", params={"q": "climate"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Test CrewAI review generation endpoint (stubbed example)
def test_review_generate():
    body = {
        "sections": [
            {
                "name": "Intro",
                "instructions": "Summarize context.",
                "format": "markdown",
            }
        ],
        "pdf_query": "climate",
        "template": "{Intro}",
    }
    response = client.post("/api/v1/review/generate", json=body)
    assert response.status_code == 200
    assert "document" in response.json() or hasattr(response.json(), "document")


# Test innovation trigger endpoint (CrewAI orchestration)
def test_innovation_trigger():
    body = {
        "initial_context": "Select a vendor for Q4 infrastructure project using RFP responses."
    }
    response = client.post("/api/v1/innovation/trigger", json=body)
    assert response.status_code == 200
    assert "result" in response.json() or hasattr(response.json(), "result")
