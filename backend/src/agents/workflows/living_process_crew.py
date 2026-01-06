from crewai import Crew, Process
from src.agents.crew.orchestrator import orchestrator
from src.agents.crew.tasks.decision_points import make_vendor_selection_task
# from shared_state import shared_state  # This import appears unused or missing; commented out for now.


class LivingProcessCrew:
    def __init__(self, initial_context):
        self.initial_context = initial_context
        self.crew = None

    def setup(self):
        kickoff_task = make_vendor_selection_task(
            orchestrator_agent=orchestrator, context=self.initial_context
        )
        self.crew = Crew(
            agents=[orchestrator],
            tasks=[kickoff_task],
            process=Process.sequential,
            verbose=True,
        )

    def kickoff(self):
        if not self.crew:
            self.setup()
        results = None
        if self.crew is not None:
            results = self.crew.kickoff()
        return results


if __name__ == "__main__":
    initial_context = (
        "Select a vendor for Q4 infrastructure project using RFP responses."
    )
    crew = LivingProcessCrew(initial_context)
    final_result = crew.kickoff()
