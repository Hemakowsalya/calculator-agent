def agent_loop(max_iters=10):
    for i in range(max_iters):
        step = i + 1

        print("Iteration", step)
        print("Observe")
        print("Decide")
        print("Act")

        if step == 5:
            return "success"

    return "failure"


result = agent_loop(10)
print("Result:", result)
