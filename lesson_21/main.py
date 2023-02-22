# try:
#     x = int(input("Введи число: "))
#     print(x)
# except (ValueError, IndexError):
#     print("Ы")
# # except IndexError:
# #     print("Ы2")
# else:  # когда ошибок не было
#     print("Молодец, что ввел число")
# finally:  # сработает в любом случае
#     print("Я сделал")

# x = input("Как кореша(собаку) зовут? ")
# try:
#     if x == "Антон":
#         raise ValueError("Ты че, пес")
# except ValueError as pelmeni:
#     print("Бек-мек, пук-пук.", pelmeni)

# задача 1
# counter_elements = 0
# counter_sum = 0
# f = open("stas.txt", "r", encoding="utf-8")
# x = f.read().split()
# # split - раскалывает по пробелам и переносам
# for element in x:
#     try:
#         intelement = int(element)
#     except ValueError:
#         print(f"{element} пропущено")
#         continue
#     else:
#         counter_elements += 1
#         counter_sum += intelement
#
# sr_areifm = counter_sum / counter_elements
# print(round(sr_areifm, 1))
#
# f.close()

# 2 задача
# maxi = -1
# try:
#     f = open("stas.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("А, э")
#     quit()
# text = f.readlines()
# f.close()
#
# for i, element in enumerate(text):
#     text[i] = element.split()
# print(text)
#
# for student in text:
#     try:
#         if int(student[3]) > maxi:  # value - не число; index- нет числа
#             maxi = int(student[3])
#     except IndexError:
#         print("Значение отсутствует:", student)
#         continue  # переходим к след. ученику
#     except ValueError:
#         print("Неверное значение:", student)
#         continue  # переходим к след. ученику
# print(maxi)

# 5 задача
# try:
#     f = open("stas.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print('файла нет')
#     quit()
# a = f.readlines()
# f.close()
# if a == []:
#     print('В ФАЙЛЕ НИЧЕГО НЕТ')
#     quit()
# print(a)
# print(f'{len(a)} кол_во строк')
# sim = 0
# slovs = 0
# for i in range(len(a)):
#     a[i] = a[i].strip('\n')
#     sim += len(a[i]) # складываем длину каждой строки
# print(f'{sim} символов')
# for i, j in enumerate(a):
#     a[i] = a[i].split()
#     slovs += len(a[i])
# print(f'{slovs} кол-во слов')

# задача 6
# try:
#     f = open("stas.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print('файла нет')
#     quit()
# a = f.read()
# b = input("Какое слово ищем? >>> ")
# n = a.count(b)
# f.close()
# print(f'слово {b} встречается {n} раз(а).')

n = 1
t = input("введите название файла: ")
try:
    f = open(t + ".txt", "r", encoding="utf-8")
except FileNotFoundError:
    print('файла нет')
    quit()
a = f.read().split()
print(a)
for i in a:
    try:
        n *= int(i)
    except ValueError:
        print("в файле встретился текст, все поломалося")
        continue
f.close()
print(n)
