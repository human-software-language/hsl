from packages.lsp.command_registry import command


@command("custom/handleEcho")
def handle_echo(params):
    message = params[0] if params else "No message"
    return {"message": "Echo: " + message}
