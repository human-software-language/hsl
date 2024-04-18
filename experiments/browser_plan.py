import dspy
import re


# Build step by step guide, where each step have typescript functions signatures.
# STAGE 1: ADAPT


"""
data_request = dspy.OutputField(
    desc="Data that must be requested from the user in order to carry out the plan/
    Example: email and password",
)"""


def check_expected_output_format(text):
    """
    Checks if the given text matches the expected format "table: element1, element2, ...".

    Args:
    - text (str): The input text to check.

    Returns:
    - bool: True if the text matches the expected format, False otherwise.
    """
    # Step 1: Check Prefix
    if not text.startswith("table:"):
        return False

    # Remove "table:" and strip leading/trailing whitespace
    elements_str = text[len("table:") :].strip()

    # Step 2: Split Elements
    elements = elements_str.split(",")

    # Step 3: Trim and Validate Elements
    for element in elements:
        trimmed_element = element.strip()
        # Ensure element is non-empty
        if not trimmed_element:
            return False
        # Additional element validation can go here (e.g., check for allowed characters)

    # Step 4: Return Result
    return True


class StepByStepPlanSignature(dspy.Signature):
    """You should solve that task like a human but in fully automated way controlling browser."""

    task_description = dspy.InputField(
        desc="""Detailed task description with algorithm how predict expected_output and step_by_step_plan for current task_description""",
    )
    expected_output = dspy.OutputField(
        desc="""expected output in format `table: element1, element2, ...` or `text: gist in short`""",
    )
    step_by_step_plan = dspy.OutputField(
        desc="""
        Detailed step-by-step plan. Write only plan, nothing else. Every line should started from step number""",
    )


class StepByStepPlanModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate = dspy.ChainOfThought(StepByStepPlanSignature)
        dspy.Retrieve

    def forward(self, task_description: str) -> dspy.Prediction:
        result = self.generate(
            task_description=task_description,
        )
        return result.expected_output, result.step_by_step_plan


class ValidateMarkdown(dspy.Signature):
    """You should solve that task like a human but in fully automated way controlling browser."""

    task_description = dspy.InputField(
        desc="""Detailed task description with algorithm how predict expected_output and step_by_step_plan for current task_description""",
    )
    expected_output = dspy.OutputField(
        desc="""expected output in format `table: element1, element2, ...` or `text: gist in short`""",
    )
    step_by_step_plan = dspy.OutputField(
        desc="""
        Detailed step-by-step plan. Write only plan, nothing else. Every line should started from step number""",
    )


class BrowserDiscover(dspy.Module):
    def __init__(self, model="gpt-3.5-turbo-0125"):
        super().__init__()

        # lm = dspy.OpenAI(model="gpt-3.5-turbo-0125", max_tokens=4096)
        # lm = dspy.OpenAI(model="gpt-4-turbo-preview", max_tokens=4096)
        self.lm = dspy.OpenAI(model=model, max_tokens=4096)
        dspy.settings.configure(lm=self.lm)

        self.step_by_step_module = StepByStepPlanModule()

    def forward(self, task_description: str) -> dspy.Prediction:
        expected_output, step_by_step_plan = self.step_by_step_module.forward(
            task_description
        )

        """
        dspy.Suggest(
            check_expected_output_format(expected_output),
            "Output should be in format `table: element1, element2, ...`",
            target_module=StepByStepPlanModule,
        )"""

        prediction = dspy.Prediction(
            expected_output=expected_output, step_by_step_plan=step_by_step_plan
        )
        self.lm.inspect_history(n=10)
        # SOLUTION
        return prediction


def main():

    # Discover
    self_discover = BrowserDiscover(model="gpt-4")
    # self_discover = SelfDiscover(model="gpt-3.5-turbo-0125")

    "Write email at outlook.com to dasda@dasd.com about last news in AI"
    "Parse all ai projects managers in London at linkedin"

    task = """
    We have few examples, each of them have: task_description, expected_output and step_by_step_plan.
    
    If task_description is `Search in google wakeboarding spots near Fortaleza, Brazil.` expected_output should be `table: title, snippet, url` and step_by_step_plan is:
    ```
    ## Globals
    De
    Output:
    ## Steps
    
    1. Go to `https://www.google.com/search?q=Parque%20de%20wakeboard%20Fortaleza%20Brasil`
    2. Find search bar and type "Parque de wakeboard Fortaleza Brasil"
    3. Click search button
    4. Parse all results on first page into table
    ```
    
    Or task is to predict expected_output and step_by_step_plan if our task_description is `Write email at outlook.com to dasda@dasd.com about last news in AI`
    """
    result = self_discover.forward(task)
    print(result)


if __name__ == "__main__":
    main()

"""


    If task_description is `Parse all ai projects managers in London at linkedin` expected_output should be `table: name, job title, company[], url` and step_by_step_plan is:
    ```
    1. Go to https://google.com
    2. Find search bar and type "Parque de wakeboard Fortaleza Brasil"
    3. Click search button
    4. Parse all results on first page into table
    ```

"""
