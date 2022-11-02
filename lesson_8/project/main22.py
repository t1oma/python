# import editional
# import random
#
# print(editional.logo)
#
# score = 0
# data = editional.data
# is_game = True
# while is_game:
#     a = random.choice(data)
#     b = random.choice(data)
#     while a == b:
#         b = random.choice()
#     print("Твой счет:", score)
#     print("-" * 20)
#     print(f"А: {a['name']}. {a['description']} из {a['country']}")
#     print(editional.vs)
#     print(f"B: {b['name']}. {b['description']} из {b['country']}")
#     select = input("У кого больше подписоты? (А, В, МЕНЯЙ)").upper().strip()
#     if select == "МЕНЯЙ":
#         continue
#     if select == "А" or select == "В":
#         if a["follower_count"] > b["follower_count"] and select == "А":
#             score = score + 1
#             print("Правильно")
#         elif a["follower_count"] < b["follower_count"] and select == "А":
#             score = score + 1
#             print("Правильно")
#         else:
#             print("Одна ошибка и ты ошибся")
#             is_game = False
#     else:
#         print("Я обиделся💔")
#         quit()