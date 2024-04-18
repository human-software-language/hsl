import yaml


def merge_validation_steps(data):
    # Helper function to recursively replace placeholders with actual values
    def replace_placeholders(item):
        if isinstance(item, str):
            if item.startswith("var."):
                return data["var"].get(item.split(".")[1], item)
            elif item.startswith("sel."):
                return data["sel"].get(item.split(".")[1], item)
            return item
        elif isinstance(item, list):
            return [replace_placeholders(x) for x in item]
        elif isinstance(item, dict):
            return {k: replace_placeholders(v) for k, v in item.items()}
        return item

    # Construct new validation steps with replaced values
    new_validation = {}
    for action_key, validation_rules in data.get("val", {}).items():
        action_parts = action_key.split(".")
        if len(action_parts) == 2 and action_parts[0] == "act":
            action_name = action_parts[1]
            if action_name in data["act"]:
                action = data["act"][action_name]
                new_action = {}
                for key, value in action.items():
                    new_action[key] = replace_placeholders(value)

                # Apply validation rules
                for rule_key, rule_value in validation_rules.items():
                    if rule_key in new_action:
                        # If rule exists in action, it's a direct merge
                        new_action[rule_key] = replace_placeholders(rule_value)
                    else:
                        # Apply rules that don't directly match action keys
                        new_action[rule_key] = replace_placeholders(rule_value)

                new_validation[action_name] = new_action

    return new_validation
