import random
# x = [1, 2, 3]
# y = x   # y ссылается на x
# y.append(5)
# print(x)
# print(y)
#
# x = [1, 2, 3]
# y = x[:]  # глубокая копия объекта
# y.append(5)
# print(x)
# print(y)

# a = "Антон"
# b = 48
# c = 183
# print(f'Cамый высокий человек в мире, Имя: {a}, Возраст: {b}, Рост: {c}')
# d = input("Ваше имя?")
# e = int(input("Ваш рост?"))
# print(f'{d}, ты ниже самого высокого человека в мире на {c - e}сантиметров')

# a = input().upper().strip()
# b = input().upper().strip()
# yellow = ["ЖЕЛТЫЙ", "ЖЁЛТЫЙ"]
# red = ["КРАСНЫЙ"]
# blue = ["СИНИЙ"]
# if (a in red and b in blue) or (a in blue and b in red):
#     print("Фиолетовый")
# elif (a in red and b in yellow) or (a in yellow and b in red):
#     print("Оранжевый")
# elif (a in blue and b in yellow) or (a in yellow and b in blue):
#     print("Зеленый")
# else:
#     print("Один из цветов введен неверно")

# a = int(input())
# b = int(input())
# if a > b:
#     for i in range(a, b + 1):
#         print(i ** 2)
# else:
#     for i in range(b, a + 1):
#         print(i ** 2)

# a = int(input())
# b = 1
# for i in range(2, a + 1):
#     b *= i
# print(b)

# a = int(input("начальное кол-во:"))
# b = int(input("процент:"))
# c = int(input("кол-во дней:"))
# e = b / 100
# d = 0
# for i in range(c):
#     print(a)
#     a = a + (a * e)

# stas = [7, 8, 0, 0, 5, 5, 5, 3, 5, 3, 5]
# a = [int (x) for x in stas]
# print(f'+{(stas[0])}({a[1]}{a[2]}{a[3]}){a[4]}{a[5]}{a[6]}-{a[7]}{a[8]}-{a[9]}{a[10]}')
# print("+{}({}{}{}){}{}{}-{}{}-{}{}".format(*stas))

# import string
# mal = string.ascii_lowercase
# bol = string.ascii_uppercase
# a = "Stasponchikpelmeni".lower()
# b = []
# for i in range(len(a)):
#     if a[i].islower():
#         b.append(mal.index(a[i]) + 1)
#     else:
#         b.append(bol.index(a[i]) + 1)
# print(b)
#
# a = int(input())
# print(format(a, ','))

# -----------------------------------------------------------
# урок 2
# задача 1
# x = [2, 3, 4, 5, 6]
# print(sum(x))

# x = [2, 3, 4, 5, 6]
# print(max(x))
# print(min(x))
# y = sorted(x)
# print(y[0], y[-1])

# задача 2
# f = "Тетради Ус Москва обнимать?!"
# print(f"{f[3:16:3]}{f[-5:-2]}")

# 3 задача
l = [1, 2, 2, 3, 1, 4]
# temp = []
# for x in l:
#     if x not in temp:
#         temp.append(x)
# print(temp)

# for elem in l:
#     if l.count(elem) > 1:
#         l.remove(elem)
# print(l)

# anton = [1, 3.14, 2, "Антон"]
# f = {}
# c = 0
# c += 1
# for i in anton:
#     if type(i) in f:
#         f[type(i)] += 1
#     else:
#         f[type(i)] = 1
# print(f)

# x1 = [1, 4, 5, 6]
# x2 = [2, 7]
# print(sorted(x1 + x2))

# задача 6
# x = "Привет, мир".lower()
# f = {}
# stop = "1234567890,!.@#$%^&*"
# for elem in x:
#     if elem not in stop:
#         f[elem] = x.count(elem)
# print(f)

# задача 7
# import string
# bol = string.ascii_uppercase
# mal = string.ascii_lowercase
# f = {}
# for i in range(len(mal)):
#     f[mal[i]] = bol[i]
# print(f)

# задача 8
# b = 0
# while True:
#     a = input().lower().split(' ')
#     if a[0] == "exit":
#         exit()
#     elif a[0] == "result":
#         print(b)
#     elif a[0] == "zero":
#         b = 0
#     elif a[0] == "add":
#         b += int(a[-1])
#     elif a[0] == "mul":
#         b *= int(a[-1])
#     elif a[0] == "minus":
#         b -= int(a[-1])
#     elif a[0] == "div":
#         b //= int(a[-1])

c = 0
d = {
    "add": lambda x: c + x,
    "mul": lambda x: c * x,
    "minus": lambda x: c - x,
    "div": lambda x: c // x,
}

while True:
    vvod = input().split()
    if len(vvod) == 1:  # zero, result, exit
        vvod = vvod[0]  # ['result'] -> result
        if vvod == "exit":
            break
        elif vvod == "result":
            print(c)
        elif vvod == "zero":
            c = 0
    else:  # add, mul, minus, div
        c = d[vvod[0]](int(vvod[1]))