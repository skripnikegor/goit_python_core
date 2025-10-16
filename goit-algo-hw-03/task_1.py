"""
Перше завдання

Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою 
і поточною датою.

Вимоги до завдання:

Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' 
(наприклад, '2020-10-09').
Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. 
Якщо задана дата пізніша за поточну, результат має бути від'ємним.
У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
Для роботи з датами слід використовувати модуль datetime Python.

Рекомендації для виконання:

Імпортуйте модуль datetime.
Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
Отримайте поточну дату, використовуючи datetime.today().
Розрахуйте різницю між поточною датою та заданою датою.
Поверніть різницю у днях як ціле число.

Критерії оцінювання:

Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами.
Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.
Читабельність коду: код повинен бути чистим і добре документованим.

Приклад:

Якщо сьогодні 5 травня 2021 року, виклик get_days_from_today("2021-10-09") 
повинен повернути 157, оскільки 9 жовтня 2021 року є на 157 днів пізніше від 
5 травня 2021 року.
"""

import datetime

def get_days_from_today(date: str) -> int:
    """
    Calculate days between input date and today.

    Args:
        date (str): date in format 'YYYY-MM-DD'.

    Returns:
        quantity of days between today and entered date, 0 if the date is incorrect.

    Raises:
        if date has wrong format or type return 0.
    """
    try:
        converted_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        return (datetime.datetime.now().date() - converted_date).days
    except ValueError, TypeError:
        return 0

    

res = get_days_from_today("2021-10-09")
res2 = get_days_from_today("2026-10-09")
res3 = get_days_from_today("asjdhasd")
res4 = get_days_from_today(12312)
print(res, res2, res3, res4)