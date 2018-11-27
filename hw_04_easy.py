# EASY
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

def list_of_square(s:list):
    return [i**2 for i in s]

print(list_of_square([1,2,4,0]))

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

def list_of_same(l1:list, l2:list):
    return [i for i in l1 for j in l2 if i==j]

l1=["яблоко", "банан", "киви", "арбуз"]
l2=["яблоко", "абрикос", "мандарин", "арбуз"]
print(list_of_same(l1, l2))


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

l = [random.randint(-100,100) for i in range(20)]
print(l)
res = [i for i in l if i%3==0 and i>0 and i%4!=0]
print(res)
