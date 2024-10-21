import numpy as np
econom = [[6.0, 6.2, 5.5, 5.4, 5.0], 
          [7.5, 7.1, 7.0, 6.8, 6.0],
          [7.4, 7.5, 8.0, 7.7, 5.0],
          [7.0, 5.8, 6.0, 6.2, 6.4]]

p = [0.1, 0.3, 0.4, 0.15, 0.05]

def Bayesa(e, p):
    res = []
    for i in range(len(e)):
        sum = 0 
        for j in range(len(e[i])):
            sum += e[i][j] * p[j]
        res.append(sum)  
    return res

def min_expected_deviation(e, p):
    max_per_state = np.max(e, axis=0)
    res = []
    for i in range(len(e)):
        total_semivariance = 0
        for j in range(len(e[i])):

            if e[i][j] < max_per_state[j]:
                deviation = max_per_state[j] - e[i][j]

                total_semivariance += deviation * p[j]
        res.append(total_semivariance)
    min_semivariance = min(res)
    best_choice_index = res.index(min_semivariance)
    
    return res, min_semivariance, best_choice_index

res, min_deviation, best_choice_index = min_expected_deviation(econom, p)

print("Сподівані відхилення для кожного варіанту рішення:", res)
print("Мінімальне сподіване відхилення:", min_deviation)
print("Найкращий варіант рішення: x", best_choice_index + 1)


res = Bayesa(econom, p)
print("\nРезультати за Байєса:", res)

max_res = max(res)
index_max = res.index(max_res)
print("Оптимальний розв'язок за Байєса: x", index_max + 1, ":", max_res)

