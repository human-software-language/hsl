import argparse
from .server import start_server

parser = argparse.ArgumentParser(description="Start the debug adapter protocol server")
# Add the arguments
parser.add_argument(
    "--host",
    type=str,
    required=True,
    help="The host IP to listen on (e.g., localhost)",
)
parser.add_argument(
    "--port",
    type=int,
    required=True,
    help="The port number to listen on (e.g., 5678)",
)

args = parser.parse_args()

start_server(args.host, args.port)
