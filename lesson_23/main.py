# class Person:  # объявление класса
#     def __init__(self, imya, vozrast):  # метод инициализации
#         self.age = vozrast  # Установка значений атрибутов
#         self.name = imya
#
#     def __str__(self):
#         return "strrr"
#
# leha = Person("Лёха", 1)
# print(leha.age)
# print(leha.name)
# print(leha)

# class Kefteme():
#     def __getitem__(self, item):
#         print("12345. Я тавлю тебе", item)
#
# obj = Kefteme()
# obj[2]

# задача 1
# class Chuvachok:
#     def __init__(self, vozrast, imya, familiya):
#         self.vozrast = vozrast
#         self.imya = imya
#         self.familiya = familiya
#     def __str__(self):
#         return (f"Я {self.imya} {self.familiya}, и мне {self.vozrast}")
#     def greet(self):
#         return (f"ауауауаа. Я {self.imya} {self.familiya}, и мне {self.vozrast}")
#
# sf = Chuvachok(1, "andrey", "ivanov")
# print(sf.vozrast)
# print(sf.imya)
# print(sf.familiya)
# print(sf.greet())

# задача 2
# import random
#
# class Chuvachok:
#     def __init__(self, vozrast, imya, familiya, grades):
#         self.vozrast = vozrast
#         self.imya = imya
#         self.familiya = familiya
#         self.grades = grades
#         self.sr = sum(grades) / len(grades)
#     def __str__(self):
#         return (f"Я {self.imya} {self.familiya}, и мне {self.vozrast}")
#     def greet(self):
#         return (f"ауауауаа. Я {self.imya} {self.familiya}, и мне {self.vozrast}")
# n = [random.randint(2,5) for i in range(2, 10)]
# anna = Chuvachok(123, "аня", "жесткая", [random.randint(2, 5) for i in range(2, 10)])
# vana = Chuvachok(123, "ванек", "лютый", [random.randint(2, 5) for i in range(2, 10)])
# sana = Chuvachok(123, "санек", "мегакрутой", [random.randint(2, 5) for i in range(2, 10)])
# dana = Chuvachok(123, "данек", "крутой", [random.randint(2, 5) for i in range(2, 10)])
# mana = Chuvachok(123, "мана", "хорош", [random.randint(2, 5) for i in range(2, 10)])
# students = [anna, mana, sana, dana, vana]
# d = {}
# for j in students:
#     d[j.imya] = j.sr
# sorted_tuples = reversed(sorted(d.items(), key=lambda item: item[1]))
# sorted_dict = {k: v for k, v in sorted_tuples}
# print(d)
# print(sorted_dict)

# задача 3-4
class Popoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x}, {self.y}"

x = 1

y = 1
class Rectalnoe:
    def __init__(self):
        self.xyz1 = gg
        self.xyz2 = ggwp
    def ploshad(self):
        a = self.xyz2.x - self.xyz1.x
        b = self.xyz2.y - self.xyz1.y
        return a * b
    def perimetr(self):
        a = self.xyz2.x - self.xyz1.x
        b = self.xyz2.y - self.xyz1.y
        return a + b
    def haspoint(self, kok):
        if (self.xyz1.x <= kok.x <= self.xyz2.x) and (self.xyz1.y <= kok.y <= self.xyz2.y):
            return True
        else:
            return not True


gg = Popoint(20, 40)
ggwp = Popoint(40, 60)
barhat = Popoint(1212, 1)
tp = Rectalnoe()
print(tp.ploshad())
print(tp.perimetr())
print()

import random

# задача 5
class Wall:
    def __init__(self, width):
        self.width = width
        self.height = random.randint(3, 7)

    def print_figure(self):
        d = '''⬛'''
        for i in range(self.height):
            print(self.width * d)

# другое решение 5 задачи
import random

class Wall:
    def __init__(self, x):
        self.x = x
        self.y = random.randint(1, 10)

    def print_figure(self):
        for i in range(self.y):
            a = '  _'
            b = '|_|'
            print(a * self.x, '\n', b * self.x)

obj = Wall(5)
obj.print_figure()

obj = Wall(width=2)
obj.print_figure()