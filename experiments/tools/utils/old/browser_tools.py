#  .py
import re
import os
from langchain.tools import tool
from .browser import browser as cbrowser


script_dir = os.path.dirname(os.path.abspath(__file__))
js_file_path = os.path.join(script_dir, "utils", "page_structure.js")


class BrowserTools:
    @tool("Execute Playwright code")
    def execute_code(code):
        """
        Execute the given Playwright source code within the browser context and return the result.
        The code should be a valid Python string formatted for Playwright operations.

        :param code: A string containing Playwright source code.
        :return: The result of the executed code or error message.
        """

        # Extract the code block
        extracted_code_match = re.search(
            r"```(?:python\n|\n)([\s\S]+?)\n```", code, re.DOTALL
        )
        if not extracted_code_match:
            return "No valid code block found."

        extracted_code = extracted_code_match.group(1).strip("\n")

        # Remove common leading whitespace
        lines = extracted_code.split("\n")
        if lines:
            first_line = lines[0]
            leading_whitespace = len(first_line) - len(first_line.lstrip())
            adjusted_lines = [line[leading_whitespace:] for line in lines]
            adjusted_code = "\n".join(adjusted_lines).strip()
            code_to_execute = adjusted_code + "\nresult = playwright_actions(page)"
        else:
            return "Extracted code is empty."

        # Ensure that the browser tool is initialized and has a page loaded
        if not cbrowser.page:
            return "No page is currently loaded in the browser."

        # Execute the code
        try:
            page = cbrowser.page
            exec_globals = {"page": page}
            exec(code_to_execute, exec_globals)
            return exec_globals.get(
                "result", "Execution completed, no result returned."
            )
        except Exception as e:
            return f"Error occurred during code execution: {str(e)}"

    @tool("Get simple html")
    def read_website():
        """
        Fetches structured token-efficient content of a web page

        :return: Structured HTML content with xpath as a string.
        """
        # Ensure that the browser tool is initialized and has a page loaded
        if not cbrowser.page:
            return "No page is currently loaded in the browser."

        # Load JavaScript code from a file
        try:
            with open(js_file_path, "r") as file:
                js_code = file.read()
        except FileNotFoundError:
            return "JavaScript file not found."

        # Execute the JavaScript code in the browser context
        try:
            result = (
                " Elements are identified by their XPath, with attributes including text, href, placeholders, alt text, and values\n"
                + cbrowser.page.evaluate(js_code)
            )

            return result
        except Exception as e:
            return f"Error occurred during code execution: {str(e)}"
