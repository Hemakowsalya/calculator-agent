def agent_loop(max_iters=10):
    state = {
        "done": False,
        "stage": "start"
    }

    log = []

    for i in range(max_iters):
        # Observe
        state["stage"] = "observe"
        log.append(f"Iteration {i + 1}: Observe")

        # Decide
        state["stage"] = "decide"
        log.append(f"Iteration {i + 1}: Decide")

        # Act
        state["stage"] = "act"
        log.append(f"Iteration {i + 1}: Act")

        # Success condition
        if i == 2:
            state["done"] = True
            state["stage"] = "success"
            log.append(f"Iteration {i + 1}: Success")
            return state, log

    # Max iterations exceeded
    state["done"] = True
    state["stage"] = "failure"
    log.append("Maximum iterations reached: Failure")

    return state, log


state, log = agent_loop()

print("Final State:", state)
print("Full Log:")

for entry in log:
    print(entry)