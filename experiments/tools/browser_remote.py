import importlib.util
import os
import signal
from playwright.sync_api import sync_playwright


class BrowserCodeExecutor:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None
        self.code_dir = "gen_code"
        self.websocket_url = os.environ.get("CHROME_REMOTE_DEBUGGING_URL")
        if not self.websocket_url:
            raise ValueError(
                "The CHROME_REMOTE_DEBUGGING_URL environment variable is not set."
            )

        os.makedirs(self.code_dir, exist_ok=True)
        self._setup_signal_handlers()

    def _setup_signal_handlers(self):
        for sig in (signal.SIGINT, signal.SIGTERM):
            signal.signal(sig, self._signal_handler)

    def _signal_handler(self, signum, frame):
        print(f"Signal {signum} received, closing resources...")
        self.close()

    def start(self):
        self.playwright = sync_playwright().start()
        # Connect to the remote Chrome instance instead of launching a new one
        self.browser = self.playwright.chromium.connect_over_cdp(self.websocket_url)
        self.page = self.browser.new_page()
        self._setup_event_listeners()
        print("Connected to remote browser, new page created")

    def _setup_event_listeners(self):
        # Execute read_page after every page load
        self.page.on("load", self.read_page)

        # Handle new pages by attaching the same load event listener
        self.browser.contexts[0].on("page", self.read_page)

    def close(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

    def execute_javascript(self, js_code):
        if not self.browser:
            return "Error: Browser not started."
        result = self.page.evaluate(js_code)
        return result

    def read_page(self):
        js_code_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "utils", "page_structure.js"
        )
        with open(js_code_path, "r") as js_file:
            js_code = js_file.read()
        result = self.execute_javascript(js_code)
        return result

    def _get_next_filename(self):
        existing_files = [f for f in os.listdir(self.code_dir) if f.endswith(".py")]
        highest_num = max(
            (int(f.split("_")[0]) for f in existing_files if f.split("_")[0].isdigit()),
            default=0,
        )
        return f"{self.code_dir}/{highest_num + 1}_dynamic_code.py"

    def _save_and_load_dynamic_code(self, py_code):
        filename = self._get_next_filename()
        with open(filename, "w") as file:
            file.write(py_code)
        module_name = os.path.basename(filename).replace(".py", "")
        spec = importlib.util.spec_from_file_location(module_name, filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def execute_python(self, py_code, execute_args=None):
        if not self.browser:
            return "Error: Browser not started."
        if not self.page:
            return "Error: Page not started."
        dynamic_module = self._save_and_load_dynamic_code(py_code)
        if hasattr(dynamic_module, "execute"):
            execute_args = execute_args or {}
            result = dynamic_module.execute(self.page, **execute_args)
            if not result.get("py_code_errors") and not result.get("automation_errors"):
                result["success"] = True
            else:
                result["success"] = False
                result["page"] = self.read_page()
            return result

        return {"success": False, "error": "No execute function found in dynamic code."}


def main(websocket_url):
    executor = BrowserCodeExecutor()
    executor.start()
    try:
        result = executor.execute_javascript("(() => {return document.title})()")
        print(result)
    finally:
        executor.close()


if __name__ == "__main__":
    main()
