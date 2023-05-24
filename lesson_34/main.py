# slovar = {"key1": "value1",
#           "key2": "value2",
#           "key3": "value3",
#           "key4": "value4",
#           "key5": "value5"}
# keys = slovar.values()
# values = slovar.keys()
# print(keys)
# print(values)


# zadacha 2
# x = ["Никита", "Екатерина", "Арсалан", "Наталья", "Григорий", "Евгений", "Анастасия", "Андрей", "Евгения", "Герман", "Тимур", "Ярослава", "Есения", "Даниил", "Данил"]
# imya = input().capitalize()
# counter = 0
# if imya in x:
#     counter += 1

# zadacha 3
# import math
# x = float(input())
# print(math.ceil(x))

# zadacha 4
# import string
# import random
# a = int(input())
# b = ''
# alphabet = string.ascii_uppercase
# alphabet = list(alphabet)
# for i in range(a):
#     b += random.choice(alphabet)
# print(b)
# y = ""
# for i in b:
#     if i not in y:
#         y += i
# print(y)

# zadacha 5
# while True:
#     a = input()
#     if a[:5] == "Суета":
#         break
#     else:
#         continue


# zadacha 6
# x = "abcdefghijklmnopqrstuvw"[::-1]
# print(x[0:-1:2])


# zadacha 7
# import random
# a = set()
# for i in range(10):
#     b = random.randint(0, 15)
#     a.add(b)
# a = list(a)
# print(a)

x = ["Ryan", "Kieran", "Mark",]
c = []
a = x[0]
b = x[-1]
c += a
print(c)
