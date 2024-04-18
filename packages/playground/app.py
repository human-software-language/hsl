import atexit
import streamlit as st
from streamlit_router import StreamlitRouter

from communication import register_message_handler, unregister_message_handler

st.set_page_config(
    page_title="Playground",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None,
)

# Add custom CSS to make the sidebar sticky to the right side and center col1
st.html(
    """
    <style>
    .stApp {
        display: flex;
        justify-content: center;
    }
    .sidebar .sidebar-content {
        position: fixed;
        right: 0;
    }
    #MainMenu {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    [data-testid="StyledLinkIconContainer"] {visibility: hidden;}
    a {visibility: hidden;}
    h3 > div > a {
        display: none;
    }
    h4 > div > a {
        display: none;
    }
    h5 > div > a {
        display: none;
    }
    h6 > div > a {
        display: none;
    }
    </style>
    """,
)


router = StreamlitRouter()


@st.cache_data
def get_message_handlers():
    return {
        "selection_change": None,
        "custom_message": None,
    }


@router.register(path="/", methods=["GET"])
def home():
    st.title("Welcome to the Playground")

    message_handlers = get_message_handlers()

    # Register message handlers if not already registered
    if message_handlers["selection_change"] is None:

        def handle_selection_change(data):
            st.write("Selection changed in VSCode:")
            st.write(data)

        message_handlers["selection_change"] = handle_selection_change
        register_message_handler("selection_change", handle_selection_change)

    if message_handlers["custom_message"] is None:

        def handle_custom_message(data):
            st.write("Custom message received from VSCode:")
            st.write(data)

        message_handlers["custom_message"] = handle_custom_message
        register_message_handler("custom_message", handle_custom_message)

    if st.button("Go to Chat Interface"):
        router.redirect(*router.build("chat_interface"))
    if st.button("Go to Hello World"):
        router.redirect(*router.build("hello_world"))
    st.markdown("Navigate using the buttons to see different features.")


@router.map(path="/chat", endpoint="chat_interface", methods=["GET"])
def chat_interface_route():
    from chat_interface import chat_route

    chat_route()


@router.map(path="/hello", endpoint="hello_world", methods=["GET"])
def hello_world_route():
    from hello_world import hello_world_route

    hello_world_route()


def main():
    router.serve()


if __name__ == "__main__":
    main()
