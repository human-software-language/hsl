# HSL Development Environment

> Caution: Work in Progress. This represents our initial experiments in developing HSL technology.

The HSL Development Environment is a comprehensive toolkit for developing and debugging programs written in the Human Software Language (HSL). It provides a set of integrated tools and components that facilitate the development, testing, and execution of HSL programs.

## Project Structure

The project is organized into the following directories and files:

- `.streamlit/`: Configuration files for the Streamlit application.
- `.vscode/`: Visual Studio Code configuration files, including tasks, launch configurations, and settings.
- `utils/`: Utility for creating context for LLM from repository.
- `packages/`: Main packages of the HSL Development Environment.
  - `logger.py`: Logging configuration and setup.
  - `dap/`: Debug Adapter Protocol (DAP) implementation.
  - `common/`: Common utilities and functions.
  - `transpile/`: HSL transpilation logic.
  - `lsp/`: Language Server Protocol (LSP) implementation.
  - `extension/`: VSCode extension for HSL.
  - `playground/`: HSL Playground application.
  - `runtime/`: HSL runtime implementation.

## Getting Started

### Prerequisites

Before setting up the HSL Development Environment, ensure that you have the following prerequisites installed:

- Python 3.7 or higher
- Node.js 12.0 or higher
- Visual Studio Code (latest version recommended)

### Installation

Clone the repository:

```
git clone https://github.com/your-username/hsl-dev-env.git
```

Navigate to the project directory:

```
cd hsl-dev-env
```

Install the required Python dependencies:

```
poetry install
```

Install the required Node.js dependencies:

```
cd packages/extension
pnpm install
```

Open the project in Visual Studio Code and code :)

## Usage

The HSL Development Environment provides several launch configurations in the `.vscode/launch.json` file for running different components of the project.

### Build context for LLM

To build the context for the Language Model (LLM):

1. Open the `hsl-dev-env` workspace in Visual Studio Code.
2. Go to the "Run and Debug" view.
3. Select the "Build context for LLM" configuration from the dropdown.
4. Press the "Start Debugging" button (green play button) to launch the script.

### DAP Server

To run the Debug Adapter Protocol (DAP) server:

1. Open the `hsl-dev-env` workspace in Visual Studio Code.
2. Go to the "Run and Debug" view.
3. Select the "DAP Server" configuration from the dropdown.
4. Press the "Start Debugging" button (green play button) to launch the DAP server.

### LSP Server

To run the Language Server Protocol (LSP) server:

1. Open the `hsl-dev-env` workspace in Visual Studio Code.
2. Go to the "Run and Debug" view.
3. Select the "LSP Server" configuration from the dropdown.
4. Press the "Start Debugging" button (green play button) to launch the LSP server.

### Playground

To run the HSL Playground application:

1. Open the `hsl-dev-env` workspace in Visual Studio Code.
2. Go to the "Run and Debug" view.
3. Select the "Playground" configuration from the dropdown.
4. Press the "Start Debugging" button (green play button) to launch the Playground application.

### Extension

To run the VSCode extension:

1. Open the `hsl-dev-env` workspace in Visual Studio Code.
2. Go to the "Run and Debug" view.
3. Select the "Extension" configuration from the dropdown.
4. Press the "Start Debugging" button (green play button) to launch the extension in debug mode.

### Full Project Debug

To debug the entire HSL Development Environment:

1. Open the `hsl-dev-env` workspace in Visual Studio Code.
2. Go to the "Run and Debug" view.
3. Select the "Full Project Debug" configuration from the dropdown.
4. Press the "Start Debugging" button (green play button) to launch the debugging session.

## Language Server Protocol (LSP)

The HSL Development Environment includes an implementation of the Language Server Protocol (LSP) for HSL. The LSP server provides features such as syntax highlighting, code completion, and diagnostics.

### Features

- Syntax highlighting for HSL code.
- Code completion suggestions based on the HSL language grammar.
- Error highlighting and diagnostic messages.
- Hover information for HSL code elements.

### Commands

The LSP server supports the following commands:

- `custom/handleEcho`: Echoes back the provided message.

### Handlers

The LSP server provides handlers for various LSP events and requests, including:

- `textDocument/didChange`: Handles text document changes and validates the document.
- `textDocument/didOpen`: Handles text document opening and validates the document.
- `textDocument/hover`: Provides hover information for HSL code elements.
- `workspace/executeCommand`: Executes a custom command.

## Debug Adapter Protocol (DAP)

The HSL Development Environment includes an implementation of the Debug Adapter Protocol (DAP) for HSL. The DAP server enables debugging of HSL programs.

### Features

- Launching and debugging HSL programs.
- Setting breakpoints and stepping through code.
- Inspecting variables and program state.
- Handling runtime errors and exceptions.

### Request Handling

The DAP server handles various DAP requests, including:

- `initialize`: Initializes the debug adapter and sets up the debugging session.
- `launch`: Launches an HSL program for debugging.
- `setBreakpoints`: Sets breakpoints in the HSL program.
- `configurationDone`: Indicates that the debugging configuration is complete.
- `disconnect`: Disconnects the debug adapter and terminates the debugging session.

### Event Handling

The DAP server handles DAP events, such as:

- `output`: Handles output events and sends them to the debug console.

## Playground

The HSL Playground is a Streamlit application that provides an interactive environment for testing and exploring HSL programs.

### Communication with VSCode Extension

The Playground communicates with the VSCode extension using a custom communication protocol. It allows the exchange of messages and data between the Playground and the extension.

### Chat Interface

The Playground includes a chat interface that allows users to interact with an AI assistant powered by OpenAI. Users can ask questions and receive responses from the AI assistant.

### Hello World Example

The Playground provides a simple "Hello, World!" example to demonstrate the basic functionality of HSL programs.

## VSCode Extension

The HSL Development Environment includes a VSCode extension that provides a seamless development experience for HSL programs.

### Commands

The extension supports the following commands:

- `hsl.renderHSL`: Renders an HSL playground in a webview panel.

### Debugger

The extension integrates with the HSL debugger, allowing users to debug HSL programs directly from within VSCode.

### Language Support

The extension provides language support for HSL, including syntax highlighting, code completion, and error highlighting.

### Webview Integration

The extension integrates with the HSL Playground using webviews, allowing users to interact with the Playground directly from within VSCode.

## Runtime

The HSL Development Environment includes a runtime component that executes HSL programs.

### Initialization

The runtime initializes the execution environment and sets up the necessary components.

### Parsing

The runtime parses the HSL program and generates an Abstract Syntax Tree (AST) using the Lark parsing library.

### Execution

The runtime executes the parsed HSL program, traversing the AST and executing the corresponding actions.

### Breakpoints

The runtime supports setting and handling breakpoints during program execution, allowing for debugging and stepping through the code.

## Contributing

Contributions to the HSL Development Environment are welcome! If you find any issues or have suggestions for improvements, please open an issue on the GitHub repository.

To contribute code changes:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure that the code passes all tests.
4. Submit a pull request describing your changes.

Please adhere to the coding conventions and style guidelines used in the project.
