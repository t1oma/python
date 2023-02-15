# f = open("восьмой бэ дежурный класс.txt", "w", encoding="utf-8") # encoding - раскодировка русских символов
# f.write("Ноль\nОдин")
# f.close()

# f = open("восьмой бэ дежурный класс.txt", "r", encoding="utf-8")
# t = f.read()
# t1 = f.readlines() # файл разбили по линиям в список
# print(t1)
# for line in t1:
#     print(line.rstrip()) # rstrip() - убирает пустоты справа

# a = input("Введи название файла")
# f = open(a + ".txt", "w", encoding="utf-8")
# b = input("")
# f.write(b)
# print("файл записан")
# while b != '':
#     f.write(b + '\n')
#     b = input('введи')
# print('файл записан')
# f.close()

# a = input('введи название')
# f = open(a, "r+", encoding="utf-8")
# b = f.readlines() # список строк
# f.close()
# print(b)
# f = open(a, "w", encoding="utf-8")
# n = 0
# print(b)
# for line in b:
#     n += 1
#     f.write(f'{n}) {line.rstrip()}')

# f = open('papa.txt', "r", encoding='utf-8')
# b = f.readlines()
# n = int(input("Кол-во строк последних файла"))
# d = b[len(b) - n:]
# for i in d:
#     print(i.rstrip())

# f = open('tadjik artem.txt', "r", encoding='utf-8')
# b = f.readlines()
# print(b)
# n = 0
# while b != []: # пока список не empty
#     d = b[:3] # зафиксировали 3 элемента
#     del b[:3]
#     stas = open(f'{n}.txt', 'w', encoding='utf-8')
#     for i in d:
#         stas.write(i)
#     stas.close()
#     n += 1
