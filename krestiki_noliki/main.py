from pprint import pprint
from typing_extensions import TypeVarTuple

import pygame

pygame.init()
font_object = pygame.font.SysFont('dejavuserif', 28)

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

area_width, area_height = 3,3
cell_width, cell_height = (SCREEN_WIDTH // area_width), (SCREEN_HEIGHT // area_height)

MAP = [[0] * area_width for i in range(area_height)]
pprint(MAP)
HOD = 0

run = True
while run:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and HOD % 2 == 0:
                mouse_x, mouse_y = event.pos
                row_index = mouse_y // cell_height
                column_index = mouse_x // cell_width
                if MAP[row_index][column_index] == 0:
                    MAP[row_index][column_index] = 1
                print(f'Cell x:{row_index}, y:{column_index}')
                print(MAP)
                HOD += 1
            elif event.button == 1 and HOD % 2 == 1:
                mouse_x, mouse_y = event.pos
                row_index = mouse_y // cell_height
                column_index = mouse_x // cell_width
                if MAP[row_index][column_index] == 0:
                    MAP[row_index][column_index] = 2
                print(f'Cell x:{row_index}, y:{column_index}')
                print(MAP)
                HOD += 1

    for row_index in range(area_height):
        for column_index in range(area_height):
            rect_x = cell_width * column_index
            rect_y = cell_height * row_index
            pygame.draw.rect(
                surface=screen,
                color=(0, 0, 0),
                rect=(rect_x, rect_y, cell_width, cell_height),
                width=1
            )

            if MAP[row_index][column_index] == 1:
                offset = 1
                circle_x = rect_x + cell_width // 2
                circle_y = rect_y + cell_height // 2
                circle_radius = (cell_height - offset * 2) // 2
                pygame.draw.circle(
                    surface=screen,
                    color=(255, 0, 0),
                    center=(circle_x, circle_y),
                    radius=circle_radius,
                    width = 5
                )
                check = False
            elif MAP[row_index][column_index] == 2:
                offset = 1
                circle_x = rect_x + cell_width
                circle_y = rect_y + cell_height
                circle_radius = (cell_height - offset * 2) // 2
                pygame.draw.line(
                    surface=screen,
                    width = 5,
                    color='blue',
                    start_pos = (rect_x, rect_y),
                    end_pos = (rect_x + cell_width, rect_y + cell_height),
                )
                pygame.draw.line(
                    surface=screen,
                    width = 5,
                    color='blue',
                    start_pos = (rect_x + cell_width, rect_y),
                    end_pos = (rect_x, rect_y + cell_height),
                )
                check = True

    if MAP[0][0] == MAP[0][1] == MAP[0][2] == 1 or MAP[1][0] == MAP[1][1] == MAP[1][2] == 1 or MAP[2][0] == \
            MAP[2][1] == MAP[2][2] == 1 or MAP[0][0] == MAP[1][1] == MAP[2][2] == 1 or MAP[0][2] == MAP[1][1] == \
            MAP[2][0] == 1 or MAP[0][0] == MAP[1][0] == MAP[2][0] == 1 or MAP[0][1] == MAP[1][1] == MAP[2][
        1] == 1 or MAP[0][2] == MAP[1][2] == MAP[2][2] == 1:
        screen.blit(font_object.render('победили 0', True, 'black'), (30, 100))
        s = 1
    elif MAP[0][0] == MAP[0][1] == MAP[0][2] == 2 or MAP[1][0] == MAP[1][1] == MAP[1][2] == 2 or MAP[2][0] == \
            MAP[2][1] == MAP[2][2] == 2 or MAP[0][0] == MAP[1][1] == MAP[2][2] == 2 or MAP[0][2] == MAP[1][1] == \
            MAP[2][0] == 2 or MAP[0][0] == MAP[1][0] == MAP[2][0] == 2 or MAP[0][1] == MAP[1][1] == MAP[2][
        1] == 2 or MAP[0][2] == MAP[1][2] == MAP[2][2] == 2:
        screen.blit(font_object.render('победили x', True, 'black'), (30, 100))
        s = 1

    pygame.display.update()
    clock.tick(30)

pygame.quit()