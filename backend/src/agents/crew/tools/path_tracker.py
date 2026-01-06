from crewai.tools import BaseTool
from src.utils.shared_state import shared_state, DecisionRecord


class UpdatePathTrackerTool(BaseTool):
    name: str = "Track Decision Path"
    description: str = "Logs the downstream impacts, constraints, and opportunities created by a decision."

    def _run(self, decision_record: dict):
        # Convert dict to DecisionRecord if necessary
        dr = None
        if isinstance(decision_record, dict):
            dr = DecisionRecord(**decision_record)
        elif isinstance(decision_record, DecisionRecord):
            dr = decision_record
        else:
            return {}
        shared_state.active_decisions.append(dr)
        impacts = dr.downstream_impacts
        shared_state.constraints += [i for i in impacts if "constraint" in i]
        shared_state.opportunities += [i for i in impacts if "opportunity" in i]
        return {
            "constraints": shared_state.constraints,
            "opportunities": shared_state.opportunities,
        }
