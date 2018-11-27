# NORMAL

# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random

with open("data_int.txt", "w", encoding="utf-8" ) as f:
    s = ''.join(str(random.randint(0,10)) for i in range(2500))
    f.write(s)

with open("data_int.txt", "r", encoding="utf-8" ) as f:
    st = f.read()

len_tmp = len_max = 1
buf = ''
res = a = st[0]

for i in range(1,len(st)):
    if st[i]==a:
        len_tmp+=1
        buf = len_tmp*a
    elif len_max<len_tmp:
        len_max = len_tmp
        res = buf
        buf = a
        len_tmp = 1
    else:
        buf = a
        len_tmp = 1
    a = st[i]
if len_tmp>len_max: res = buf
print(res)

# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится ровно
# один ноль на случайном месте, остальные элементы тоже рандомные.
# Пользователь вводит размер
import pprint
n = int(input('Input size matrix: '))

M = [[random.randint(1,100) for i in range(n)]for j in range(n)]
for i in range(n):
    M[i][random.randint(0,n-1)] = 0

pprint.pprint(M)