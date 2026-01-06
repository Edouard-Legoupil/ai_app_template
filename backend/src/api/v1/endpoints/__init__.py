from fastapi import APIRouter
from .document import router as document_router

api_router = APIRouter()
api_router.include_router(document_router, prefix="", tags=["Document"])
from .ai_agents import router as ai_agents_router

api_router.include_router(ai_agents_router, prefix="", tags=["AI Agents"])
from .templates import router as templates_router

api_router.include_router(templates_router, prefix="", tags=["Templates"])
from .document_generate import router as document_generate_router

api_router.include_router(
    document_generate_router, prefix="", tags=["Document Generate"]
)
