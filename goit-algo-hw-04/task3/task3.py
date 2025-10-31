"""
Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. 
Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.

Вимоги до завдання:

Створіть віртуальне оточення Python для ізоляції залежностей проєкту.
Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
Використання бібліотеки colorama для реалізації кольорового виведення.
Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.

Рекомендації для виконання:

Спочатку встановіть бібліотеку colorama. Для цього створіть та активуйте віртуальне оточення Python, а потім встановіть пакет за допомогою pip.
Використовуйте модуль sys для отримання шляху до директорії як аргументу командного рядка.
Для роботи з файловою системою використовуйте модуль pathlib.
Забезпечте належне форматування виводу, використовуючи функції colorama.

Критерії оцінювання:

Створення та використання віртуального оточення.
Правильність отримання та обробки шляху до директорії.
Точність виведення структури директорії.
Коректне застосування кольорового виведення за допомогою colorama.
Якість коду, включаючи читабельність, структурування та коментарі.

Приклад використання:

Якщо виконати скрипт та передати йому абсолютний шлях до директорії як параметр.

python hw03.py /шлях/до/вашої/директорії

Це призведе до виведення в терміналі списку всіх піддиректорій та файлів у вказаній директорії з використанням різних кольорів для піддиректорій та файлів, що полегшить візуальне сприйняття файлової структури.

Для директорії зі наступною структурою

📦picture
 ┣ 📂Logo
 ┃ ┣ 📜IBM+Logo.png
 ┃ ┣ 📜ibm.svg
 ┃ ┗ 📜logo-tm.png
 ┣ 📜bot-icon.png
 ┗ 📜mongodb.jpg

скрипт повинен вивести схожу структуру:

"""
import sys
from pathlib import Path
from colorama import Fore

def print_directory_structure(filepath: Path, separator: str=""):
    """
    Print files from directory by path. If filepath is dir - run itself recursive.

    Args:
        path - path to the file.
        separator - symbol before file name

    """
    for item in filepath.iterdir():
        if item.is_dir():
            print(f"{separator}{Fore.BLUE}{item.name}/")
            print_directory_structure(item, separator + "   ")
        else:
            print(f"{separator}{Fore.GREEN}{item.name}")


def get_files_from_directory():
    """"
    Checks if directory exist and it is directory. Prints file structure by directory. 

    Args:
        path - get path to folder as script start parameter.

    Raises:
        if path/data wrong returns an empty array.
    """
    if len(sys.argv) < 2:
        print(f"{Fore.RED} Error. Please add path to the directory.")
        print(f"{Fore.YELLOW} Example: python task3.py C:/Users/Admin/Pictures")
        sys.exit(1)

    directory = Path(sys.argv[1])

    if not directory.exists():
        print(f"{Fore.RED}Error '{directory}' not exist.")
        sys.exit(1)

    if not directory.is_dir():
        print(f"{Fore.RED}Error: '{directory}' is not directory.")
        sys.exit(1)

    # Print root directory
    print(f"{Fore.CYAN}{directory.name}/")
    print_directory_structure(directory, separator="    ")

if __name__ == "__main__":
    get_files_from_directory()
