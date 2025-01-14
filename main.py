from datetime import datetime
import random
import re

def get_days_from_today(date):
    try:
        now_day = datetime.today().date() # Робимо поточну дату
        date_object = datetime.strptime(date, "%Y-%m-%d").date() # Перетворюємо дату яка надходить в обьект date
        delta = now_day - date_object # Обчислюємо кількість днів від введеної дати до поточної
    except ValueError:
        return "Неверный формат даты. Ожидаемый формат: YYYY-MM-DD"
    return delta.days


print(get_days_from_today('2025-01-10')) # тест для превірки роботи ф-ції



def get_numbers_ticket(min, max, quantity):
    try:
        # Проверка корректности входных данных
        if not isinstance(min, int) or not isinstance(max, int) or not isinstance(quantity, int):
            return []

        # Проверка диапазона значений
        if min < 1 or max > 1000 or min > max:
            return []

        # Проверка, что возможно выбрать указанное количество уникальных чисел
        if quantity > (max - min + 1):
            return []

        # Генерация уникальных случайных чисел
        random_numbers = random.sample(range(min, max + 1), quantity)

        # Сортировка результата
        return sorted(random_numbers)
    except Exception:
        return []

print(get_numbers_ticket(1,1000,33))

# додаткове завдання

def normalize_phone(phone_number):

    # Убираем пробелы по краям
    phone_number = phone_number.strip()

    # Оставляем только цифры и '+' в начале
    normalized_number = re.sub(r"[^\d+]", "", phone_number)

    # Проверяем, есть ли международный код
    if normalized_number.startswith("+"):
        # Если номер начинается с '+', проверяем, содержит ли он код '38'
        if not normalized_number.startswith("+38"):
            normalized_number = "+38" + normalized_number[1:]
    elif normalized_number.startswith("380"):
        # Если номер начинается с '380', добавляем '+'
        normalized_number = "+" + normalized_number
    else:
        # Если номер не содержит кода, добавляем '+38'
        normalized_number = "+38" + normalized_number

    return normalized_number

#Пример использования
phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]
normalized_numbers = [normalize_phone(phone) for phone in phone_numbers]
for normalized in normalized_numbers:
    print(f"Нормализованный: {normalized}")