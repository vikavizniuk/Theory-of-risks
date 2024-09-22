from math import sqrt

L1 = 2000
L2 = [3000, 0.5, 1000]
L3 = [4000, 0.5, 0]

def risk (L):
    expected_gain = (L[0] + L[2]) * L[1]
    expected_utility = (L[1] * (0.01 * L[0] ** 2)) + (L[1] * (0.01 * L[2] ** 2))

    det_equivalent = sqrt(expected_utility / 0.01)

    x = expected_gain - det_equivalent

    return x, expected_utility

x1 = 2000
u1 = 0.01 * x1 ** 2
x2, u2 = risk(L2)
x3, u3 = risk(L3)

print("Премія за ризик роботи 1: ", x1)
print("Премія за ризик роботи 2: ", x2)
print("Премія за ризик роботи 3: ", x3)

print("\nСподівана корисність роботи 1: ", u1)
print("Сподівана корисність роботи 2: ", u2)
print("Сподівана корисність роботи 3: ", u3, "\n")


if u1 > u2 and u1 > u3:
    print("Вам доцільно обрати роботу 1")
elif u2 > u1 and u2 > u3:
    print("Вам доцільно обрати роботу 2")
else: 
    print("Вам доцільно обрати роботу 3")

