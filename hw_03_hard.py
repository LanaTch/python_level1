# HARD

        #Задание-1

#Написать консольное меню вида:

#1. Добавить
#2. Удалить
#3. Распечатать
#4. Посчитать
#5. Выйти

#Надо чтобы
#а) Можно было удобно менять порядок меню и\или добавлять\удалять пункты меню
#б) Каждое действие (добавить, удалить и тд) должно быть функцией
#в) У пользователя надо спросить номер команды
#г) Программа не должна завершаться пока не введется команда Выйти
#д) Проверять на ввод ошибочных данных, там где они могут появиться

def append():
    print('добавил')

def delete():
    print('удалил')

def print_my():
    print('напечатал')

def calculate_my():
    print('вычислил')

def exit_my():
    print('выход')

point_menu = [['Добавить', append],
    ['Удалить', delete],
    ['Распечатать', print_my],
    ['Вычислить', calculate_my],
    ['Выйти', exit_my]
]

print("==Меню==")
for i in range(len(point_menu)):
    print(f"{i+1}. ", point_menu[i][0])

answer = ''

while answer != str(len(point_menu)):
    answer = input('Ведите номер пункта меню: ')
    if answer=='0' or len(answer) > 1 or answer.isalpha():
        print('Неправильный ввод данных. номер пункта меню от 1 до', len(point_menu))
    else:
        for i in range(len(point_menu)):
            if answer == str(i+1):
                point_menu[i][1]()