def agent_loop(max_iters=10):
    for i in range(max_iters):
        step = i + 1

        print(f"Iteration {step}")
        print("Observe")
        print("Decide")
        print("Act")

        # Example success condition
        if step == 5:
            return "success"

    # Safety limit exceeded
    return "failure"


result = agent_loop(10)
print("Result:", result)