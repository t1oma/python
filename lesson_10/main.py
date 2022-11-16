# while True:
#     try:
#         level = int(input("Ярусов:"))
#         if level < 1:
#             raise Exception("Положительное число, плзз")
#     except ValueError:
#         print("Ну блин")
#         continue
#     except Exception as error:
#         print("Низя.", error)
#         continue
#     else:   # если ошибок нет, то выходим из while true
#         break
#
#
# while True:
#     symbol = input("Символ: ")
#     if len(symbol) != 1:
#         print("Хочу один символ и круто программировать")
#     else:
#         break
#
#
# for i in range(1, level + 1):
#     # левая половина
#     print(" " * (level - i), end="")
#     print(symbol * i, end="")
#
#
#     # правая половина
#     print(symbol * i)

# x = int(input("Ваше число: "))
# for mega_anton in range(1, 11):
#     print(x, "x", mega_anton, "=", x * mega_anton)

# ne_znayu = int(input("Ширина: "))
# zabil = int(input("Высота: "))
#
# for _ in range(0, zabil):
#     print("# " * ne_znayu)


