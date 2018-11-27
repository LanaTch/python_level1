# HARD

# Задание-1
# Куб состоит из n^3 прозрачных и непрозрачных элементарных кубиков. Имеется ли хотя бы один просвет
# по каждому из трех измерений?
# Если это так, вывести координаты каждого просвета. Куб задается трехмерной матрицей из 0 и 1.

import random
import pprint

n = int(input('Input size matrix: '))
M = [[[random.randint(0, 1) for _ in range(n)] for _ in range(n)] for _ in range(n)]

pprint.pprint(M)

for i in range(n):
    for j in range(n):
        if M[i][j][0]==0:
            for k in range(n):
                if M[i][j][k]==0:
                    print("верхняя грань: (%d,%d,%d)\n" % (i,j,k))

for i in range(n):
    for k in range(n):
        if M[i][0][k]==0:
            for j in range(n):
                if M[i][j][k]==0:
                   print("левая грань: (%d,%d,%d)\n" %(i,j,k))

for j in range(n):
    for k in range(n):
        if M[0][j][k]==0:
            for i in range(n):
                if M[i][j][k]==0:
                    print("передняя грань: (%d,%d,%d)\n"%(i,j,k))


# Задание-2
# Дан pwd.txt с логинами и паролями. Найдите топ10 самых популярных паролей.
#
import operator
with open("pwd.txt", "r", encoding="utf-8" ) as f:
    s = f.read()

password_list = []
tmp_pass = ''
i = 0
pos_n = 0
while i<len(s):
    if s[i] == ';':
        pos_n = i+1
    if s[i] == '\n':
        tmp_pass = s[pos_n:i]
        if tmp_pass != '':
            password_list.append(tmp_pass)
    i+=1

password_dict = {}

for pw in password_list:
    password_dict[pw] = password_dict.get(pw)+1 if pw in password_dict.keys() else 1

p_list = list(password_dict.keys())

for p in p_list:
    if password_dict.get(p) == 1:
        password_dict.pop(p)

sorted_pd = sorted(password_dict.items(), key=operator.itemgetter(1))
top_10 = sorted_pd[(len(sorted_pd)-10):]

for i in top_10:
    print(str(i))


#
# Задание-3
# Пользователь вводит положительное целое число больше 1
# Нужно создать квадратную матрицу этого размера и по спирали заполнить её числами
# 5
#  1  2  3  4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

# 3
# 1 2 3
# 8 9 4
# 7 6 5

import pprint

n = int(input('Input size matrix: '))
M = [[0]*n for i in range(n)]
st,m=1,0

for j in range(n//2):
    #текущая верхняя строка
    for i in range(n-m):
        M[j][i+j] = st
        st+=1
    #текущий правый столбец
    for i in range(j+1, n-j):
        M[i][-j-1] = st
        st+=1
    #текущая нижняя строка
    for i in range(j+1, n-j):
        M[-j-1][-i-1]= st
        st+=1
    #текущий левый столбец
    for i in range(j+1, n-(j+1)):
        M[-i-1][j] = st
        st+=1
    m+=2
#центральный элемент
M[n//2][n//2]=n*n

pprint.pprint(M)