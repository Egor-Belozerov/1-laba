from bs4 import BeautifulSoup  # импортируем библиотеку BeautifulSoup
import requests  # импортируем библиотеку requests
import re  # импортируем библиотеку re для работы с регулярными выражениями


def parse():
    url = 'https://www.eldorado.ru/c/smartfony/'  # URL с айфонами на Эльдорадо
    page = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})  # отправляем GET-запрос
    print("Статус код:", page.status_code)  # проверяем статус ответа
    soup = BeautifulSoup(page.text, "html.parser")  # инициализируем парсер BeautifulSoup

    # Ищем блоки с ценами айфонов
    blocks = soup.find_all('span', class_='EV MV')  # замените на актуальный класс для цен

    prices = []
    for block in blocks:
        price_text = block.get_text()  # извлекаем текст цены
        price = re.sub(r'\D', '', price_text)  # убираем всё, кроме цифр
        if price.isdigit():  # если остались только цифры
            prices.append(int(price))  # добавляем цену в список

    if prices:
        print(f"Минимальная цена: {min(prices)}")
        print(f"Максимальная цена: {max(prices)}")
        print(f"Средняя цена: {sum(prices) / len(prices):.2f}")
    else:
        print("Цены не найдены.")


parse()
