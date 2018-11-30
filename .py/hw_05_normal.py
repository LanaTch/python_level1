# NORMAL

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое указанной папки
# 3. Удалить папку
# 4. Создать папку
# При выборе любых пунктов печатается статус "Успешно создано/удалено/перешел", "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os
import shutil

def print_menu(menu):
    for i, key in enumerate(menu, start=1):
        print(f"{i}. {key}")


def get_command(limit):
    command = int(input("Введите команду: "))
    if 1 <= command <= limit:
        return command


def go_to_dir():
    path = str(input('Введите путь к директории'))
    if os.path.exists(path):
        os.chdir(path)
        print("Успешно перешел")
    else:
        print('Перейти невозможно. Путь не существует')
    return 0

def view_of_dir_list():
    path = str(input('Введите путь к директории'))
    if os.path.exists(path):
        print(os.listdir(path))
    else:
        print('Путь не существует')
    return 0


def delete_dir():
    path = str(input('Введите путь к директории'))
    if os.path.exists(path):
        shutil.rmtree(path)
        print("Успешно удалена" if not (os.path.exists(path)) else print('Невозможно удалить'))
    else:
        print('Путь не существует')
    return 0


def make_dir():
    path = str(input('Введите путь к директории'))
    os.mkdir(path)
    print('Создана успешно')
    return 0

def finish():
    exit(0)


menu = {
    "Перейти в папку": go_to_dir,
    "Просмотреть содержимое указанной папки": view_of_dir_list,
    "Удалить папку": delete_dir,
    "Создать папку": make_dir,
    "Выйти": finish,
}


while True:
    print_menu(menu)
    command = get_command(len(menu))
    if command is not None:
        key = list(menu.keys())[command - 1]
        menu[key]()
    else:
        print("Неправильная команда!")