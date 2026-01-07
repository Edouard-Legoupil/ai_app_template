from fastapi import APIRouter
from src.models.pydantic_models import (
    ReviewRequest,
    ReviewResponse,
    ReviewSectionResult,
)
from src.services.vector_store import vector_store
from crewai import Agent, Crew

router = APIRouter()

from agents.workflows.living_process_crew import LivingProcessCrew
from shared_state import shared_state
from fastapi import Body
from fastapi.responses import JSONResponse
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
)
from agents.workflows.living_process_crew import LivingProcessCrew
from shared_state import shared_state
from fastapi import Body
from fastapi.responses import JSONResponse


@router.post("/review/generate")
def generate_review(request: ReviewRequest):
    # For each section spec, create an agent and run its task
    results = []
    agents = []
    tasks = []
    for section in request.sections:
        # Get relevant chunks for the section based on query (if any)
        if request.pdf_query:
            chunks = vector_store.search(request.pdf_query)
        else:
            chunks = vector_store.chunks[:5]  # fallback: first 5 chunks
        combined_text = "\n".join(c["text"] for c in chunks)
        # Setup CrewAI agent for this section
        agent = Agent(
            role=f"{section.name} Writer",
            goal=section.instructions,
            backstory="Expert academic reviewer.",
        )
        agents.append(agent)
        # Use plain str for format or fallback
        section_format = section.format if section.format else "markdown"
        prompt = f"Section: {section.name}\nInstructions: {section.instructions}\nFormat: {section_format}\nText: {combined_text}"
        tasks.append(prompt)
    # Orchestrate agents/tasks via Crew
    # CrewAI orchestration (fall back to manual loop)
    outputs = []
    for agent, prompt in zip(agents, tasks):
        # CrewAI API might use agent.work(prompt) or another function, adapt below if needed
        output = f"Stubbed CrewAI output for section: {prompt[:80]}..."  # Replace with CrewAI call when API available
        outputs.append(output)
    results = []
    for section, output in zip(request.sections, outputs):
        section_format = section.format if section.format else "markdown"
        results.append(
            ReviewSectionResult(
                name=section.name,
                content=output,  # Should be actual agent output when API correct
                format=section_format,
            )
        )
    # Format final document
    if request.template:
        doc = request.template.format(**{res.name: res.content for res in results})
    else:
        doc = "\n\n".join(f"## {r.name}\n{r.content}" for r in results)
    return ReviewResponse(sections=results, document=doc)
