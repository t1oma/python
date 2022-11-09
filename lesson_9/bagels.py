# import random
#
# length = 3
# life = 10
#
#
# answer = random.randint(100, 999)
# answer = str(answer)  # число в строчку
# answer = list(answer)  # строчка в список
#
#
#
#
#
# while life: # while life != 0
#     is_guessed = False  # отгадано?
#     print("=" * 10)
#     # print("❤💔💕Жизней: ", life)
#     print("Жизней:", end=" ")
#     for _ in range(0, life):
#         print("♥", end=" ")
#     print() # разрыв
#
#     guess = input("Предположение: ")
#     if len(guess) != 3 or not guess.isdigit():
#         # если длина не равна 3 или это не число
#         print("Ты ошибся, друг(от 100 до 999 пжпж)")
#         continue
#
#     if list(guess) == answer:
#         print("Ура победа ура🥳🥳🥳")
#         is_guessed = True
#         break
#
#     if not is_guessed:
#         for i in range(0, length):
#             if guess[i] == answer[i]:  # совпадение позиции и значения
#                 print("Bagels")
#                 is_guessed = True
#                 break  # выход из for
#
#     if not is_guessed:
#         for char in guess: # char = элемент
#             if char in answer: # совпадение значения
#                 print("Fermi")
#                 is_guessed = True
#                 break
#
#     if not is_guessed:
#         print("Piko😭👺👹") # Вообще мимо
#
#     life -= 1