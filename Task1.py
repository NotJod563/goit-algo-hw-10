import pulp

# Створюємо проблему лінійного програмування для максимізації
model = pulp.LpProblem("Maximization_of_Production", pulp.LpMaximize)

# Змінні: кількість вироблених одиниць Лимонаду та Фруктового соку
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Об'єктивна функція: максимізація кількості напоїв
model += lemonade + fruit_juice, "Total_Production"

# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"  # 100 од. Води
model += 1 * lemonade <= 50, "Sugar_Constraint"  # 50 од. Цукру
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"  # 30 од. Лимонного соку
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"  # 40 од. Фруктового пюре

# Розв'язуємо задачу
model.solve(pulp.PULP_CBC_CMD(msg=False))

# Виведення результатів
print(f"Статус: {pulp.LpStatus[model.status]}")
print(f"Кількість виробленого Лимонаду: {lemonade.varValue}")
print(f"Кількість виробленого Фруктового соку: {fruit_juice.varValue}")
print(f"Максимальна загальна кількість напоїв: {pulp.value(model.objective)}")


