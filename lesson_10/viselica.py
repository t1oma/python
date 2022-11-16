# import random
# import viselica_art
#
# print(viselica_art.intro)
#
# vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']
#
# word_answer = random.choice(vocabulary).lower()
# word_display = []
#
# for _ in range(len(word_answer)): # выполним букв в слове раз
#     word_display.append("_")
#
# life = 8
# counter = 0 # счетчик проявленных букв
#
# while life > 0 and counter != len(word_answer): # пока есть жизни и все буквы не отгаданы
#     print(viselica_art.stages[life])
#     letter = input("Буква: ")
#     letter_is_he = False # наличие буквы в слове
#     for i in range(len(word_answer)): # пробегаемся по слову
#         if letter == word_answer[i]: # если буква равна букве из слова
#             if word_display[i] != "_": # если буква уже перевернута
#                 letter_is_he = True
#             else:
#                 word_display[i] = letter # переворачиваем букву
#                 counter += 1 # тоже самое что и counter = counter + 1
#
#     if letter_is_he == False: # если буквы не было найдено
#         life -= 1
#     print(word_display)
# if counter == len(word_answer):
#     print("Пабеда🥇")
# else:
#     print(viselica_art.stages[life])
#     print("Проиграл😿")
#
