# def helloworld(chislo): # объявление функции
#     print("Hello world")
#     print("ЦИфра", chislo)
#
# from random import randint
# number = randint(5, 10)
# helloworld(number) # вызов функции с аргкментов number

# from random import randint
#
# def number_2(chislo):
#     x = chislo / 2
#     return x # возвращаем из функции x
#
# number = randint(10, 100)
# result = number_2(number) # resukt = return x (от number_2)
# print(result)

# задача 1
# def is_sorted(spisok):
#     sort = sorted(spisok)
#     print(sort)
#     if spisok == sort:
#         return True
#
# lst = [5, 7, 9, 1, 0]
# if is_sorted(lst): # если возвращен True, то
#     print("Сортированы")
# else:
#     print("Неупорядочено")

# Задача 2
def find_longest(spisok):
    len_list = []
    for word in spisok:
        len_list.append(len(word))
    maxi = max(len_list) # максимальная длина
    ind = len_list.index(maxi) # Индекс максимальной длины
    return (spisok[ind], len_list[ind])

lst = ["Богдан", "Дом", "Программирование"]
print(find_longest(lst))


