beans = 20

p1Name = input("Имя первого игрока?")
p2Name = input("Имя второго игрока?")


def change(x):
    global beans
    beans = beans - x


while beans > 1:
    while True:  # бесконечный цикл, остановится при нормальном значении
        p1 = int(input(f"{p1Name}, сколько фасолин возьмёшь?"))
        if p1 <= 3 and p1 >= 1:
            break
    change(p1)
    if beans <= 0:
        print("Победил" f"{p2Name}")
    print("Фасолин - " f"{beans}")
    while True:  # бесконечный цикл, остановится при нормальном значении
        p2 = int(input(f"{p2Name}, сколько фасолин возьмёшь?"))
        if p2 <= 3 and p2 >= 1:
            break
    change(p2)
    if beans <= 0:
        print("Победил" f"{p1Name}")
    print("Фасолин - " f"{beans}")