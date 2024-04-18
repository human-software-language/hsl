from playwright.sync_api import sync_playwright
import threading
import queue


class BrowserCodeExecutor:
    def __init__(self):
        self.playwright = None
        self.browser = None
        # Use a thread to initialize Playwright to avoid blocking the asyncio loop
        self.init_thread = threading.Thread(target=self._init_playwright)
        self.init_thread.start()
        self.init_thread.join()  # Wait for Playwright to be initialized

    def _init_playwright(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)

    def _execute_in_thread(self, func, *args):
        result_queue = queue.Queue()

        def target():
            try:
                result = func(*args)
                result_queue.put(result)
            except Exception as e:
                result_queue.put(e)

        thread = threading.Thread(target=target)
        thread.start()
        thread.join()
        result = result_queue.get()
        if isinstance(result, Exception):
            raise result
        return result

    def execute_javascript(self, page_url, js_code):
        def run():
            page = self.browser.new_page()
            page.goto(page_url)
            result = page.evaluate(js_code)
            page.close()
            return result

        return self._execute_in_thread(run)

    def execute_python(self, py_code):
        def run():
            exec_globals = {"browser": self.browser}
            exec(py_code, exec_globals)
            return exec_globals.get(
                "result", "Execution completed, no result returned."
            )

        return self._execute_in_thread(run)

    def close(self):
        if self.playwright:
            self.playwright.stop()
            self.browser.close()

    def __enter__(self):
        # Ensure Playwright is initialized
        if not self.playwright:
            self._init_playwright()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


def main():
    # Usage example
    with BrowserCodeExecutor() as executor:
        result = executor.execute_javascript(
            "https://example.com", "(() => {return document.title})()"
        )
        print(result)
        # Note: The execute_python method's intended functionality needs to be clarified.
        # python_code example below assumes direct interaction with the browser, which may not align with Playwright's capabilities.
        python_code = """
# Example Python code that interacts with the browser needs clarification.
result = browser
"""
        print(executor.execute_python(python_code))


if __name__ == "__main__":
    main()
