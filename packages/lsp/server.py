import os
from typing import Optional
from packages.logger import logger

from lark import Lark
from lsprotocol import types as lsp
from pygls.server import LanguageServer

from .command_registry import command_handlers


class HSLLanguageServer(LanguageServer):
    CMD_ECHO = "custom/handleEcho"

    def __init__(self, *args):
        super().__init__(*args)
        self.parser = Lark(
            open(os.path.join(os.path.dirname(__file__), "hsl_grammar.lark")).read(),
            start="start",
            parser="earley",
        )

    async def execute_command(self, params):
        command = params.get("command")
        data = params.get("arguments", [])

        if command in command_handlers:
            handler = command_handlers[command]
            result = handler(data)
            return result
        else:
            return {"error": "Unknown command"}

    async def validate(self, document):
        logger.info(f"Validating document: {document.uri}")
        # TODO: Implement validation logic
        pass

    def parse(self, document):
        try:
            logger.debug(f"Parsing document: {document.uri}")
            return self.parser.parse(document.source)
        except Exception as e:
            logger.error(f"Error parsing HSL: {e}", exc_info=True)


server = HSLLanguageServer("hsl-language-server", "0.1.0")


@server.feature(lsp.TEXT_DOCUMENT_DID_CHANGE)
async def did_change(ls: HSLLanguageServer, params: lsp.DidChangeTextDocumentParams):
    """Text document did change notification."""
    await ls.validate(ls.workspace.get_text_document(params.text_document.uri))


@server.feature(lsp.TEXT_DOCUMENT_DID_OPEN)
async def did_open(ls: HSLLanguageServer, params: lsp.DidOpenTextDocumentParams):
    """Text document did open notification."""
    ls.show_message("Text Document Did Open")
    await ls.validate(ls.workspace.get_text_document(params.text_document.uri))


@server.feature(lsp.TEXT_DOCUMENT_HOVER)
def hover(ls: HSLLanguageServer, params: lsp.HoverParams) -> Optional[lsp.Hover]:
    document = ls.workspace.get_text_document(params.text_document.uri)
    tree = ls.parse(document)
    if tree is None:
        return None
    # TODO: Implement hover logic based on tree
    return lsp.Hover(
        contents=lsp.MarkupContent(
            kind=lsp.MarkupKind.Markdown,
            value="Hover content",
        ),
        range=lsp.Range(
            start=lsp.Position(
                line=params.position.line, character=params.position.character
            ),
            end=lsp.Position(
                line=params.position.line, character=params.position.character
            ),
        ),
    )


@server.feature(lsp.WORKSPACE_EXECUTE_COMMAND)
async def execute_command(ls: HSLLanguageServer, params):
    result = await ls.execute_command(params)
    return result
