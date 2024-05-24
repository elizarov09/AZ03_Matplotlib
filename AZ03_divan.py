import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

# Путь к вашему драйверу ChromeDriver
chrome_driver_path = '/Users/olegelizarov/PycharmProjects/AZ03_Matplotlib/.venv/bin/chromedriver'  # Убедитесь, что указали правильный путь

# URL шаблон страницы, которую будем парсить
base_url = 'https://www.divan.ru/category/divany-i-kresla/page-{}'

# Настройка сервиса для веб-драйвера
service = Service(executable_path=chrome_driver_path)

# Настройка веб-драйвера
driver = webdriver.Chrome(service=service)

# Список для хранения данных о диванах
sofas = []

# Инициализация переменной для отслеживания страницы
page = 1

while True:
    # Формирование URL для текущей страницы
    url = base_url.format(page)
    driver.get(url)

    # Ждем загрузки страницы
    time.sleep(5)

    # Поиск всех блоков с информацией о диванах
    sofa_items = driver.find_elements(By.CSS_SELECTOR, 'div[itemprop="itemListElement"]')

    # Если не найдено ни одного элемента, значит страницы закончились
    if not sofa_items:
        print(f"Страницы закончились на странице {page}")
        break

    for item in sofa_items:
        try:
            # Получение названия дивана
            name = item.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text.strip()

            # Получение цены дивана
            price = item.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content').strip()

            # Добавление данных о диване в список
            sofas.append({'Name': name, 'Price': price})
        except Exception as e:
            print(f"Ошибка при обработке элемента: {e}")

    # Переход к следующей странице
    page += 1

# Закрытие веб-драйвера
driver.quit()

# Создание DataFrame с данными о диванах
df = pd.DataFrame(sofas)

# Сохранение данных в CSV файл
df.to_csv('sofas.csv', index=False, encoding='utf-8')
print("Данные успешно сохранены в sofas.csv")
