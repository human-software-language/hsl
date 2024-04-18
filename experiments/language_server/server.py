import os
import sys
from pylsp.__main__ import main
from pylsp.config.config import Config
from pylsp.workspace import Workspace
from pylsp.server import LanguageServer

# Ensure the directory containing your plugin is in the Python path
plugin_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(plugin_dir)


# Define a custom LanguageServer class to override the default configuration
class CustomLanguageServer(LanguageServer):
    def __init__(self, rx, tx):
        super().__init__(rx, tx)
        # Override the configuration to include your plugin directory
        self.config = Config(
            root_uri="", init_opts={}, process_id=os.getpid(), capabilities={}
        )
        self.workspace = Workspace(self, root_uri="", workspace_folders=[])
        self.config.plugin_dirs.append(plugin_dir)
        self.config.update({"plugins": {"hsl_lsp_plugin": {}}}, source="settings")


# Override the main function of pylsp to use the custom language server
if __name__ == "__main__":
    sys.argv.extend(["--tcp", "--port", "2087"])  # Example: run server on TCP port 2087
    main(language_server_class=CustomLanguageServer)
