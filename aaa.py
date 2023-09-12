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

a = int(input())
print(format(a, ','))