# Observe -> Decide -> Act Agent Loop


def observe():
    return input("Observe: Enter current situation: ")


def decide(observation):
    if "rain" in observation.lower():
        return "Carry an umbrella"
    if "hot" in observation.lower():
        return "Drink water"
    return "Continue normally"


def act(decision):
    print("Act:", decision)
    return decision


def agent_loop(max_iters=3):
    for iteration in range(1, max_iters + 1):
        print(f"\n--- Iteration {iteration} ---")
        observation = observe()
        decision = decide(observation)
        print("Decide:", decision)
        act(decision)
    return "Agent loop completed"


if __name__ == "__main__":
    print(agent_loop())