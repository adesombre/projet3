# ! /usr/bin/env python3
# coding:utf-8
import pygame
import build_maze
import moving_objets_and_characters
import display
def main():
    labyrinthe, y, x = build_maze.load_labyrinthe()
    moving_objets_and_characters.objet(labyrinthe)
    point = 0
    display.display_labyrinthe(labyrinthe)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if moving_objets_and_characters.check_move(labyrinthe, y - 1, x):
                        point = moving_objets_and_characters.collect_item(y - 1, x, labyrinthe, point)
                        labyrinthe[y - 1][x] = 'm'
                        labyrinthe[y][x] = ' '
                        y = y - 1
                elif event.key == pygame.K_RIGHT:
                    if moving_objets_and_characters.check_move(labyrinthe, y, x + 1):
                        point = moving_objets_and_characters.collect_item(y, x + 1, labyrinthe, point)
                        labyrinthe[y][x + 1] = 'm'
                        labyrinthe[y][x] = ' '
                        x = x + 1
                elif event.key == pygame.K_DOWN:
                    if moving_objets_and_characters.check_move(labyrinthe, y + 1, x):
                        point = moving_objets_and_characters.collect_item(y + 1, x, labyrinthe, point)
                        labyrinthe[y + 1][x] = 'm'
                        labyrinthe[y][x] = ' '
                        y = y + 1
                elif event.key == pygame.K_LEFT:
                    if moving_objets_and_characters.check_move(labyrinthe, y, x - 1):
                        point = moving_objets_and_characters.collect_item(y, x - 1, labyrinthe, point)
                        labyrinthe[y][x - 1] = 'm'
                        labyrinthe[y][x] = ' '
                        x = x - 1

                display.display_labyrinthe(labyrinthe)


main()
if __name__ == "__main__":
    main()
