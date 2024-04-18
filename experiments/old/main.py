# main.py
from dotenv import load_dotenv
from browser_agents import AutomationAgents
from browser_tasks import AutomationTasks
from crewai import Crew
from tools.browser import browser

# Load environment variables if needed
load_dotenv()


class InteractiveAutomationCrew:
    def __init__(self, action, website):
        self.action = action
        self.website = website

    def run(self):
        agents = AutomationAgents()
        tasks = AutomationTasks()

        browser.initialize_browser_context(url=self.website)

        plan_builder = agents.plan_builder()
        script_creator = agents.create_script_creator()
        script_tester = agents.create_script_tester()

        # Initialize tasks with dynamic feedback mechanism
        build_plan_task = tasks.build_plan(plan_builder, self.action, self.website)
        validate_plan_task = tasks.validate_plan(plan_builder)
        # script_testing_task = tasks.test_script_task(script_tester)

        # Create a crew with the agents and their tasks
        crew = Crew(
            agents=[plan_builder, script_creator, script_tester],
            tasks=[build_plan_task, validate_plan_task],
            verbose=2,
        )

        result = crew.kickoff()

        return result


def main():
    # User input for the action and website
    action = "Show current full profile"
    website = "https://www.linkedin.com"

    interactive_crew = InteractiveAutomationCrew(action, website)
    final_script = interactive_crew.run()

    # Display the final script
    print("Final Automation Script:", final_script)


if __name__ == "__main__":
    main()
