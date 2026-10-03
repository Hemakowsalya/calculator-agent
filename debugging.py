def agent_loop(max_iters=10):
    i = 0
    log = []

    while i < max_iters:
        i += 1  # Fix: increment the counter

        log.append(f"Iteration {i}")

        print(f"Running iteration {i}")

        # Example success condition
        if i == 5:
            print("Success!")
            return {
                "status": "success",
                "iterations": i,
                "log": log
            }

    return {
        "status": "failure",
        "iterations": i,
        "log": log
    }


result = agent_loop()
print(result)