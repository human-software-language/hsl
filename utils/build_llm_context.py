import os
import pyperclip


def build_llm_context(paths):
    file_contents = "Files:\n"
    file_structure = ""
    total_files = 0
    total_lines = 0

    # List of directories and files to ignore
    ignore_list = [
        "node_modules",
        "venv",
        "__pycache__",
        ".git",
        ".DS_Store",
        "*.log",
        "*.tmp",
        "*.bak",
        "*.swp",
        "init",
        "conftest",
        "out",
        "markdown_preview",
        "crossnote",
        "test",
        "pylsp_hsl-plugin",
        "crossnote",
        "build",
        "tailwind-vscode.js",
        "tailwind.config.js",
        "logging",
        "logger",
        "api-reference",
        "databases",
        "instalation",
        "changelog",
    ]

    # Helper function to process a single file
    def process_file(file_path, base_path):
        nonlocal total_files, total_lines, file_structure, file_contents
        file_name = os.path.basename(file_path)
        _, extension = os.path.splitext(file_name)
        if extension in [
            ".sh",
            ".rst",
            ".py",
            ".js",
            ".jsx",
            ".ts",
            ".tsx",
            ".html",
            ".css",
            ".md",
            ".json",
            ".lark",
            ".toml",
        ] and not any(
            ignore.endswith(("*" + extension, "*.*")) for ignore in ignore_list
        ):
            total_files += 1
            relative_path = os.path.relpath(file_path, base_path)
            indent = "  " * (
                relative_path.count(os.sep)
            )  # Adjust indentation based on the relative path
            file_structure += f"{indent}- {file_name}\n"

            # Read the content of the file
            with open(file_path, "r") as f:
                content = f.read()
                lines = content.split("\n")
                total_lines += len(lines)
                file_contents += f"File: {relative_path}\n```\n{content}\n```\n\n"

    for path in paths:
        abs_path = os.path.normpath(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
        )
        if os.path.isdir(abs_path):
            # Traverse the folder structure and process files
            for root, dirs, files in os.walk(abs_path):
                # Remove ignored directories from dirs list
                dirs[:] = [
                    d
                    for d in dirs
                    if d not in ignore_list
                    and not any(ig in os.path.join(root, d) for ig in ignore_list)
                ]

                level = root.replace(abs_path, "").count(os.sep)
                indent = "  " * level  # Adjust indentation based on level
                file_structure += f"{indent}[{os.path.basename(root) if root != abs_path else os.path.basename(path)}]\n"

                for file in files:
                    file_path = os.path.join(root, file)
                    process_file(file_path, abs_path)
        elif os.path.isfile(abs_path):
            # Process the single file
            process_file(abs_path, os.path.dirname(abs_path))
            # Ensure the file's directory is included in the structure
            if abs_path.count(os.sep) > 0:
                file_structure += f"[{os.path.basename(os.path.dirname(abs_path))}]\n"

    return file_contents, file_structure, total_files, total_lines


if __name__ == "__main__":
    # Specify the list of relative paths
    relative_paths = [
        "../.streamlit",
        "../.vscode",
        "../hsl_exampels",
        "../utils",
        "../poetry.toml",
        # "../debugpy/src/debugpy/common",
        # "../debugpy/src/debugpy/launcher",
        # "../debugpy/src/debugpy/server",
        "../packages",
        # "../vscode",
        # "../md/streamlit-content/develop",
        # "../packages/dap",
        # "../md/pygls-docs-source",
        # "../pylsp-hsl-plugin",
        # "../debug-adapter-examples-main"
    ]

    file_contents, file_structure, total_files, total_lines = build_llm_context(
        relative_paths
    )
    context = "Structure:\n" + file_structure + "\n\n" + file_contents

    # Copy the context to the clipboard
    pyperclip.copy(context)

    # Print the structure and stats
    print("Structure:")
    print(file_structure)
    print(f"Total files: {total_files}")
    print(f"Total lines of code: {total_lines}")
    print("The context has been copied to the clipboard.")
