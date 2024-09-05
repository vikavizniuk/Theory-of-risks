from math import *

first_good_profit = 10
first_good_probability = 0.6
first_bad_profit = 0.5
first_bad_probability = 0.4
second_good_profit = 10
second_good_probability = 0.4
second_bad_profit = 1
second_bad_probability = 0.6

m_first = (first_good_profit * first_good_probability) + (first_bad_profit * first_bad_probability)
m_second = (second_good_profit * second_good_probability) + (second_bad_profit * second_bad_probability)

print("Значення сподіваної чистої теперішньої вартості 1 коорпорації:", m_first, "\nЗначення сподіваної чистої теперішньої вартості 2 коорпорації:", m_second)

v_first = ((first_good_profit - m_first)**2 * first_good_probability) + ((first_bad_profit - m_first)**2 * first_bad_probability)
v_second= ((second_good_profit - m_second)**2 * second_good_probability) + ((second_bad_profit - m_second)**2 * second_bad_probability)

omega_first = sqrt(v_first)
omega_second = sqrt(v_second)

cv_first = omega_first / m_first
cv_second = omega_second / m_second

print("\nКоефіцієнт варіації 1 коорпорації:", cv_first, "\nКоефіцієнт варіації 2 коорпорації:", cv_second)

if cv_first > cv_second:
    print("Найменш ризикованою є коорпорація 2")
elif cv_first < cv_second:
    print("Найменш ризикованою є коорпорація 1")
else: 
    print("Ризик коорпорацій однаковий")