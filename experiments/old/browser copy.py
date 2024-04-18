from playwright.sync_api import sync_playwright
import threading
import queue
import re
from contextlib import contextmanager


class BrowserCodeExecutor:
    def __init__(self):
        self.browser = None
        self.playwright = None
        self._playwright_started = False
        self.result_queue = queue.Queue()
        self._start_playwright()  # Start the browser at initialization

    def _start_playwright(self):
        if not self._playwright_started:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(headless=True)
            self._playwright_started = True

    def _threaded_execute_javascript(self, page_url, js_code):
        def run():
            page = None
            try:
                page = self.browser.new_page()
                page.goto(page_url)
                result = page.evaluate(js_code)
                self.result_queue.put(result)
            except Exception as e:
                self.result_queue.put(e)
            finally:
                if page is not None:
                    page.close()

        thread = threading.Thread(target=run)
        thread.start()
        thread.join()

    def execute_javascript(self, page_url, js_code):
        self._threaded_execute_javascript(page_url, js_code)
        return self.result_queue.get()

    def _threaded_execute_python(self, python_code):
        def run():

            try:
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
                    code_to_execute = (
                        adjusted_code + "\nresult = playwright_actions(page)"
                    )
                else:
                    return "Extracted code is empty."
                """

                exec_globals = {"browser": self.browser}
                exec(python_code, exec_globals)
                result = exec_globals.get(
                    "result", "Execution completed, no result returned."
                )
                self.result_queue.put(result)
            except Exception as e:
                self.result_queue.put(e)

        thread = threading.Thread(target=run)
        thread.start()
        thread.join()

    def execute_python(self, python_code):
        """Fixed: Removed the page_url argument"""
        self._threaded_execute_python(python_code)
        return self.result_queue.get()

    def close(self):
        if self._playwright_started:
            self.browser.close()
            self.playwright.stop()
            self._playwright_started = False
            self.browser = None
            self.playwright = None

    def __enter__(self):
        self._start_playwright()  # Ensure the browser is started here
        return self  # Provide the executor instance for usage within the with block

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()  # Clean up the resources
        if exc_type:
            print(f"An exception occurred: {exc_val}")

    @contextmanager
    def execution_context(self):
        try:
            yield self
        finally:
            self.close()


# Usage example
with BrowserCodeExecutor() as executor:
    result = executor.execute_javascript(
        "https://example.com", "return document.title;"
    )
    print(result)
    python_code = """
result = page.evaluate('document.title')
"""
    print(executor.execute_python(python_code))
