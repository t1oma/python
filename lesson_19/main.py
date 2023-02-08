# import easygui

# print(ord("Ж"))
# print(chr(97))

# задача 1
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
# eng_alphabet2 = eng_alphabet[::-1]
# alphabet2 = alphabet[::-1]
#
# y = ""
#
#
#
# x = input("Что будем шифровать? >>>").lower()
# for i in x:
#     if i in eng_alphabet:
#         if i not in eng_alphabet:
#             y += i
#         else:
#             y += eng_alphabet2 [eng_alphabet.index(i)]
#     if i in alphabet:
#         if i not in alphabet:
#             y += i
#         else:
#             y += alphabet2 [alphabet.index(i)]
# print(y)
# easygui.msgbox(
#     msg=y,
# )

# a = input('введи чо то')
# n = int(input('сдвиг-'))
# mas = []
# fraz = ''
# for i in a:
#    fraz += chr(ord(i)+ n)
# print(fraz)

# a = input('гшрагшу:')
# n = int(input('sdasdsad:'))
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# fraz = ''
# for i in a:
#     c = alphabet.index(i)
#     c = (c + n) % 33
#     fraz += alphabet[c]
# print(fraz)

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper()
fraz = 'ЫНУЪЫ, УЧЫЧЩДТ ЮЧЫНФЧЪЕ ЙД АЫЧЙД ЩИРЛИМИФС'
contr_slov = 'ТЕКСТ'
frazer = ''
for i in fraz:
    if i in alphabet or i == ' ':
        frazer += i
mas = fraz.split(' ')
for shift in range(1, 33):
    ghj = ''
    for letter in contr_slov:
        c = alphabet.index(letter)
        c = (c + shift) % 33
        ghj += alphabet[c]
    if ghj in mas:
        print('Сдвиг равен: ', shift)
        break