import pygame


def main():
    labyrinthe, y, x = load_labyrinthe()
    objet(labyrinthe)
    point = 0
    display_labyrinthe(labyrinthe)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if check_move(labyrinthe, y - 1, x):
                        point = collect_item(y - 1, x, labyrinthe, point)
                        labyrinthe[y - 1][x] = 'm'
                        labyrinthe[y][x] = ' '
                        y = y - 1
                elif event.key == pygame.K_RIGHT:
                    if check_move(labyrinthe, y, x + 1):
                        point = collect_item(y, x + 1, labyrinthe, point)
                        labyrinthe[y][x + 1] = 'm'
                        labyrinthe[y][x] = ' '
                        x = x + 1
                elif event.key == pygame.K_DOWN:
                    if check_move(labyrinthe, y + 1, x):
                        point = collect_item(y + 1, x, labyrinthe, point)
                        labyrinthe[y + 1][x] = 'm'
                        labyrinthe[y][x] = ' '
                        y = y + 1
                elif event.key == pygame.K_LEFT:
                    if check_move(labyrinthe, y, x - 1):
                        point = collect_item(y, x - 1, labyrinthe, point)
                        labyrinthe[y][x - 1] = 'm'
                        labyrinthe[y][x] = ' '
                        x = x - 1

                display_labyrinthe(labyrinthe)


main()
