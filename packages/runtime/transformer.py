from lark import Transformer
import logging

# Setup logging
logger = logging.getLogger(__name__)


class HSLTransformer(Transformer):
    def start(self, items):
        return {"type": "program", "sections": items}

    def section(self, items):
        header = items[0]
        content = items[1:]
        return {"type": "section", "header": header, "content": content}

    def section_header(self, items):
        section_type = items[0].value
        description = items[1].value if len(items) > 1 else ""
        return {
            "type": "section_header",
            "section_type": section_type,
            "description": description,
        }

    def component(self, items):
        header = items[0]
        content = items[1:]
        return {"type": "component", "header": header, "content": content}

    def component_header(self, items):
        return {"type": "component_header", "name": items[0].value}

    def variable_definition(self, items):
        name = items[0].value
        var_type = items[1].value if len(items) > 1 else None
        description = items[2].value if len(items) > 2 else ""
        return {
            "type": "variable",
            "name": name,
            "var_type": var_type,
            "description": description,
        }

    def step(self, items):
        step_num = int(items[0].value)
        content = items[1].value
        return {"type": "step", "number": step_num, "content": content}

    def arbitrary_text(self, items):
        return {"type": "text", "content": items[0].value}
