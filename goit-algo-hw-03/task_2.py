"""
Друге завдання

Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку 
з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. 
Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), 
яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.

Вона буде повертати випадковий набір чисел у межах заданих параметрів, 
причому всі випадкові числа в наборі повинні бути унікальні.

Вимоги до завдання:

Параметри функції:
min - мінімальне можливе число у наборі (не менше 1).
max - максимальне можливе число у наборі (не більше 1000).
quantity - кількість чисел, які потрібно вибрати (значення між min і max).
Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
Функція повертає список випадково вибраних, відсортованих чисел. 
Числа в наборі не повинні повторюватися. 
Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.

Рекомендації для виконання:

Переконайтеся, що вхідні параметри відповідають заданим обмеженням.
Використовуйте модуль random для генерації випадкових чисел.
Використовуйте множину або інший механізм для забезпечення унікальності чисел.
Пам'ятайте, що функція get_numbers_ticket повертає відсортований список унікальних чисел.

Критерії оцінювання:

Валідність вхідних даних: функція повинна перевіряти коректність параметрів.
Унікальність результату: усі числа у видачі повинні бути унікальними.
Відповідність вимогам: результат має бути у вигляді відсортованого списку.
Читабельність коду: код має бути чистим і добре документованим.


Приклад: Припустимо, вам потрібно вибрати 6 унікальних чисел для лотерейного квитка, 
де числа повинні бути у діапазоні від 1 до 49. Ви можете використати вашу функцію так:

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

Цей код викликає функцію get_numbers_ticket з параметрами min=1, max=49 та quantity=6. 
В результаті ви отримаєте список з 6 випадковими, унікальними та відсортованими числами, 
наприклад, [4, 15, 23, 28, 37, 45]. Кожен раз при виклику функції ви отримуватимете 
різний набір чисел.
"""

import random

def get_numbers_ticket(min: int, max: int, quantity: int) ->list:
    """
    Generate and return list of random unique sorted numbers.

    Args:
        min: range starts from this number.
        max: range finishes by this number.
        quantity: quantity of numbers to return(list length).

    Returns:
        the list with random sorted unique integers.

    Raises:
        if min > max, min < 0, max >= 1000, min < quantity > max or values has wrong type returns empty list.
    """
    if not isinstance(quantity, int) or not isinstance(min, int) or not isinstance(max, int):
        # raise TypeError("The quantity must be integer.")
        return []
    if min < 1 or max >= 1000 or min < quantity > max or min >= max or ((max - min) < quantity):
        # raise ValueError("Wrong range or quantity")
        return []

    result = []
    while len(result) < quantity:
        
        random_number = random.randint(min, max)
        if random_number not in result:
            result.append(random_number)
        
    return sorted(result)


# Tests
test1 = get_numbers_ticket(1, 49, 6)
print(f"{test1=}")

test2 = get_numbers_ticket(1, 36, 5)
print(f"{test2=}")

test3 = get_numbers_ticket(1, 49, 7.5)
print(f"{test3=}")

test4 = get_numbers_ticket("1", 49, 7)
print(f"{test4=}")

test5 = get_numbers_ticket(49, 1, 7)
print(f"{test5=}")

test6 = get_numbers_ticket(1, 5, 7)
print(f"{test6=}")

test7 = get_numbers_ticket(10, 14, 7)
print(f"{test7=}")