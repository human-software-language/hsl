import argparse
from packages.logger import logger
from .server import server


def add_arguments(parser: argparse.ArgumentParser):
    parser.description = "HSL Language Server"

    parser.add_argument("--tcp", action="store_true", help="Use TCP server")
    parser.add_argument("--ws", action="store_true", help="Use WebSocket server")
    parser.add_argument("--host", default="127.0.0.1", help="Bind to this address")
    parser.add_argument("--port", type=int, default=2087, help="Bind to this port")


parser = argparse.ArgumentParser()
add_arguments(parser)
args = parser.parse_args()

logger.info("Starting HSL Language Server Protocol")
print("test")
if args.tcp:
    logger.info(f"Starting in TCP mode on {args.host}:{args.port}")
    server.start_tcp(args.host, args.port)
elif args.ws:
    logger.info(f"Starting in WebSocket mode on {args.host}:{args.port}")
    server.start_ws(args.host, args.port)
else:
    logger.info("Starting in STDIO mode")
    server.start_io()

logger.info("Server startup complete")
