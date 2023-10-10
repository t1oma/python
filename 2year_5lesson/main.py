import pygame

pygame.init()  # подключение модулей

SCREEN_SIZE = SCREEEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode(SCREEN_SIZE)  # создание экрана заданого размера
#
# run = True
# while run:  # основной игровой цикл
#     for event in pygame.event.get():  # получение списка событий
#         if event.type == pygame.QUIT: # pygame.QUIT => 256
#             run = False
#
# pygame.quit()  # отключение модулей

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

run = True
while run:  # основной игровой цикл
    for event in pygame.event.get():  # получение списка событий
        if event.type == pygame.QUIT:  # pygame.QUIT => 256
            run = False

    #   screen.fill(RED)
    #   pygame.draw.rect(
    #       surface=screen,  # рисуем на основном окне
    #       color=BLUE,      # задаем цвет, указанный в переменной
    #       rect=(50, 50, 100, 100)  # указываем координаты угла и размер
    #   )

    #   pygame.draw.circle(
    #       surface=screen,    # рисуем на основном окне
    #       color=BLUE,        # задаем цвет, указанный в переменной
    #       center=(SCREEEN_WIDTH / 2, SCREEN_HEIGHT / 2),  # центр установим в середину экрана
    #       radius=150
    # )

    #   pygame.draw.circle(
    #       surface=screen,    # рисуем на основном окне
    #       color=BLUE,        # задаем цвет, указанный в переменной
    #       center=(SCREEEN_WIDTH / 2, SCREEN_HEIGHT / 2),  # центр установим в середину экрана
    #       radius=150         # радиус окружности
    # )

    # pygame.draw.polygon(
    #     surface=screen,  # рисуем на основном окне
    #     color=GREEN,  # задаем цвет, указанный в переменной
    #     points=[[10, 180], [50, 190], [200, 180], [220, 30]],  # координаты точек
    #     width=5  # толщина линии
    # )
    #
    # pygame.draw.lines(
    #     surface=screen,
    #     color=GREEN,
    #     points=[[0, 0], [405, 405],
    #             [0, 405], [405, 0]],
    #     closed=False,
    #     width=5
    # )

        # size = 400, 400
        # w, h = size
        # run = True
        # while run:
        #     for e in pygame.event.get():
        #         if e.type == pygame.QUIT:
        #             run = False
        #     pygame.draw.rect(
        #         surface=screen,
        #         color=(255, 0, 0),
        #         rect=(5, 5, w - 10, h - 10)
        #     )
        #
        #     pygame.display.update()



# ------------------ шахматная доска
#     import pygame
#
#     pygame.init()
#
#     BLACK = (0, 0, 0)
#     WHITE = (255, 255, 255)
#
#     size = 400, 400
#     width, heigth = size
#     screen = pygame.display.set_mode(size)
#     w = 0
#     h = 0
#     c = 0
#     screen.fill(WHITE)
#     run = True
#     while run:
#         for e in pygame.event.get():
#             if e.type == pygame.QUIT:
#                 run = False
#
#         for _i in range(500):
#             if w >= 500:
#                 h += 20
#                 c += 20
#                 w = -c
#             else:
#                 pygame.draw.rect(
#                     surface=screen,
#                     color=BLACK,
#                     rect=(w, h, 20, 20)
#                 )
#             w += 40
#
#         pygame.display.update()
#
#     pygame.quit()

# ---------------------- мишень
#     import pygame
#
#     pygame.init()
#     SCREEN_SIZE = w, h = 600, 600
#     screen = pygame.display.set_mode(SCREEN_SIZE)
#     WHITE = (255, 255, 255)
#
#     base_radius = 300
#
#     run = True
#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#
#         screen.fill(WHITE)
#         for i in range(10):
#             pygame.draw.circle(
#                 surface=screen,
#                 color=(211, 89, 10),
#                 center=(w / 2, h / 2),
#                 width=10,
#                 radius=base_radius - (base_radius * 0.1 * i),
#             )
#         pygame.display.update()
#     pygame.quit()




    pygame.display.update()

pygame.quit()

