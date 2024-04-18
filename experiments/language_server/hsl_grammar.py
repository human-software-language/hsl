from lark import Lark
from pathlib import Path

# Define the HSL grammar
hsl_grammar = r"""
    %import common.WS
    %ignore WS

    start: program

    program: section+

    section: section_header section_content

    section_header: "#" (PROGRAM | FRONTEND | BACKEND | BROWSER | MOBILE | CUSTOM) ":" SECTION_DESCRIPTION?

    section_content: (component | arbitrary_text)+

    component: component_header component_content

    component_header: "##" COMPONENT_NAME

    component_content: (arbitrary_text | variable_definition | step_sequence | component_section)*

    component_section: input_section | output_section | secrets_section | context_section | examples_section | notes_section

    input_section: "### Input"
    output_section: 
    "### Output"
    secrets_section: "### Secrets"
    context_section: "### Context"
    steps_section: "### Steps"
    examples_section: "### Examples"
    notes_section: "### Notes"

    arbitrary_text: TEXT
    variable_definition: "- `" VARIABLE_NAME (":" VARIABLE_TYPE)? "`" DESCRIPTION?
    step_sequence: step+
    step: NUMBER "." STEP_CONTENT

    SECTION_DESCRIPTION: /.+/
    COMPONENT_NAME: /[A-Za-z0-9 ]+/
    VARIABLE_NAME: /[a-zA-Z0-9_]+/
    VARIABLE_TYPE: /[a-zA-Z0-9_]+/
    DESCRIPTION: /.+/
    STEP_CONTENT: /.+/
    NUMBER: /[0-9]+/
    TEXT: /[^#\n]+/

    PROGRAM: "Program"
    FRONTEND: "Frontend"
    BACKEND: "Backend"
    BROWSER: "Browser"
    MOBILE: "Mobile"
    CUSTOM: /[A-Za-z0-9]+/



"""


def main():

    # Get the directory of the current script
    script_dir = Path(__file__).parent.parent.absolute()

    # Correctly navigate to the sibling directory 'hls/examples' from 'lark'
    markdown_file_path = script_dir.parent / "hsl" / "examples" / "program.md"

    # Check if the file exists
    if not markdown_file_path.is_file():
        print(f"File not found: {markdown_file_path}")
        return

    # If the file is found, proceed with reading and parsing
    markdown_content = markdown_file_path.read_text()

    # Create an instance of the Lark parser with the HSL grammar
    parser = Lark(hsl_grammar)

    try:
        # Parse the markdown content
        ast = parser.parse(markdown_content)
        print("Parsing successful!")
        print(ast.pretty())
    except Exception as e:
        print("Parsing failed:")
        print(e)


if __name__ == "__main__":
    main()
