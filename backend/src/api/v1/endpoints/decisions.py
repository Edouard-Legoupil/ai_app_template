from fastapi import APIRouter, HTTPException, Body
from typing import List, Dict

router = APIRouter()

# In-memory data store (simulate demo process state)
pending_decisions = [
    {
        "id": "decision-1",
        "question": "Which vendor should we select for infrastructure?",
        "context": "Q4 Cloud RFP responses reviewed.",
        "options": [
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
        ],
        "supporting_docs": [
            {"doc_id": "rfp-summary", "title": "RFP Summaries", "type": "report"}
        ],
    }
]
decision_history: List[Dict] = []

ripple_data = {
    "decision-1": {
        "paths": [
            {
                "outcome": "Choose Vendor_A",
                "description": "Fast onboarding, lower costs",
                "risks": "Potential compliance audit",
                "next_nodes": ["onboarding", "legal-review"],
            },
            {
                "outcome": "Choose Vendor_B",
                "description": "More robust SLA, higher OPEX",
                "risks": "Budget overrun",
                "next_nodes": ["onboarding", "exec-approval"],
            },
        ]
    }
}

process_story = [
    {
        "id": "evt-101",
        "type": "document",
        "summary": "RFP Summary uploaded",
        "timestamp": "2024-07-01T09:30:00Z",
        "related_doc": "rfp-summary",
    },
    {
        "id": "evt-102",
        "type": "decision",
        "summary": "Chose Vendor_A",
        "timestamp": "2024-07-02T11:01:00Z",
        "related_decision": "decision-1",
    },
]

collective_context = {
    "teamGoal": "Complete vendor onboarding by Aug 1st",
    "updates": [
        "Decision Made: Vendor selected",
        "Procurement process started",
        "Doc: SLA drafted",
    ],
}


@router.get("/decisions/pending")
def get_pending_decisions():
    return {"decisions": pending_decisions}


@router.post("/decisions/{decision_id}/submit")
def submit_decision(decision_id: str, body: dict = Body(...)):
    choice = body.get("choice")
    rationale = body.get("rationale")
    # Simulate recording & removing decision
    dec = next((d for d in pending_decisions if d["id"] == decision_id), None)
    if not dec:
        raise HTTPException(status_code=404, detail="Decision not found")
    pending_decisions.remove(dec)
    decision_history.append(
        {"id": decision_id, "choice": choice, "rationale": rationale}
    )
    return {"status": "ok"}


@router.get("/decisions/{decision_id}/ripple")
def get_ripple(decision_id: str):
    data = ripple_data.get(decision_id)
    if not data:
        raise HTTPException(status_code=404, detail="Ripple data not found")
    return data


@router.get("/process/thread")
def get_process_thread():
    return {"events": process_story}


@router.get("/collective_context")
def get_collective_context():
    return collective_context
