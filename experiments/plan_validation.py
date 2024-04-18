import os
import re
import dspy
import json
from tools.browser_remote import BrowserCodeExecutor
import yaml
import difflib
from utils.process_yaml import merge_validation_steps


def parse_code_blocks(code_string):
    """
    Extracts code from a string that contains code wrapped in triple backticks. This includes
    blocks starting with ```, ```python, or ```yml.

    Args:
        code_string (str): The string containing the code wrapped in triple backticks.

    Returns:
        str: The extracted code.
    """
    # Regular expression to match code within triple backticks, optionally preceded by 'python' or 'yml'
    pattern = r"```(?:python|yml|yaml)?\s*([\s\S]*?)```"
    matches = re.findall(pattern, code_string)

    if matches:
        # Join all matches separated by two newlines (customize this as needed)
        return "\n\n".join(matches).strip()
    else:
        return ""


class ValidationCodeSignature(dspy.Signature):
    'Write python playwright source code to control browser like a human. Source code should be appended to our current codebase: `from playwright.sync_api import sync_playwright\nplaywright = sync_playwright().start()\nbrowser = playwright.chromium.launch(headless=True)\npage = browser.new_page()` - Do not repeat that code, you should use that variables and don\'t close page. Code should started from `from playwright.sync_api._generated import Page\n\ndef execute(page: Page, result={"py_code_errors": [], "automation_errors": [], "result": []}):\ntry:\n` - write only that function, nothing else.'
    validation_yml = dspy.InputField(
        desc="""Detailed yaml description how to validate our system. We should write source code based on that logic.""",
    )
    code = dspy.OutputField(
        desc="""
Python source code to execute. You should always save result and errors(if exist) to `result` variable and always return `result` variable. So each time make and collect as much experiments and hypothesis inside python logic as possible to build context for LLM in `result`. You should always use try-catch to find and throw errors and always wait necessary async elements after actions. You should write as much possible information into `result` and errors as possible, including selectors, we need that information to guaranty localize the problem and rewrite code to fix that problem. Errors should be detailed as possible, including selectors, error message should provide details of what the problem is and what to do to fix it. So we have only information from `result` and source code, nothing else.
""",
    )


class ValidationCodeModule(dspy.Module):
    def __init__(self, lm):
        super().__init__()
        self.lm = lm
        self.init_code = dspy.ChainOfThought(ValidationCodeSignature)

    def forward(self, validation_yml: dict) -> dspy.Prediction:
        validation_yml: str = (
            "```yml\n" + yaml.dump(validation_yml, sort_keys=False) + "```"
        )
        prediction = self.init_code(validation_yml=validation_yml)
        self.lm.inspect_history(n=1)
        return parse_code_blocks(prediction.code)


class FixCodeSignature(dspy.Signature):
    """
    Analyzes errors and results from a previous execution to generate a revised version of the source code,
    aiming to fix identified issues for more reliable browser automation. You should validate each selector independently. You should always output the full code with a test of all steps and elements.
    """

    code = dspy.InputField(
        desc="The original Python Playwright code that requires debugging or enhancement."
    )
    py_code_errors = dspy.InputField(
        desc="List of Python execution errors encountered during the last run. You should fix all that errors in `new_code`."
    )
    automation_errors = dspy.InputField(
        desc="List of automation-specific errors from the browser interaction process."
    )
    results = dspy.InputField(
        desc="Accumulated results from previous code executions, used to inform code adjustments."
    )
    page = dspy.InputField(
        desc="When analyzing YAML-like output from webpage structures, focus on interpreting elements by their unique deterministic ID (did), HTML tags, relevant attributes, and text content snippets. Use the did to pinpoint specific elements, the tags to understand their role in the webpage (e.g., a for links, button for clickable actions), attributes for additional context like alt text for images or role for accessibility, and textContent to grasp the visible text or function. Your goal is to deduce the significance of each element in the context of user interaction or content presentation, based on this structured information."
    )
    new_code = dspy.OutputField(
        desc="Revised Python Playwright `code` with adjustments to address previous errors and inefficiencies. You should understand `page` structure to fix all necessary selectors, context and make decisions. You should fix all possible selectors using `did` attribute. "
    )


class FixCodeCodeModule(dspy.Module):
    def __init__(self, lm):
        super().__init__()
        self.lm = lm
        self.fix_code = dspy.ChainOfThought(FixCodeSignature)

    def forward(self, code: str, result: dict) -> dspy.Prediction:
        prediction = self.fix_code(
            code=code,
            py_code_errors=str(result["py_code_errors"]),
            automation_errors=str(result["automation_errors"]),
            results=str(result["result"]),
            page="```\n" + result["page"] + "```",
        )
        self.lm.inspect_history(n=1)
        return parse_code_blocks(prediction.new_code)


class FixYMLSignature(dspy.Signature):
    """
    We have yml with browser automation business logic. We should write correct logic to achieve task in the prompt. For that you should modify actions and validation(if necessary) in same rules and fix problems, you can change selectors or actions. Don't modify `prompt` and `var` section. We use deterministic algorithm to append `did` ids to all important DOM elements.
    """
    yml = dspy.InputField()
    code = dspy.InputField()
    py_code_errors = dspy.InputField(
        desc="List of python errors from the browser interaction process."
    )

    automation_errors = dspy.InputField(
        desc="List of automation-specific errors from the browser interaction process."
    )
    results = dspy.InputField(
        desc="Accumulated results from code execution, used to inform code adjustments."
    )
    page = dspy.InputField(
        desc="Focus on interpreting elements by their unique deterministic ID (did), HTML tags, relevant attributes, and text content snippets. Use the did to pinpoint specific elements, the tags to understand their role in the webpage (e.g., a for links, button for clickable actions), attributes for additional context like alt text for images or role for accessibility, and textContent to grasp the visible text or function. Your goal is to deduce the significance of each element in the context of user interaction or content presentation, based on this structured information."
    )
    new_yml = dspy.OutputField(
        desc="Based on page structure and previous experience write new hierarchial yaml with fixed/improved business logic and selectors(sel), actions(act), memory(mem), validation(val). Always choose selectors using `did` attribute."
    )


class FixYMLModule(dspy.Module):
    def __init__(self, lm):
        super().__init__()
        self.lm = lm
        self.fix_yml = dspy.ChainOfThought(FixYMLSignature)

    def forward(
        self, yml: dict, code: str, result: dict
    ) -> dspy.Prediction:
        prediction = self.fix_yml(
            yml="```yml\n" + yaml.dump(yml, sort_keys=False) + "```",
            code="```python" + code + "```",
            # yml_diffs="```\n" + str(yml_diffs) + "```",
            py_code_errors=str(result["py_code_errors"]),
            automation_errors=str(result["automation_errors"]),
            results=str(result["result"]),
            page="```\n" + result["page"] + "```",
        )
        self.lm.inspect_history(n=1)
        return yaml.safe_load(parse_code_blocks(prediction.new_yml))


class YamlValidation(dspy.Module):
    def __init__(self, model="gpt-3.5-turbo", filepath="google_30.yaml"):
        super().__init__()
        self.lm = dspy.OpenAI(model=model, max_tokens=4096)
        self.code = ValidationCodeModule(lm=self.lm)
        # self.fix_code = FixCodeCodeModule(lm=self.lm)
        self.fix_yml = FixYMLModule(lm=self.lm)

        dspy.settings.configure(lm=self.lm)

        self.browser = BrowserCodeExecutor()
        self.browser.start()

        self.yml = yaml.safe_load(
            open(os.path.join(os.path.dirname(__file__), "yaml", filepath), "r")
        )
        self.yml_diffs = []
        print(yaml.dump(self.yml, sort_keys=False))

    def forward(self, fixed_yml=None, iteration=0) -> dspy.Prediction:
        max_iterations = 10

        if fixed_yml is None:
            fixed_yml = self.yml

        validation_code = self.code.forward(
            validation_yml=merge_validation_steps(fixed_yml)
        )
        validation_result = self.browser.execute_python(py_code=validation_code)
        print(validation_code)
        print(validation_result)

        while iteration < max_iterations and not validation_result.get("success"):
            print("Iteration: " + str(iteration))
            """
            fixed_code = self.fix_code.forward(
                code=validation_code, result=validation_result
            )
            fixed_code_result = self.browser.execute_python(py_code=fixed_code)
            """
            new_yml = self.fix_yml.forward(
                yml=self.yml,
                code=validation_code,
                # yml_diffs=self.yml_diffs,
                result=validation_result,
            )
            print(yaml.dump(new_yml, sort_keys=False))

            # Generate a diff
            current_yml_str = yaml.dump(fixed_yml, sort_keys=False)
            fixed_yml_str = yaml.dump(new_yml, sort_keys=False)
            diff = generate_diff(current_yml_str, fixed_yml_str)
            print(diff)

            self.yml_diffs.append(diff)

            iteration += 1

            return self.forward(fixed_yml=new_yml, iteration=iteration)

        print("SOMETHING WRONG")
        return validation_result


def generate_diff(original_yml: str, modified_yml: str) -> str:
    original_lines = original_yml.splitlines(keepends=True)
    modified_lines = modified_yml.splitlines(keepends=True)
    diff = difflib.unified_diff(
        original_lines, modified_lines, fromfile="orig.yml", tofile="mod.yml"
    )
    return "".join(diff)


def main():
    # Discover
    yaml_validation = YamlValidation(
        model="gpt-4-turbo-preview", filepath="google_30.yaml"
    )
    # self_discover = SelfDiscover(model="gpt-3.5-turbo-0125")

    "Write email at outlook.com to dasda@dasd.com about last news in AI"
    "Parse all ai projects managers in London at linkedin"

    result = yaml_validation.forward()
    print(result)


if __name__ == "__main__":
    main()
