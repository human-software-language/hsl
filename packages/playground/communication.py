import streamlit as st
import streamlit.components.v1 as components
import json
import uuid

# JavaScript code template that facilitates communication
_js_template = """
<script>
(function() {
    const vscode = window.parent; // Reference to the VSCode API

    // Listen for messages from the VSCode extension
    window.addEventListener("message", (event) => {
        const handlers = window.messageHandlers || {};

        if (event.data.hasOwnProperty("selections")) {
            // Handle selection change event
            const handler = handlers["selection_change"];
            if (handler) {
                handler(event.data);
            }
        } else if (event.data.hasOwnProperty("requestId")) {
            // Handle response to custom message
            const { requestId, result } = event.data;
            const handler = handlers[requestId];
            if (handler) {
                handler(result);
                delete window.messageHandlers[requestId];
            }
        } else {
            // Handle custom message from VSCode extension
            const { data } = event.data;
            const handler = handlers["custom_message"];
            if (handler) {
                handler(data);
            }
        }
    });

    // Send a message to the VSCode extension
    window.sendMessageToVSCode = (data, callback) => {
        const requestId = uuid.v4();
        const message = { data, requestId };
        vscode.postMessage(message);

        if (callback) {
            window.messageHandlers[requestId] = callback;
        }
    };

    // Register a message handler
    window.registerMessageHandler = (type, handler) => {
        window.messageHandlers = window.messageHandlers || {};
        window.messageHandlers[type] = handler;
    };

    // Unregister a message handler
    window.unregisterMessageHandler = (type) => {
        window.messageHandlers = window.messageHandlers || {};
        delete window.messageHandlers[type];
    };
})();
</script>
"""


def send_message(data):
    # Generate a unique request ID
    request_id = str(uuid.uuid4())

    # Create a JavaScript function to handle the response
    response_handler = f"""
    function handleResponse_{request_id}(result) {{
        window.streamlitMessageResponses["{request_id}"] = result;
    }}
    """

    # Send the message to the VSCode extension
    components.html(
        _js_template
        + f"""
        <script>
        window.streamlitMessageResponses = window.streamlitMessageResponses || {{}};
        sendMessageToVSCode({json.dumps(data)}, handleResponse_{request_id});
        </script>
        """
        + response_handler,
        height=0,
        key=request_id,
    )

    # Wait for the response
    while request_id not in components.get_state("streamlitMessageResponses", {}):
        pass

    # Get the response and remove it from the state
    response = components.get_state("streamlitMessageResponses", {})[request_id]
    components.set_state(
        "streamlitMessageResponses",
        {
            k: v
            for k, v in components.get_state("streamlitMessageResponses", {}).items()
            if k != request_id
        },
    )

    return response


@st.cache_data(hash_funcs={components.html: lambda _: None})
def register_message_handler(type, handler):
    components.html(
        _js_template
        + f"""
        <script>
        registerMessageHandler("{type}", (data) => {{
            window.streamlitMessageHandlers["{type}"](data);
        }});
        </script>
        """,
        height=0,
        key=type,
    )
    components.set_state(f"streamlitMessageHandler_{type}", handler)


@st.cache_data(hash_funcs={components.html: lambda _: None})
def unregister_message_handler(type):
    components.html(
        _js_template
        + f"""
        <script>
        unregisterMessageHandler("{type}");
        </script>
        """,
        height=0,
        key=str(uuid.uuid4()),
    )
    components.set_state(f"streamlitMessageHandler_{type}", None)
