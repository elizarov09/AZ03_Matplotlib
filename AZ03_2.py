import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 1000  # Количество образцов
data1 = np.random.rand(num_samples)  # Первый набор случайных данных
data2 = np.random.rand(num_samples)  # Второй набор случайных данных

# Создание диаграммы рассеяния
plt.figure(figsize=(10, 6))
plt.scatter(data1, data2, alpha=0.5, color='blue', edgecolors='black')
plt.title('Диаграмма рассеяния для двух наборов случайных данных')
plt.xlabel('Первый набор данных')
plt.ylabel('Второй набор данных')
plt.grid(True)
plt.show()

