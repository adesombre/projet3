# ! /usr/bin/env python3
# coding:utf-8

import pygame

from labyrinth import Labyrinth
from display import Display


def main():
    lab = Labyrinth("../map.txt")
    y, x = lab.find_player()
    point = 0
    display = Display()
    display.display_labyrinthe(lab.lab)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if lab.check_move(y - 1, x):
                        point = lab.collect_item(y - 1, x, point)
                        lab.update_character(y - 1, x)
                        y = y - 1
                elif event.key == pygame.K_RIGHT:
                    if lab.check_move(y, x + 1):
                        point = lab.collect_item(y, x + 1, point)
                        lab.update_character(y, x + 1)
                        x = x + 1
                elif event.key == pygame.K_DOWN:
                    if lab.check_move(y + 1, x):
                        point = lab.collect_item(y + 1, x, point)
                        lab.update_character(y + 1, x)
                        y = y + 1
                elif event.key == pygame.K_LEFT:
                    if lab.check_move(y, x - 1):
                        point = lab.collect_item(y, x - 1, point)
                        lab.update_character(y, x - 1)
                        x = x - 1

                display.display_labyrinthe(lab.lab)

if __name__ == '__main__':
    main()
