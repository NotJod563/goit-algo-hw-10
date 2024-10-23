import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції для інтегрування
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Метод Монте-Карло для обчислення інтегралу
def monte_carlo_integration(f, a, b, num_points):
    x_random = np.random.uniform(a, b, num_points)
    y_random = f(x_random)
    integral_value = (b - a) * np.mean(y_random)
    return integral_value

# Кількість точок для методу Монте-Карло
num_points = 10000

# Обчислення інтегралу за допомогою методу Монте-Карло
mc_result = monte_carlo_integration(f, a, b, num_points)

# Обчислення інтегралу за допомогою SciPy (функція quad)
quad_result, quad_error = spi.quad(f, a, b)

# Порівняння результатів
print(f"Результат за допомогою методу Монте-Карло: {mc_result}")
print(f"Результат за допомогою функції quad з SciPy: {quad_result}")
print(f"Різниця між результатами: {abs(mc_result - quad_result)}")

# Створення графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою (інтегральна площа)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Інтегрування f(x) = x^2 від {a} до {b}')

plt.grid()
plt.show()
