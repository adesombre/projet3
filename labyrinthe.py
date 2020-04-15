

import random
import pygame

pygame.init()
size = (15 * 30, 15 * 30)
screen = pygame.display.set_mode(size)

w = pygame.image.load('ressource/mur.png').convert_alpha()
f = pygame.image.load('ressource/fond.jpg').convert_alpha()
m = pygame.image.load('ressource/macGyver.png').convert_alpha()
m = pygame.transform.scale(m, (30, 30))
g = pygame.image.load('ressource/Gardien.png').convert_alpha()
a = pygame.image.load('ressource/aiguille.png').convert_alpha()
a = pygame.transform.scale(a, (30, 30))
b = pygame.image.load('ressource/seringue.png').convert_alpha()
b = pygame.transform.scale(b, (30, 30))
c = pygame.image.load('ressource/ether.png').convert_alpha()
c = pygame.transform.scale(c, (30, 30))


# programme principal

# creating a maze from a txt file
def load_labyrinthe():
    lab = []
    m_position_x = 0
    m_position_y = 0
    with open("map.txt") as file:
        for y, ligne in enumerate(file):
            lab_line = []
            for x, char in enumerate(ligne):
                if char != '\n':
                    if char == "m":
                        m_position_x = x
                        m_position_y = y
                    lab_line.append(char)
            lab.append(lab_line)
    return lab, m_position_y, m_position_x


# display of a maze on the screen
def display_labyrinthe(labyrinthe):
    for y, line in enumerate(labyrinthe):
        for x, case in enumerate(line):
            if case == "#":
                screen.blit(w, (x * 30, y * 30))
            elif case == " ":
                screen.blit(f, (x * 30, y * 30))
            elif case == "m":
                screen.blit(m, (x * 30, y * 30))
            screen.blit(g, (1 * 30, 1 * 30))
    objet(labyrinthe)
    screen.blit(b, (x * 30, y * 30))
    pygame.display.flip()


# creation of objects to capture
def objet(labyrinthe):
    objects = ["a", "b", "c"]
    for o in objects:
        xo = random.randint(0, 14)
        yo = random.randint(0, 14)
        while labyrinthe[yo][xo] != " ":
            xo = random.randint(0, 14)
            yo = random.randint(0, 14)

        labyrinthe[yo][xo] = o


# mac giver character's move collision wall
def check_move(lab, new_y, new_x):
    if 0 <= new_y < len(lab) and 0 <= new_x < len(lab[new_y]) and \
            lab[new_y][new_x] != "#":
        return True
    else:
        return False


# verification collision  object character , guardian
def collect_item(y, x, lab, point):
    if lab[y][x] != " ":
        if lab[y][x] == "g":
                end_game(point)
        else:
            point = point + 1
            print(point)
    return point


# end of the game
def end_game(point):
    if point == 3:
        print("vous avez gagnee!!")
    else:
        print("vous avez perdu ...")
    exit()


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
