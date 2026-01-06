from crewai import Agent
from src.services.llm_service import llm
from .tools.human_input import PresentDecisionPointTool
from .tools.document_context import DocumentAnalysisTool
from .tools.path_tracker import UpdatePathTrackerTool
from .tools.reality_updater import RealityUpdaterTool



present_decision_tool = PresentDecisionPointTool(
    decision_id="default_decision_id",
    question="default_question",
    options=[],
    supporting_docs=[],
)
document_context_tool = DocumentAnalysisTool()
path_tracker_tool = UpdatePathTrackerTool()
reality_updater_tool = RealityUpdaterTool()

orchestrator = Agent(
    role="Process Orchestrator and Decision Facilitator",
    goal="Guide innovation adoption by identifying decision points, gathering context, involving humans, and updating the shared process map.",
    backstory="You are designed to facilitate structured, documented, and ripple-tracking decisions at every process node.",
    verbose=True,
    llm=llm,
    tools=[
        present_decision_tool,
        document_context_tool,
        path_tracker_tool,
        reality_updater_tool,
    ],
    max_iter=15,
)
