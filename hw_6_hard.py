# HARD

# Задание-1:
#
# Написать класс, который будет удобно использовать для работы с матрицами

# Чем логичнее код тем лучше


class Matrix:
    """умеет выводить размер матрицы, указанную строку, сумму со скаляром или другой матрицей, умножение на матрицу,
        транспонирование матрицы должны быть квадратными"""
    def __init__(self, list_of_lists:list):
        self.list2D = list_of_lists.copy()
        self.dim_C = len(list_of_lists)
        self.dim_R = len(list_of_lists[0])

    def size(self):
        return len(self.list2D), len(self.list2D[0])

    def getitem(self, index):
        return self.list2D[index]

    def add(self, other):
        result = []
        numbers = []
        for i in range(len(self.list2D)):
            for j in range(len(self.list2D[0])):
                summa = other.list2D[i][j] + self.list2D[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.list2D):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

    def mul(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[other * x for x in y] for y in self.list2D])
        else:
            s_dim_C = range(self.dim_C)
            s_dim_R = range(self.dim_R)
            o_dim_C = range(other.dim_C)
            result = []
            for i in s_dim_R:
                res = []
                for j in o_dim_C:
                    el, m = 0, 0
                    for k in s_dim_C:
                        m = self.list2D[i][k] * other.list2D[k][j]
                        el += m
                    res.append(el)
                result.append(res)
            return Matrix(result)

    def transposition(self):
        return Matrix([list(x) for x in zip(*(self.list2D))])
    def str(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.list2D])


m = Matrix([[1,0],[1,0]])
m2 = Matrix([[1,1],[1,1]])

print(m.str())
# print('===============')
# print(m2.str())
# print('=====сумма:====')
# print(m.add(m2).str())
# print('==произведение:==')
# print(m.mul(m2).str())
print(m.transposition().str())