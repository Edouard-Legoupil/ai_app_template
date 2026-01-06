from crewai.tools import BaseTool
from src.utils.shared_state import shared_state


class DocumentAnalysisTool(BaseTool):
    name: str = "Fetch Document Stories"
    description: str = "Retrieves document context and story, including original purpose, creator, related decisions, alternatives, and data fields."

    def _run(self, doc_id: str):
        story = shared_state.document_registry.get(doc_id, None)
        if story is not None and hasattr(story, "dict"):
            return dict(story.dict())
        elif isinstance(story, dict):
            return story
        else:
            return {}
