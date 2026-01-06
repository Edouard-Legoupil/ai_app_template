from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from src.models.pydantic_models import (
    ReviewRequest,
    ReviewResponse,
    ReviewSectionResult,
)
from src.services.vector_store import vector_store
from crewai import Agent
from src.agents.workflows.living_process_crew import LivingProcessCrew
from src.agents.crew.orchestrator import orchestrator

router = APIRouter()


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
        section_format = section.format if section.format else "markdown"
        prompt = f"Section: {section.name}\nInstructions: {section.instructions}\nFormat: {section_format}\nText: {combined_text}"
        tasks.append(prompt)
    outputs = []
    for agent, prompt in zip(agents, tasks):
        try:
            output = agent.work(prompt)
        except Exception as e:
            output = f"Error running CrewAI agent: {e}"
        outputs.append(output)
    for section, output in zip(request.sections, outputs):
        section_format = section.format if section.format else "markdown"
        results.append(
            ReviewSectionResult(
                name=section.name, content=output, format=section_format
            )
        )
    if request.template:
        doc = request.template.format(**{res.name: res.content for res in results})
    else:
        doc = "\n\n".join(f"## {r.name}\n{r.content}" for r in results)
    return ReviewResponse(sections=results, document=doc)


@router.post("/innovation/trigger")
async def trigger_innovation(request: Request):
    payload = await request.json()
    initial_context = payload.get(
        "initial_context",
        "Select a vendor for Q4 infrastructure project using RFP responses.",
    )
    crew = LivingProcessCrew(initial_context)
    result = crew.kickoff()
    return JSONResponse({"result": result})
