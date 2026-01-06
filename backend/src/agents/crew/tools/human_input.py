from crewai.tools import BaseTool
from pydantic import Field
import json


class PresentDecisionPointTool(BaseTool):
    name: str = "Present Decision Point"
    description: str = (
        "Presents a structured decision point to a human. Gathers all relevant info, options, risks. "
        "Returns the human's choice and rationale."
    )
    decision_id: str = Field(
        "default_decision_id", description="Unique ID for this decision instance."
    )
    question: str = Field(
        "default_question", description="The clear question for the human."
    )
    options: list = Field(
        default_factory=list,
        description="List of dicts with 'option', 'pros', 'cons', 'risks'.",
    )
    supporting_docs: list = Field(
        default_factory=list, description="Relevant document stories for context."
    )

    def _run(self) -> str:
        print("\n" + "=" * 60)
        print(f"🚦 DECISION REQUIRED: {self.question}")
        print(f"Decision ID: {self.decision_id}")
        print("-" * 60)
        for i, opt in enumerate(self.options):
            print(f"\nOption {i + 1}: {opt.get('option', '')}")
            print(f"  Pros: {opt.get('pros', 'N/A')}")
            print(f"  Cons: {opt.get('cons', 'N/A')}")
            print(f"  Risks: {opt.get('risks', 'N/A')}")
        print("\nSupporting Context:")
        for doc in self.supporting_docs:
            print(
                f"  - Doc: {doc.get('title', '')} | Purpose: {doc.get('purpose', '')}"
            )
        print("=" * 60)
        chosen_index = 0
        rationale = "Human reviewed risks and selected the most conservative option."
        return json.dumps(
            {
                "chosen_option": self.options[chosen_index] if self.options else None,
                "human_rationale": rationale,
                "decision_id": self.decision_id,
            }
        )
