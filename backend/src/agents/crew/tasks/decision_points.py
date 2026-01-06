from crewai import Task
from .execution_actions import execute_vendor_contract_task
import datetime


def make_vendor_selection_task(orchestrator_agent, context):
    options = [
        {
            "option": "Vendor_A",
            "pros": "Best price",
            "cons": "Less reputation",
            "risks": "Compliance issues",
        },
        {
            "option": "Vendor_B",
            "pros": "Strong reputation",
            "cons": "Higher cost",
            "risks": "Slower onboarding",
        },
    ]
    question = "Which vendor should we select for cloud services?"
    supporting_docs = []  # Add docs as needed
    decision_id = f"vendor_decision_{datetime.datetime.now().isoformat()}"
    task_description = "Review vendor proposals, analyze risks, present decision to procurement manager, and log rationale."

    def callback(output):
        chosen = options[0]
        downstream = ["Legal review path initiated", "Budget allocation locked"]
        return execute_vendor_contract_task(
            {"chosen_vendor": chosen, "downstream_impacts": downstream}
        )

    return Task(
        description=task_description,
        agent=orchestrator_agent,
        expected_output="Decision record including chosen vendor, rationale, and downstream impacts.",
        async_execution=False,
        callback=callback,
    )
