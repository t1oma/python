# # задача 1
# x = "Ветер, ветер, ты могуч!".lower()
# symbols = list("!,?-.")
# phrase_cleared = ""
# for char in x:
#     if char not in symbols:
#         phrase_cleared += char
#
# d = {}
# phrase_list = phrase_cleared.split() # разбили на слова
# for word in phrase_list:
#     if word not in d: # если ключа в словаре нет
#         d[word] = 1  # первое вхождение
#     else:
#         d[word] += 1 # плюс повторение
# print(d)


# задача 2
# d = {"Молоко": 68, "Открытка": 100, "Диван деда": 999}
# s = 0
# for i in d.values(): # перебор среди ЗНАЧЕНИЙ словаря
#     s += i
# print(s)

# задача 5
d = {'Один': 1, 'Два': 2, 'Три': 3, 'Четыре': 4, 'Пять': 5}
d["Один"], d["Пять"] = d["Пять"], d["Один"]
del d['Два']
d["new_key"] = 'ney_value'