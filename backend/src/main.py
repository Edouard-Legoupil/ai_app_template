import os
import sys
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse

from src.api.v1.endpoints import api_router

# Initialize app
app = FastAPI(title="AI App Boilerplate", version="0.1.0")

# Allow CORS for development (React dev server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Determine dev/prod environment
IS_DEV = os.getenv("ENVIRONMENT", "development") == "development"
FRONTEND_BUILD_PATH = Path(__file__).parent / "static"

# API Routes
app.include_router(api_router, prefix="/api/v1")

# Static file serving for production
if not IS_DEV and FRONTEND_BUILD_PATH.exists():
    app.mount(
        "/static",
        StaticFiles(directory=str(FRONTEND_BUILD_PATH / "static")),
        name="static",
    )

    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        if full_path.startswith("api/"):
            return JSONResponse({"error": "Not found"}, status_code=404)
        index_path = FRONTEND_BUILD_PATH / "index.html"
        if index_path.exists():
            return FileResponse(index_path)
        return JSONResponse({"error": "Frontend not built"}, status_code=500)

    @app.get("/")
    async def serve_root():
        index_path = FRONTEND_BUILD_PATH / "index.html"
        if index_path.exists():
            return FileResponse(index_path)
        return JSONResponse({"error": "Frontend not built"}, status_code=500)


# Health endpoint for Docker healthcheck
@app.get("/api/v1/health")
async def health_check():
    return {"status": "ok"}
