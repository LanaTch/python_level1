#NORMAL

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib = [1,1]
    for i in range(2,m):
        fib.append(fib[i-2]+fib[i-1])
    return fib[n-1:m]

print(fibonacci(1,10))
print(fibonacci(4,20))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    N=len(origin_list)
    sort_list = origin_list.copy()
    for bypass in range(1,N):
        for k in range(0,N-bypass):
            if sort_list[k]>sort_list[k+1]:
                sort_list[k],sort_list[k+1]=sort_list[k+1],sort_list[k]
    return sort_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
