from art import box_carrot, box_empty, box_close
from random import choice

def generation_boxes(status1, status2):
    result = ""
    if status1 == "ПУСТОТА":
        box1 = box_empty.format(COLOR1.center(13)).split("\n")
    elif status1 == "МОРКОВКА":
        box1 = box_carrot.format(COLOR1.center(13)).split("\n")
    else:
        box1 = box_close.format(COLOR1.center(13)).split("\n")

    if status2 == "ПУСТОТА":
        box2 = box_empty.format(COLOR2.center(13)).split("\n")
    elif status2 == "МОРКОВКА":
        box2 = box_carrot.format(COLOR2.center(13)).split("\n")
    else:
        box2 = box_close.format(COLOR2.center(13)).split("\n")

    for element in zip(box1, box2):
        result += "   ".join(element) + "\n"
    result += p1name[:10].center(13) + " " * 7 + p2name[:10].center(13) 
    return result


COLORS = ["ФИОЛЕТОВАЯ", "КАЙФОВАЯ", "МАГАДАНСКАЯ", "УНЫЛАЯ"]
COLOR1 = choice(COLORS)
COLOR2 = choice(COLORS)
while COLOR1 == COLOR2: # цвета разные
    COLOR2 = choice(COLORS)

p1box = "ЗАКРЫТО"
p2box = "МОРКОВКА"


p1name = input(">>>  Имя первого игрока: ")
while p1name.strip() == "": # если убрав пробелы останется пустота
    p1name = input(">>>  Имя первого игрока: ")
p2name = input(">>>  Имя второго игрока: ")
while p2name.strip() == "": # если убрав пробелы останется пустота
    p1name = input(">>>  Имя второго игрока: ")

print(generation_boxes("ПУСТОТА", "м0Х"))

while True:
    print(f"{p2name}, в твоей коробке {p2box}")

    # БЛЕФ / ПРАВДА
    action = input(f"Нужно сделать выбор:\n"
                   f"1. Блеф: сказать что в коробке {p1box}\n"
                   f"2. Правда: сказать что в коробке {p2box}\n"
                   f">>> (Б - блеф, П - правда) -> ").upper

    while action != "Б" and action != "П":
        action = input(f">>> (Б - блеф, П - правда) -> ").upper()

    print("\n" * 70)
    input(f">>> {p1name} открывает глаза(Enter)...")
    if action == "Б":
        print(f"{p2name} сообщает, что в его коробке находится {p1box}")
    else:
        print(f"{p2name} сообщает, что в его коробке находится {p2box}")

    # Обмен
    change = input("Хочешь меняться?\n"
                   "Д(меняться) или Н(не меняться)").upper()
    if change == "Д":
        p1box, p2box = p2box, p1box # меняем содержимое коробок
        input(f"{p1name} закрывай глаза, (Enter)...")

        if p2box == "МОРКОВКА":
            box2 = box_carrot.format(COLOR2.center(13)).split("\n")
        else:
            box2 = box_empty.format(COLOR2.center(13)).split("\n")

    else:
        break

print("========== РЕЗУЛЬТАТЫ ==========")
print(generation_boxes(p1box, p2box))
if p1name == "МОРКОВКА":
    print(p1name, "победил")
else:
    print(p2name, "победил")

