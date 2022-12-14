# множества
# set() # преобразование ко множеству
# mySet = {1, 2, 3, 4} # неупорядочные тип данных
# print(mySet)

# mySet = {"А", 0, True}
# print(mySet)

# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# print(set1 | set2)  # объединение  .union()
# print(set1 & set2)  # пересечение  .intersection()
# print(set1 - set2)  # разность  .difference()
# print(set1 ^ set2)  # симметрическая разность  .symmetric_difference()

# словарь
# mydict = {"Ключик1": 1,
#           "Ключик2": "Значение2",
#           "Ключик3": {"Влож1": -1}}

# from random import randint
# lst = []
# for _ in range(5):
#     lst.append(randint(1, 5))
# print(lst)
#
# unique = set(lst) # перевод во множество, удалили повторение
# print(f"{len(unique)} шт.: {unique}")

# from random import randint
# size = randint(100, 1000)
# r_start = 0
# r_end = 10000
# lst1 = []
# lst2 = []
#
# for _ in range(size):
#     lst1.append(randint(r_start, r_end))
#     lst2.append(randint(r_start, r_end))
#
# set1 = set(lst1)
# set2 = set(lst2)
# overall = set1.intersection(set2)   # set1 & set2
# print(f"Общих чисел: {len(overall)}")
# print(f"[Кол-во генераций]: {size}")
# print(f"[Минимальное значение]: {min(overall)}")
# print(f"[Максимальное значение]: {max(overall)}")
# print(sorted(overall)) # -> список, при том сортированный

# s = set()  # set() - создание пустого множества.
# insert = ""
# while insert != "end":
#     insert = input("Число: ")
#     if insert.lstrip("-").isdigit(): # .lstrip() - убрать символы слева
#         if insert not in s:
#             print("❌ Нет")
#             s.add(insert)
#         else:
#             print("✅ Да")
#     elif insert == "end":
#         break
#     else:
#         print("❗ Число хочу")


# lst1 = [0, False, 1 - 1, "один", 2, 3.14]
# print(f"{lst1} - возможно, есть повторения")
# set = set(lst1)
# print(f"{set1} - повторений нет")
# if len(lst1) != len(set):
#     print("Повторения есть")
# else:
#     print("Повторений нет")

# phrase = "Я люблю movavi, программирование, а ещё я люблю пельмени!".lower
# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', ',', '.', '?', '>', '<', "'", '"', '/', ':', ';']
# text = ""
# for char in phrase: # перебор каждого символа фразы
#     if char not in symbols: # если не спец символ, то добавляем
#         text = text + char
# text = text.split(" ")
# s = set(text)
# print(f"Различных слов: {len(s)} шт.")

n = int(input("Количество связей деревьев: "))
gen = {}
for _ in range(n):
    child, parent = input("Ребенок Родитель: ").upper().split()
    if parent not in gen: # если родителя еще нет в гене
        gen[parent] = [child]
    else: # если папаша уже есть
        gen[parent].append(child) # добавляем ребенка
print(gen)
