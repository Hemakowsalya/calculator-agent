def rule_based_agent(temperature):
    if temperature > 100:
        return "cool"
    return "idle"


if __name__ == "__main__":
    temperatures = [80, 100, 101, 120]

    for temp in temperatures:
        action = rule_based_agent(temp)
        print(f"Temperature: {temp}")
        print(f"Agent action: {action}")
        print("-" * 30)