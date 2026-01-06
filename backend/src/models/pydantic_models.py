from pydantic import BaseModel
from typing import List, Optional


class SectionSpec(BaseModel):
    name: str
    instructions: str
    format: Optional[str] = "markdown"


class ReviewRequest(BaseModel):
    sections: List[SectionSpec]
    template: Optional[str] = None  # Top-level formatting (optional)
    pdf_query: Optional[str] = None  # Core text to select relevant chunks


class ReviewSectionResult(BaseModel):
    name: str
    content: str
    format: str


class ReviewResponse(BaseModel):
    sections: List[ReviewSectionResult]
    document: Optional[str] = None  # Final assembled document
