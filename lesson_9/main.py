# # for
# lst = ["А", "Б", "В", "Г", "Д"]
# for ellement in lst:
#     print(ellement)
#
# for index in range(0, 5):
#     print(index)

# while
# x = 10
# while x != 0:
#     print(x)
#     x -= 1 # x = x - 1

# word = input("Введи словечко: ")
# while word:  # работает пока ворд не пустой(из-зи типа  "строка)
#     print(word, end=" ")
#     word = word[:-1]

# number = int(input("Число: "))
# while number: # пока намбер не равен нулю(из-за типа "число")
#     number -= 1 # тоже самое что и number = number = -1
#     if number % 2 == 0:
#         print(number, end=" ")

x = int(input("Число: "))
step = 0
while x != 1:
    step += 1 # то же самое что и step = step + 1
    if x % 2 == 0:
        print(f"{step})", end=" ")
        print(x, "/ 2 =", end=" ")
        x = x // 2 # // чтобы было не 13.0 а 13
        print(x)
    else:
        print(f"{step})", end=" ")
        print(x, "* 3 + 1 =", end=" ")
        x = x * 3 + 1
    print(x)
print(step, "шагов")
