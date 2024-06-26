"""
# Chatbot

A way to create a chatbot using OpenAI's GPT-4 API, utilizing their new API, and the streaming feature.
"""

import os
from typing import List

from openai import OpenAI
from typing_extensions import TypedDict

import solara
import solara.lab


class VsCodeState(TypedDict):
    file_path: str
    cursor_location: tuple
    line_text: str


class MessageDict(TypedDict):
    role: str
    content: str


if os.getenv("OPENAI_API_KEY") is None and "OPENAI_API_KEY" not in os.environ:
    openai = None
else:
    openai = OpenAI()
    openai.api_key = os.getenv("OPENAI_API_KEY")  # type: ignore


messages: solara.Reactive[List[MessageDict]] = solara.reactive([])
a = solara.reactive("test")

vscode_state = solara.reactive(
    {
        "file_path": "/path/to/your/file.py",
        "cursor_location": (10, 5),  # line 10, column 5
        "line_text": "import os",
    }
)


def no_api_key_message():
    messages.value = [
        {
            "role": "assistant",
            "content": "No OpenAI API key found. Please set your OpenAI API key in the environment variable `OPENAI_API_KEY`.",
        },
    ]


def add_chunk_to_ai_message(chunk: str):
    messages.value = [
        *messages.value[:-1],
        {
            "role": "assistant",
            "content": messages.value[-1]["content"] + chunk,
        },
    ]


@solara.component
def Page():
    user_message_count = len([m for m in messages.value if m["role"] == "user"])

    def send(message):
        messages.value = [
            *messages.value,
            {"role": "user", "content": message},
        ]

    def call_openai():
        if user_message_count == 0:
            return
        if openai is None:
            no_api_key_message()
            return
        response = openai.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=messages.value,  # type: ignore
            stream=True,
        )
        a.value = "1231231231"
        messages.value = [*messages.value, {"role": "assistant", "content": ""}]
        for chunk in response:
            if chunk.choices[0].finish_reason == "stop":  # type: ignore
                return
            add_chunk_to_ai_message(chunk.choices[0].delta.content)  # type: ignore

    task = solara.lab.use_task(call_openai, dependencies=[user_message_count])  # type: ignore

    with solara.Column(
        style={"width": "700px", "height": "50vh"},
    ):
        solara.Markdown(f"### a\n- a: {a.value}\n")
        print(a.value)
        solara.Markdown(
            f"### VS Code State\n- File Path: {vscode_state.value['file_path']}\n- Cursor Location: {str(vscode_state.value['cursor_location'])}\n- Line Text: {vscode_state.value['line_text']}"
        )

        with solara.lab.ChatBox():
            for item in messages.value:
                with solara.lab.ChatMessage(
                    user=item["role"] == "user",
                    avatar=False,
                    name="ChatGPT" if item["role"] == "assistant" else "User",
                    color=(
                        "rgba(0,0,0, 0.06)"
                        if item["role"] == "assistant"
                        else "#ff991f"
                    ),
                    avatar_background_color=(
                        "primary" if item["role"] == "assistant" else None
                    ),
                    border_radius="20px",
                ):
                    solara.Markdown(item["content"])
        if task.pending:
            solara.Text(
                "I'm thinking...", style={"font-size": "1rem", "padding-left": "20px"}
            )
        solara.lab.ChatInput(send_callback=send, disabled=task.pending)
