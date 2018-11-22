# EASY

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    pos_point = 0
    s = str(number)

    while s[pos_point] != '.':
        pos_point +=1

    return float(s[:(pos_point+1+ndigits)]) if int(s[pos_point+ndigits+1])<=5 else float(s[:(pos_point+1+ndigits)])+10**(-ndigits)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if ticket_number//10**5 != 0:
        s = str(ticket_number)
        sn = [int(item) for item in s]
        return 'Билет счастливый!' if sum(sn[0:3])==sum(sn[3:6]) else 'Билет не счастливый'
    else:
        return 'Ошибка! Номер билета должен быть шестизначным'

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))