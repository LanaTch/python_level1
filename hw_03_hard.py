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
    pass

def delete():
    pass

def print_my():
    pass

def calculate_my():
    pass

def main():
    print("==Меню==")
    print(" [1] - Добавить")
    print(" [2] - Удалить")
    print(" [3] - Распечатать")
    print(" [4] - Посчитать")
    print(" [5] - Выйти")

    аnswer = ''

    while answer != '5':
        answer = input('Ведите номер пункта меню: ')
            if len(answer)>1 or (ord('1') < ord(answer[0]) <ord('5')):
                print('Неправильный ввод данных. введите номер пункта меню от 1 до 5')
            elif answer == '1':
                append()
            elif answer == '2':
                delete()
            elif answer == '3':
                print_my()
            elif answer == '4':
                calculate_my()
            elif answer == '5':
                pass

if __name__ == "__main__":
    main()
