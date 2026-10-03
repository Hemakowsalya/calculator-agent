def agent_loop(action):
    valid_actions = ["search", "calculate", "finish"]

    # Check for invalid action
    if action not in valid_actions:
        return {
            "status": "error",
            "message": "Invalid action",
            "action": action
        }

    # Handle valid actions
    if action == "search":
        return {
            "status": "success",
            "message": "Search action executed"
        }

    elif action == "calculate":
        return {
            "status": "success",
            "message": "Calculate action executed"
        }

    elif action == "finish":
        return {
            "status": "success",
            "message": "Agent finished"
        }


# Example
result = agent_loop("invalid_action")
print(result)