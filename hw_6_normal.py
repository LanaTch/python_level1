# EASY-NORMAL

# Задача-1:
#
# Создать класс треугольник и реализовать в нем конструктор, методы для площади, периметра и вывод на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника, если нет, то написать,
# что такой треугольник нельзя создать и сделать exit(1)
import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not(self.a+self.b>self.c and self.a+self.c>self.b and self.b+self.c>self.a):
            exit(1)
    #для расчёта периметра треугольника
    def CalcPerimeter(self):
        return self.a + self.b + self.c

    #для расчёта площадь треугольника
    def CalcArea(self):
        semiperimeter = Triangle.CalcPerimeter(self)/2
        return math.sqrt(semiperimeter*(semiperimeter-self.a)*(semiperimeter-self.b)*(semiperimeter-self.c))

    #рисование треугольника
    def Sides(self):
        return f"Длины сторон треугольника: A={self.a} см, B={self.b} см и C={self.c} см"

a = int(input('введите длины сторон треугольника А: '))
b = int(input('введите длины сторон треугольника B: '))
c = int(input('введите длины сторон треугольника C: '))
t = Triangle(a,b,c)
print(t.Sides())
print(f"Периметр треугольника: P={t.CalcPerimeter()} см")
print(f"Площадь треугольника S={t.CalcArea():.2f} см")