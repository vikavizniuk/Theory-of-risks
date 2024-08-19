
imov_rain = float(input("Введіть імовірність дощу: "))
imov_sun= 1 - imov_rain
cond_forest_rain = int(input("Введіть корисність в дощову погоду в ліс (від 1 до 10): "))
cond_forest_sun = int(input("Введіть корисність в сонячну погоду в лісі (від 1 до 10): "))
cond_home_rain = int(input("Введіть корисність в дощову погоду вдома (від 1 до 10): "))
cond_home_sun = int(input("Введіть корисність в сонячну погоду вдома (від 1 до 10): "))

result_forest = cond_forest_rain * imov_rain + cond_forest_sun * imov_sun
result_home = cond_home_rain * imov_rain + cond_home_sun * imov_sun

print("Корисність піти в ліс:", result_forest, "Корисність залишитись вдома:", float('{:.3f}'.format(result_home)))

if result_forest > result_home:
    print("Вам рекомендовано піти в ліс")
else:
    print("Вам рекомендовано залишитись вдома")

