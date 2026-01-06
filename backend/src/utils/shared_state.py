from typing import Dict, List, Any, Optional
from pydantic import BaseModel


class DecisionRecord(BaseModel):
    decision_point_id: str
    options_considered: List[Dict]  # each dict: {'option', 'pros', 'cons', 'risks'}
    chosen_option: Dict
    rationale: str
    human_maker: Optional[str]
    timestamp: str
    downstream_impacts: List[str] = []


class DocumentStory(BaseModel):
    doc_id: str
    original_purpose: str
    creator_role: str
    related_decisions: List[str]
    alternative_versions: List[Dict] = []
    extracted_data: Dict


class ProcessState(BaseModel):
    active_decisions: List[DecisionRecord] = []
    document_registry: Dict[str, DocumentStory] = {}
    constraints: List[str] = []
    opportunities: List[str] = []
    completed_actions: List[Dict] = []


shared_state = ProcessState()
