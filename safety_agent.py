def agent_loop(max_iters=10):
    for i in range(max_iters):
        observation = observe()
        decision = decide(observation)
        if decision == "success":
            act(decision)
            return "success"
    return "failure"