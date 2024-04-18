import yaml


def find_message_in_yaml(data, target_messages):
    """
    Recursively search for target messages in the given data structure.

    :param data: The current data to search through.
    :param target_messages: The list of messages to find.
    :return: True if any target message is found, False otherwise.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "message" and value in target_messages:
                return True
            elif find_message_in_yaml(value, target_messages):
                return True
    elif isinstance(data, list):
        for item in data:
            if find_message_in_yaml(item, target_messages):
                return True
    return False


def message_exists_in_yaml(result, yaml_obj):
    """
    Check if any message from result['details'] exists in the YAML content at any level.

    :param result: Dictionary containing the result details.
    :param yaml_content: String containing the YAML content.
    :return: True if any message exists in YAML, False otherwise.
    """

    # Check if any message from result['details'] exists in the YAML data
    return find_message_in_yaml(yaml_obj, result["details"])


# Example usage
result = {
    "success": False,
    "error": "Errors were encountered during execution.",
    "details": [
        "Search input box is missing.",
        "Search submit button is missing.",
        "Timeout 30000ms exceeded.",
    ],
}

yaml_content = """
# Your YAML content here...
"""

# Call the function with your result and YAML content
exists = message_exists_in_yaml(result, yaml.safe_load(yaml_content))

print(exists)
