import numpy as np

F_plus = np.array([
    [250, 350, 150],
    [750, 200, 350],
    [255, 850, 250],
    [800, 550, 450]
])

P = np.array([0.1, 0.5, 0.4])

expected_values = F_plus @ P

lambda_values = [0.1, 0.3]
hurwicz_criteria = []

for lmbda in lambda_values:
    hurwicz_criteria.append([lmbda * np.min(F_plus[i]) + (1 - lmbda) * np.max(F_plus[i]) for i in range(len(F_plus))])

print("Очікувані значення для кожного рішення:", expected_values)

expected_values_2 = np.dot(expected_values, 0.5)
for idx, lmbda in enumerate(lambda_values):
    print(f"Критерій Гурвіца для λ = {lmbda}:", hurwicz_criteria[idx])

optimal_hurwicz_2 = np.dot(hurwicz_criteria[1], 0.5)


optimal_decision_expected = np.argmax(expected_values)
optimal_decision_hurwicz_1 = np.argmax(hurwicz_criteria[0])
optimal_decision_hurwicz_2 = np.argmin(expected_values_2 + optimal_hurwicz_2)

print("Оптимальне рішення за очікуваним значенням:", optimal_decision_expected + 1)
print("Оптимальне рішення за критерієм Гурвіца для λ = 0.1:", optimal_decision_hurwicz_1 + 1)
print("Оптимальне рішення за критерієм Гурвіца для λ = 0.3:", optimal_decision_hurwicz_2 + 1)
