import random
import matplotlib.pyplot as plt
import pandas as pd

theoretical_probs = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}


def monte_carlo_dice_simulation(trials=1000000):
    results = {i: 0 for i in range(2, 13)}

    for _ in range(trials):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        s = d1 + d2
        results[s] += 1

    probabilities = {k: v / trials for k, v in results.items()}
    return probabilities


trials = 2000000
simulated_probs = monte_carlo_dice_simulation(trials)

data = []
for s in range(2, 13):
    data.append(
        {
            "Sum": s,
            "Monte Carlo": f"{simulated_probs[s]*100:.2f}%",
            "Analytical": f"{theoretical_probs[s]*100:.2f}%",
            "Difference": f"{(simulated_probs[s]-theoretical_probs[s])*100:.2f}%",
        }
    )

df = pd.DataFrame(data)
print(df.to_string(index=False))

plt.figure(figsize=(8, 5))
plt.bar(
    simulated_probs.keys(),
    [p * 100 for p in simulated_probs.values()],
    alpha=0.6,
    label="Monte Carlo",
)
plt.plot(
    theoretical_probs.keys(),
    [p * 100 for p in theoretical_probs.values()],
    "ro-",
    label="Analytical",
)
plt.xlabel("Sum of two dice")
plt.ylabel("Probability (%)")
plt.title(f"Probabilities of sums when rolling two dice ({trials:,} of simulations)")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
