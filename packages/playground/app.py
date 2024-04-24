import streamlit as st
from communication import register_message_handler

from chat_interface import chat_route
from hello_world import hello_world_route


def main():
    st.set_page_config(
        page_title="Playground",
        page_icon=None,
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items=None,
    )

    routes = {
        "home": home,
        "chat_interface": chat_route,
        "hello_world": hello_world_route,
    }

    if "current_route" not in st.session_state:
        st.session_state["current_route"] = "home"

    routes[st.session_state["current_route"]]()

    if st.button("Go to Home"):
        st.session_state["current_route"] = "home"
    if st.button("Go to Chat Interface"):
        st.session_state["current_route"] = "chat_interface"
    if st.button("Go to Hello World"):
        st.session_state["current_route"] = "hello_world"


def home():
    st.title("Welcome to the Playground")
    message_handlers = {
        "selection_change": lambda data: st.write("Selection changed in VSCode:", data),
        "custom_message": lambda data: st.write(
            "Custom message received from VSCode:", data
        ),
    }
    for message_type, handler in message_handlers.items():
        register_message_handler(message_type, handler)
    st.markdown("Navigate using the buttons to see different features.")


if __name__ == "__main__":
    main()
