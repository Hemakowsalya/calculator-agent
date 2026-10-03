def agent_loop(max_iters=10):
    state = {
        "done": False,
        "stage": "start"
    }

    for i in range(max_iters):
        # Observe
        state["stage"] = "observe"

        # Decide
        state["stage"] = "decide"

        # Act
        state["stage"] = "act"

        # Success condition
        if i == 2:
            state["done"] = True
            state["stage"] = "success"
            return "success", state

    # Max iterations exceeded
    state["done"] = True
    state["stage"] = "failure"
    return "failure", state


result, state = agent_loop()
print(result)
print(state)