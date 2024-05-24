import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0  # Среднее значение
std_dev = 1  # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.75, color='blue', edgecolor='black')
plt.title('Гистограмма для данных, распределенных по нормальному закону')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.show()
