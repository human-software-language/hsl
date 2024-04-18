# Browser_tasks.py
from crewai import Task
from textwrap import dedent


class AutomationTasks:
    def build_plan(self, agent, action, website):
        return Task(
            description=dedent(
                f"""
                Action: {action}
                Website: {website}
                Task: Think step by step about expected output based on action. Create step by step plan to implement the action on the target website. Assume that we are already logged in and navigated to necessary page.
                """
            ),
            agent=agent,
        )

    def validate_plan(self, agent):
        return Task(
            description=dedent(
                f"""
                Task: Write source code for the plan and validate each step one by one sending task to QA agent. Fix and improve script and plan based on feedback.
                """
            ),
            agent=agent,
        )

    def create_script_task(self, agent, action, website):
        return Task(
            description=dedent(
                f"""
                Action: {action}
                Website: {website}
                Task: Create step by step plan to implement the action on the target website. After plan creation you should generate playwright script for each step and validate each step one by one sending tasks to QA agent.
                Requirements:
                1. read_website before writing the script
                2. Write only the playwright_actions source code, based on result from read_website
                3. You should always return result to understand if script works correctly, also errors.
                4. There should be self validating mechanism in the script.
                5. You should fix script while it start working.
                6. You should use xpath to find elements.
                7. Assume that the user is already logged in.
                8. playwright_actions.py should started from `def playwright_actions(page):`


                ```python main.py
                from playwright.sync_api import sync_playwright

                with sync_playwright() as p:
                browser = p.chromium.launch_persistent_context(
                    headless=False,
                )
                page = browser.new_page()
                page.goto("{website}")
                playwright_actions(page)
                page.close()
                ```
                """
            ),
            agent=agent,
        )

    def test_script_task(self, agent):
        return Task(
            description=dedent(
                """
                Task: Test the developed Playwright python script on the target website. Provide detailed feedback on the script's performance, including any errors or areas for improvement.
                """
            ),
            agent=agent,
        )
