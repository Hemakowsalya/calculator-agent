def agent_loop():
    state = {
        "done": False,
        "stage": 0,
        "status": None
    }

    max_iters = 10

    for i in range(max_iters):
        state["stage"] += 1

        print(f"Iteration {state['stage']}")

        # Observe
        print("Observe")

        # Decide
        print("Decide")

        # Act
        print("Act")

        # Success condition
        if state["stage"] == 3:
            state["done"] = True
            state["status"] = "success"
            return state

    # Safety limit exceeded
    state["done"] = True
    state["status"] = "failure"
    return state


print(agent_loop())