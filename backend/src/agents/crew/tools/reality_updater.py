from crewai.tools import BaseTool
from src.utils.shared_state import shared_state


class RealityUpdaterTool(BaseTool):
    name: str = "Update Landscape"
    description: str = "Updates the external world and shared process state after validated actions (DB/API triggers, post-decision updates)."

    def _run(self, action_update: dict):
        shared_state.completed_actions.append(action_update)
        return action_update
