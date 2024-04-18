import os
import re
import dspy
import json
from tools.browser import BrowserCodeExecutor
import yaml
from utils.process_yaml import process_yaml
from utils.process_errors import message_exists_in_yaml


def parse_python_code(code_string):
    """
    Extracts JavaScript code from a string that contains the code wrapped in triple backticks.

    Args:
        code_string (str): The string containing the JavaScript code wrapped in triple backticks.

    Returns:
        str: The extracted JavaScript code.
    """
    # Regular expression to match code within triple backticks, optionally preceded by 'javascript'
    pattern = r"```python\s*([\s\S]*?)```|```([\s\S]*?)```"
    match = re.search(pattern, code_string)

    if match:
        # Return the first non-None group found
        return next(
            (group for group in match.groups() if group is not None), ""
        ).strip()
    else:
        return ""


def dump_yaml_excluding_properties(yaml_obj, exclude_keys):
    # Create a copy of the object excluding specified keys
    yaml_copy = {k: v for k, v in yaml_obj.items() if k not in exclude_keys}

    # Perform the dump on the copy
    yaml_str = yaml.dump(yaml_copy)

    return yaml_str


class InitialCodeSignature(dspy.Signature):
    'Write python playwright source code to control browser like a human. Source code should be appended to our current codebase: `import yaml\nfrom playwright.sync_api import sync_playwright\nyaml_obj = yaml.safe_load(yaml)\nplaywright = sync_playwright().start()\nbrowser = playwright.chromium.launch(headless=True)` - Do not repeat that code, you should use that variables and don\'t close browser. Code should started from `from playwright.sync_api._generated import Browser\n\ndef execute(browser: Browser, yaml_obj, result={"errors": [], "result": []}):\ntry:\n` - write only that function, nothing else.'
    yaml = dspy.InputField(
        desc="""Detailed yaml description of our system.""",
    )
    init_code = dspy.OutputField(
        desc="""
Python source code to execute validation_steps. You should always save result and errors to `result` variable. So each time make and collect as much experiments and hypothesis inside python logic as possible to build context for LLM in `result`. You should always use try-catch to find and throw errors, cleanup resources and close pages in finally block.
""",
    )


class InitCodeModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.init_code = dspy.ChainOfThought(InitialCodeSignature)

    def forward(self, yaml: str) -> dspy.Prediction:
        result = self.init_code(yaml=yaml)
        return parse_python_code(result.init_code)


class FindSelectorsSignature(dspy.Signature):
    """
    Generates Python code to dynamically adjust and test web element selectors in a browser automation context.
    Source code should be appended to our current codebase: `from playwright.sync_api import sync_playwright\nplaywright = sync_playwright().start()\nbrowser = playwright.chromium.launch(headless=True)` - Do not repeat that code, you should use that variables and don\'t close browser. Code should started from `from playwright.sync_api._generated import Browser\nfrom typing import Callable\n\ndef execute(browser: Browser, validate_dom: Callable[[], str], result={"errors": [], "result": []}):\ntry:\n` - write only that function, nothing else.'
    """

    yaml = dspy.InputField(
        desc="YAML configuration of the automation task, including actions and initial selectors. Python code use selectors from here."
    )

    errors = dspy.InputField(
        desc="List of errors encountered with the current selectors, used to guide the improvement process. You should analyze it and find best strategies to detect actual selectors."
    )

    py_code = dspy.OutputField(
        desc="Python code with enhanced selector strategies, designed to overcome the identified selector issues. Each time make and collect as much experiments and hypothesis inside python logic as possible to build context for LLM in `result`. You should always use try-catch to find and throw errors, cleanup resources and close pages in finally block. You should wait all necessary events."
    )


class FindSelectorsModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.init_code = dspy.ChainOfThought(FindSelectorsSignature)

    def forward(self, yaml: str, errors: str) -> dspy.Prediction:
        result = self.init_code(yaml=yaml, errors=errors)
        return parse_python_code(result.py_code)


class YamlValidation(dspy.Module):
    def __init__(self, model="gpt-4"):
        super().__init__()
        self.browser = BrowserCodeExecutor()
        self.browser.start()
        self.lm = dspy.OpenAI(model=model, max_tokens=4096)
        dspy.settings.configure(lm=self.lm)
        self.init_code = InitCodeModule()
        self.find_selectors = FindSelectorsModule()

    def forward(
        self, yaml_obj: yaml, iteration=0, py_code=None, result=None
    ) -> dspy.Prediction:
        max_iterations = 10

        # generate initial code
        """
        if not py_code:
            # Now passing serialized strings to `self.validate.forward`
            py_code = self.init_code.forward(
                yaml=dump_yaml_excluding_properties(
                    yaml_obj,
                    [
                        "errors",
                        "user_interface",
                        "steps",
                        "selectors",
                        "validation_steps",
                    ],
                )
            )
            result = self.browser.execute_python(
                py_code=py_code, yaml_obj=stripped_yaml_obj
            )
        """
        while iteration < max_iterations:

            # Serialize `iteration` and `results` into JSON strings
            # results_str = json.dumps(result, separators=(",", ":"))
            # There can be selectors or code error, we should fix them independently
            improved_code = self.find_selectors.forward(
                yaml=dump_yaml_excluding_properties(
                    yaml_obj, ["errors", "user_interface", "steps"]
                ),
            )

            improved_result = self.browser.execute_python(py_code=improved_code)
            iteration += 1

            print(improved_result)

        prediction = dspy.Prediction(result=result)
        self.lm.inspect_history(n=10)
        return prediction


def main():
    # Discover
    yaml_validation = YamlValidation(model="gpt-4")
    # self_discover = SelfDiscover(model="gpt-3.5-turbo-0125")

    "Write email at outlook.com to dasda@dasd.com about last news in AI"
    "Parse all ai projects managers in London at linkedin"

    google_parsing_yaml = yaml.safe_load(
        open(os.path.join(os.path.dirname(__file__), "yaml", "google_30.yaml"), "r")
    )
    result = yaml_validation.forward(yaml_obj=google_parsing_yaml)
    print(result)


if __name__ == "__main__":
    main()
