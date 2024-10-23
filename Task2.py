import numpy as np
import scipy.integrate as integrate

# Функція, яку будемо інтегрувати
def func(x):
    return np.sin(x)

# Метод Монте-Карло для обчислення інтегралу
def monte_carlo_integration(func, a, b, num_points=10000):
    x_random = np.random.uniform(a, b, num_points)
    func_values = func(x_random)
    integral = (b - a) * np.mean(func_values)
    return integral

# Використання функції quad з бібліотеки SciPy
def scipy_quad_integration(func, a, b):
    result, _ = integrate.quad(func, a, b)
    return result

# Інтервали інтегрування
a = 0
b = np.pi

# Обчислення за методом Монте-Карло
mc_result = monte_carlo_integration(func, a, b)
print(f"Результат за допомогою методу Монте-Карло: {mc_result}")

# Аналітичне або обчислене за допомогою SciPy значення
quad_result = scipy_quad_integration(func, a, b)
print(f"Результат за допомогою функції quad з SciPy: {quad_result}")

# Порівняння результатів
error = abs(mc_result - quad_result)
print(f"Різниця між результатами: {error}")
