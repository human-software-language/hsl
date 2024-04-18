# hsl_plugin.py
import os
from pylsp import hookimpl, hookspec
from pylsp.workspace import Document
from lark import Lark, UnexpectedCharacters, UnexpectedEOF

# Load the HSL grammar from a file located in the same directory as this plugin
grammar_path = os.path.join(os.path.dirname(__file__), "hsl_grammar.lark")
with open(grammar_path) as f:
    grammar = f.read()

# Initialize Lark parser with the HSL grammar
parser = Lark(grammar, start="start", parser="earley")


@hookimpl
def pylsp_document_diagnostics(document: Document):
    # Implement diagnostics using Lark to parse the HSL document
    diagnostics = []
    try:
        parser.parse(document.source)
    except (UnexpectedCharacters, UnexpectedEOF) as e:
        # Add diagnostic information based on the exception
        diagnostics.append(
            {
                "range": {
                    "start": {"line": e.line - 1, "character": e.column},
                    "end": {"line": e.line - 1, "character": e.column + 1},
                },
                "message": str(e),
                "severity": hookspec.DiagnosticSeverity.Error,
                "source": "hsl",
            }
        )
    return diagnostics
