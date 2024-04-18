# browser_agents.py
from crewai import Agent
from tools.search_tools import SearchTools
from tools.browser_tools import BrowserTools


class AutomationAgents:
    def plan_builder(self):
        return Agent(
            role="Plan Builder",
            goal="Build a step by step plan for automation script.",
            backstory="A skilled developer adept at creating flexible automation plans for various web applications. Known for their ability to quickly adapt plans based on testing feedback.",
            allow_delegation=False,
            verbose=True,
        )

    def create_script_creator(self):
        return Agent(
            role="Developer",
            goal="""
            Generate python playwright source code.
            Requirements:
            0. You should use read_website if you do not know real selectors.
            1. Result or error should always be saved to `result` variable.
            2. There should be self validating mechanism in the script.
            3. You should fix script while it start working.
            4. You should use xpath to find elements.
            5. Assume that the user is already logged in.
            6. playwright_actions.py should started from `def playwright_actions(page):`


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
            """,
            backstory="""
            A skilled developer adept at creating flexible automation scripts for various web applications. Known for their ability to quickly adapt scripts based on testing feedback. It should test result by executing source code using QA agent.
            """,
            tools=[BrowserTools.read_website],
            allow_delegation=False,
            verbose=True,
        )

    def create_script_tester(self):
        return Agent(
            role="Quality Assurance Specialist",
            goal="Test automation scripts on the target website and provide feedback for improvements.",
            backstory="An experienced QA specialist who excels in testing web automation scripts, identifying flaws, and suggesting enhancements to ensure script effectiveness and reliability.",
            tools=[BrowserTools.execute_code],
            allow_delegation=False,
            verbose=True,
        )


class ResearcherAgents:
    def create_script_creator(self):
        return Agent(
            role="Automation Developer",
            goal="Dynamically generate and adapt sync Playwright scripts to perform specified actions on a target website. Always test source code using QA agent and make sure that it works correctly.",
            backstory="""
            A skilled developer adept at creating flexible automation scripts for various web applications. Known for their ability to quickly adapt scripts based on testing feedback. It should test result by executing source code using QA agent.
            """,
            tools=[BrowserTools.read_website],
            allow_delegation=True,
            verbose=True,
        )

    def source_finder(self):
        return Agent(
            role="Sources finder",
            goal="Iteratively improving query find best sources with necessary information and return link for that source.",
            backstory="Google search tips expert, has access only to google snippets that use search queries with long tail and with inurl: parameter and validate results, he think step by step how to improve query, until you find ideal answer with necessary information. After each research you should think step by step how to improve query or return link to best source. Maximum 10 iterations.",
            tools=[
                # BrowserTools.scrape_and_summarize_webpage,
                BrowserTools.scrape_and_summarize_webpage,
            ],
            allow_delegation=False,
            verbose=True,
        )

    def table_manager(self):
        return Agent(
            role="Table Manager",
            goal="Fulfill table with necessary information.",
            backstory="Work with inmemory tables. Should fulfill only validated information. Do not write information that is not real.",
            tools=[],
            allow_delegation=False,
            verbose=True,
        )

    def create_research_agent(self):
        return Agent(
            role="Research Agent",
            goal="Gather preliminary information on a specific topic",
            backstory="An experienced researcher known for uncovering hidden gems of information and setting the foundation for in-depth analysis.",
            tools=[BrowserTools.scrape_and_summarize_webpage],
            verbose=True,
        )

    def create_analysis_agent(self):
        return Agent(
            role="Analysis Agent",
            goal="Analyze the gathered data for relevance and depth",
            backstory="A meticulous analyst with a knack for discerning patterns and insights from complex datasets, always aiming to extract the most relevant information.",
            tools=[BrowserTools.scrape_and_summarize_webpage],
            verbose=True,
        )

    def create_synthesis_agent(self):
        return Agent(
            role="Synthesis Agent",
            goal="Compile and synthesize information into a coherent document",
            backstory="A skilled writer and synthesizer, adept at weaving together disparate pieces of information into a comprehensive and engaging narrative.",
            verbose=True,
        )
