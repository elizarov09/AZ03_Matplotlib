import pandas as pd
import matplotlib.pyplot as plt

# Загрузка CSV файла
df = pd.read_csv('sofas.csv')

# Фильтрация строк, содержащих слово "Диван" или "диван" в названии
filtered_df = df[df['Name'].str.contains('Диван|диван', case=False, na=False)].copy()

# Преобразование столбца 'Price' в числовой формат
filtered_df.loc[:, 'Price'] = pd.to_numeric(filtered_df['Price'], errors='coerce')

# Вычисление средней цены
average_price = filtered_df['Price'].mean()
print(f"Средняя цена на диваны: {average_price:.2f} руб.")

# Построение гистограммы цен
plt.figure(figsize=(20, 12))
plt.hist(filtered_df['Price'].dropna(), bins=60, alpha=0.2, color='blue', edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (руб)')
plt.ylabel('Количество')
plt.grid(True)
plt.show()
