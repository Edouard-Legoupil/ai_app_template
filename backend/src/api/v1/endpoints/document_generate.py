from fastapi import APIRouter, Body
from src.api.v1.template.template_loader import load_template
from crewai import Agent

router = APIRouter()


@router.post("/document/generate")
def generate_document_template(payload: dict = Body(...)):
    template_name = payload.get("template_name")
    context = payload.get("context", "")
    if not template_name:
        return {"error": "template_name required"}
    template = load_template(template_name)
    results = []
    for section in template.get("sections", []):
        instructions = section.get("instructions", "")
        agent = Agent(role=f"{section['name']} Writer", goal=instructions)
        output = agent.work(f"Context: {context}\nInstructions: {instructions}")
        results.append({"section": section["name"], "content": output})
    return {"document_name": template.get("name", template_name), "sections": results}
