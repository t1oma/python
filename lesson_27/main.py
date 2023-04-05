# задача 1(taskadditional)
# import math
# zemlekopi = float(input())
# print(math.ceil(zemlekopi))

# задача 1 (tasklesson)
# a = input().upper().strip()
# b = input().upper().strip()
# yellow = ["ЖЕЛТЫЙ", "ЖЁЛТЫЙ"]
# if (a == "КРАСНЫЙ" and b == "СИНИЙ") or (a == "СИНИЙ" and b == "КРАСНЫЙ"):
#     print("Фиолетовый")
# elif (a == "КРАСНЫЙ" and b in yellow) and (a in yellow and b == "КРАСНЫЙ"):
#     print("Оранжевый")
# elif (a == "СИНИЙ" and b in yellow) or (a in yellow and b == "СИНИЙ"):
#     print("Зеленый")
# else:
#     print("Один из цветов введен неверно")

# задача 2
# a = input("lesson-start: ")
# b = int(input("lesson-time: "))
# c = int(input("peremena-time: "))
# d = int(input("colvo: "))
# e = int(a[:2])
# f = int(a[3:])
# time = e * 60 + f
# for i in range(d):
#     e = time // 60
#     f = time % 60
#     print(f"{i + 1} урок: {str(e).rjust(2, '0')}:{str(f).rjust(2,'0')} - ",end='')
#     time += b # прибавили время урока
#     e = time // 60
#     f = time % 60
#     print(f"{str(e).rjust(2, '0')}:{str(f).rjust(2, '0')}")
#     time += c # прибавили время перемены

# задача 3
# a = int(input("Сколько зомби было к началу расчёта: "))
# b = int(input("Сколько каждый может заразить: "))
# c = int(input("На который день делаем расчёт: "))
# for i in range(c):
#     print(a)
#     a = a + a * b

# задача 4
a = input().split(" ")
a = list(map(int, a))
def boba(a):
    lt = []
    for ind, elem in enumerate(a):
        if ind == 0:
            sssr = a[-1] + a[ind + 1]
        elif ind ==len(a)-1:
            sssr = a[ind - 1] + a[0]
        else:
            sssr = a[ind - 1] + a[ind + 1]
        lt.append(sssr)
    return lt

print(boba(a))