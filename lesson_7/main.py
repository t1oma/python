# ZeroDivisionError
# x = 7/0

# TypeError
# x = 15 + "a"

# IndexError
# x = [0, -5.5, "пять"]
# print(x[3])

# SyntaxError
# x = "Привет, я Артём

# ValueError
# int("А")

# NameError
# print(x)

# AssertionError
# def summa(numbers):
#     return sum(numbers)
#
# assert summa([1,2]) == 3
# assert summa([1,2]) == 4

# try:
#     div = int(input("Введи число для деления: "))
#     x = 5/div
# except ZeroDivisionError: #обработка деления на ноль
#     print("У тебя ошибка деления на ноль!!!")
# # except Exception: #обработка любой ошибки
# #     print("Ошибка!")
# except ValueError: #обработка str и int
#     print("Впиши цифру пожалуйста!!!")
# else: # else - если ошибок не было
#     print("Все гуд!")
# finally: # finally сработает всегда
#     print("Я проверил и попытался!")
#
# print("Я сработал")

# lst = []
# try:
#     f = open("file.txt") # файл помещен в f
# except FileNotFoundError:
#     print("А файла то нет")
# else:
#     try:
#         for line in f: #для каждой строчке в файле
#             lst.append(int(line)) # добавить в список число
#     except ValueError:
#         print("Я хочу только цифры :(")
#     else:
#         print("Все хорошо!")
# finally:
#     f.close()
# print(lst)

# try:
#     5/0
# except ZeroDivisionError as error_message:
#     print("Слушай, а тут ошибочка вылезла", error_message)

# x = input("Введи любое имя:").lower().strip()
# try:
#     if x  == "антон":
#         raise Exception("Имя моего препода запрещено") # raise - вызов ошибки
# except Exception:
#     print("???")

# try:
#     x = 5/0
# except ZeroDivisionError:
#     pass # затычка, ничего
#
# if 5 == 2:
#     pass

import random
while True:
    print("Угадай число")
    try:
        difficult = int(input("Введи максимальное число для угадывания:"))
        if difficult < 1:
            raise Exception
    except Exception:
        print("Число > 0")
        continue

    mini = 0
    maxi = difficult
    computer_number = random.randint(0, difficult)
    life = 7
    while life > 0:
        try:
            user_number = int(input("Введи число: "))
        except ValueError:
            print("Нужно число")
            continue
        if user_number < 0 or user_number > difficult:
            print(f"Введи число в интервале")
            continue
        if computer_number == user_number:
            print("Вы победили!")
            break
        elif computer_number < user_number:
            print("Нужно меньше.")
            maxi = user_number
        else:
            print("Нужно больше.")
            mini = user_number
        print(f">>> Интервал: {mini} – {maxi}")
        life = life - 1
        print("❤️:", life)
    answer = input("Хочешь продолжить?").lower().strip()
    if answer == "Да".lower().strip():
        continue
    else:
        break