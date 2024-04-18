import socket
from debugpy.common import messaging
from .debug_adapter import HSLDebugAdapter
from packages.logger import logger


def start_server(host: str, port: int):
    adapter = HSLDebugAdapter()

    def handle_event(event):
        adapter.handle_event(event)

    def handle_request(request):
        return adapter.handle_request(request)

    # Set up a TCP socket and listen for connections
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        logger.info(f"HSL Debug Adapter listening on {host}:{port}")

        # Accept connections continuously in a loop
        while True:
            conn, addr = server_socket.accept()
            with conn:
                print("Connected")
                logger.info(f"Connected by {addr}")

                # Create an instance of JsonIOStream from the accepted socket connection
                try:
                    json_io_stream = messaging.JsonIOStream.from_socket(conn)
                except Exception as e:
                    logger.error(f"Failed to create JsonIOStream: {e}")
                    continue

                while True:
                    try:
                        # Use the json_io_stream instance to read and write JSON messages
                        message = json_io_stream.read_json()
                        if isinstance(message, messaging.Event):
                            handle_event(message)
                        elif isinstance(message, messaging.Request):
                            response = handle_request(message)
                            json_io_stream.write_json(response.to_dict())
                    except messaging.NoMoreMessages:
                        # Handle disconnection or no more messages condition
                        logger.info("No more messages or client disconnected.")
                        break
                    except Exception as e:
                        # General error handling for unexpected issues
                        logger.error(f"Error during message processing: {e}")
                        break
