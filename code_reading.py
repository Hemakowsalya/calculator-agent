def agent_loop():
    log = []

    for i in range(2):
        step = i + 1

        log.append(f"Step {step}: Observe")
        log.append(f"Step {step}: Decide")
        log.append(f"Step {step}: Act")

    return log


result = agent_loop()

for item in result:
    print(item)