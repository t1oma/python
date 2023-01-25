# def add_one1(a, b):
#     return a + b + 1
#
# add_one = lambda a,b: a + b + 1 #аналогичная лямбда функция
#
# result = lambda answer: True if answer == "Д" else False # if else внутри lambda
#
# # list comprehesion
#
# from random import randint
# lst = []
# for i in range(5):
#     lst.append(randint(1, 5))
# print(lst)
#
# lst2 = [randint(1,5) for n in range(5)]
# # 1. list comprehension всегда пишется в квадратных скобках
# # 2. for n in range() - обычный цикл for -> сколько элементов будет в списке
# # 3. Перед for -> сам добавляемый элемент
# print(lst2)

# Задача 1.
# c2f = lambda c: 9/5 * c + 32
# print(c2f(200))

# f2c = lambda f: (f - 32) * 5/9
# print(f2c(200))
#
# c2k = lambda c: c + 273.15
# print(c2k(200))
#
# k2c = lambda k: k - 273.15
# print(k2c(200))
#
# f2k = lambda f: c2k(f2c(f))
# degree = 203
# print(f2k(degree))

#ЗАДАЧА 2

# from random import randint
# exitcode = lambda vihod: True if vihod == "Д" else False
# while True:
#     q = int(input("Сколько бросаем кубов?"))
#     lst = [randint(1, 6) for i in range(q)]
#     print(lst)
#     if exitcode(input("Выходим?")):
#         break

# ЗАДАЧА 3
from random import choice

chars = [list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
         list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
         list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
         list("abcdefghijklmnopqrstuvwxyz"),
         list("1234567890")
        ]

a = "https://www.google.com"
dict = {}
# f = ""
# for i in range(6):
#     b = choice(chars)
#     c = choice(b)
#     f += c
# print(f)

# f = [choice(choice(chars)) for i in range(6)]
# b = "".join(f)
# print(b)
# if a in dict:
#     print("ок", dict[a])
# else:
#     dict[a] = b
#     print("Ссылке по кайфу", dict[a])

# ЗАДАЧА 5
field = {"A": ["⬜", "⬜", "⬜"],
         "B": ["⬜", "⬜", "⬜"],
         "C": ["⬜", "⬜", "⬜"]}

cell_letter = ["A", "B", "C"]
cell_number = ["1", "2", "3"]

def drawer() -> None:
    """отрисовывает поле 3х3"""
    print(" 1 2 3")
    for row in range(3):
        print(cell_letter[row], end="")
        for column in range(3):
            print(list(field.values())[row][column], end="")
        print()

def turn(player1) -> None:
    """ход игрока"""




