# Easy
#
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2. банан
# 3. киви
# 4. арбуз
#
# Подсказка: воспользоваться методом .format()

list_fruit = ["яблоко", "банан", "киви", "арбуз"]
for i in range(len(list_fruit)):
    print("{}{}{}".format(str(i+1),'. ',list_fruit[i]))
#     print(i+1, list_fruit[i], sep='. ') альтернативный вариант

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

A = [1,2,3,4]
B = [4]

for i in range(len(B)):
    j = 0
    while j<len(A):
        if A[j] == B[i]:
            A.pop(j)
        j+=1
print(A)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

A = [1,2,3,4,5,6,7,8]
B = []
for i in range(len(A)):
    B.append(A[i]/4 if A[i]%2==0 else A[i]*2)
print(A)
print(B)

