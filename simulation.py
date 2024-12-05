# Nate LaForme
# Group 10
# def simulation

# Simulation
def simulation(t, e=10):
    sum_explore_happiness = 0
    sum_exploit_happiness = 0
    sum_e_greedy_happiness = 0

    for _ in range(t):
        sum_explore_happiness += exploreOnly()
        sum_exploit_happiness += exploitOnly()
        
        # Call eGreedy
        e_greedy_value = eGreedy(e)
        if not e_greedy_value:  # Ensure default if None or 0
            e_greedy_value = e
        sum_e_greedy_happiness += e_greedy_value

    # Calculate averages
    avg_explore_happiness = sum_explore_happiness / t
    avg_exploit_happiness = sum_exploit_happiness / t
    avg_e_greedy_happiness = sum_e_greedy_happiness / t

    # Expected values
    expected_happiness_explore = cafe_means[0]
    expected_happiness_exploit = cafe_means[2]
    expected_happiness_e_greedy = (cafe_means[1] + cafe_means[2]) / 2

    # Calculate regrets
    expected_regret_explore = optH - expected_happiness_explore
    expected_regret_exploit = optH - expected_happiness_exploit
    expected_regret_e_greedy = optH - expected_happiness_e_greedy

    simulated_regret_explore = optH - avg_explore_happiness
    simulated_regret_exploit = optH - avg_exploit_happiness
    simulated_regret_e_greedy = optH - avg_e_greedy_happiness

    # Print results
    print(f"Optimum Happiness: {optH:.2f}\n")

    print("Explore Only:")
    print(f"  Expected Happiness: {expected_happiness_explore:.2f}")
    print(f"  Expected Regret: {expected_regret_explore:.2f}")
    print(f"  Simulated Happiness: {avg_explore_happiness:.2f}")
    print(f"  Simulated Regret: {simulated_regret_explore:.2f}\n")

    print("Exploit Only:")
    print(f"  Expected Happiness: {expected_happiness_exploit:.2f}")
    print(f"  Expected Regret: {expected_regret_exploit:.2f}")
    print(f"  Simulated Happiness: {avg_exploit_happiness:.2f}")
    print(f"  Simulated Regret: {simulated_regret_exploit:.2f}\n")

    print("eGreedy:")
    print(f"  Expected Happiness: {expected_happiness_e_greedy:.2f}")
    print(f"  Expected Regret: {expected_regret_e_greedy:.2f}")
    print(f"  Simulated Happiness: {avg_e_greedy_happiness:.2f}")
    print(f"  Simulated Regret: {simulated_regret_e_greedy:.2f}\n")

# Run the simulation
t = 300
simulation(t, e=10)