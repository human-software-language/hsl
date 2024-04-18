import logging
from lark import Lark
from .transformer import HSLTransformer

# Setup logging
logger = logging.getLogger(__name__)


class HSLRuntime:
    def __init__(self, debug_adapter, file_path=None):
        self.debug_adapter = debug_adapter
        self.file_path = file_path
        self.parser = Lark(
            open("hsl_grammar.lark").read(), parser="earley", lexer="standard"
        )
        self.transformer = HSLTransformer()
        self.ast = None
        self.program_state = {}
        self.breakpoints = {}

    def initialize(self, arguments):
        self.file_path = arguments.get("program")
        logger.info(f"Initializing runtime for program: {self.file_path}")

    def launch(self):
        logger.info("Launching HSL program")
        if self.file_path:
            self.parse()
            self.execute()

    def parse(self):
        with open(self.file_path, "r") as file:
            content = file.read()
        self.ast = self.transformer.transform(self.parser.parse(content))

    def execute(self):
        program = self.ast
        for section in program["sections"]:
            self.debug_adapter.send_event(
                "output",
                {
                    "category": "console",
                    "output": f"Executing section: {section['header']['section_type']}",
                },
            )
            self.execute_section(section)

    def execute_section(self, section):
        for item in section["content"]:
            if item["type"] == "component":
                self.execute_component(item)
            elif item["type"] == "text":
                self.debug_adapter.send_event(
                    "output",
                    {
                        "category": "console",
                        "output": f"Arbitrary Text: {item['content']}",
                    },
                )

    def execute_component(self, component):
        for item in component["content"]:
            if item["type"] == "variable":
                self.program_state[item["name"]] = self.resolve_variable(item["name"])
            elif item["type"] == "step":
                self.execute_step(item)

    def execute_step(self, step):
        line = step["number"]
        if self.breakpoints.get(line):
            self.debug_adapter.send_event(
                "stopped", {"reason": "breakpoint", "threadId": 1}
            )
        self.debug_adapter.send_event(
            "output",
            {
                "category": "console",
                "output": f"Executing Step {step['number']}: {step['content']}",
            },
        )

    def resolve_variable(self, var_name):
        # Logic to resolve variable value, possibly considering current program state
        return self.program_state.get(var_name, None)

    def set_breakpoints(self, path, breakpoints):
        self.breakpoints = {bp["line"] for bp in breakpoints}
        logger.info(f"Set breakpoints at: {self.breakpoints}")

    def disconnect(self, terminate_debuggee):
        logger.info("Disconnecting runtime")
        if terminate_debuggee:
            # Termination logic for the running program if needed
            logger.info("Terminating debuggee program")
