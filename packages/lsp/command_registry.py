import importlib.util
import pathlib

command_handlers = {}


def command(name):
    def decorator(fn):
        command_handlers[name] = fn
        return fn

    return decorator


def load_command_handlers():
    commands_path = pathlib.Path(__file__).parent / "commands"
    for file in commands_path.glob("*.py"):
        if file.name == "__init__.py":
            continue  # Skip the __init__.py file
        module_name = file.stem  # Get the module name without the .py extension
        spec = importlib.util.spec_from_file_location(module_name, file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)


# Call load_command_handlers at the end of this script to ensure it runs
load_command_handlers()
