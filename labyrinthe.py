# fonction  affichage du labyrhin

import random


# programme principal


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


def display_labyrinthe(labyrinthe):
    for line in labyrinthe:
        print("".join(line))


def objet(labyrinthe):
    object = ["a", "b", "c"]
    for o in object:
        xo = random.randint(0, 14)
        yo = random.randint(0, 14)
        while labyrinthe[yo][xo] != " ":
            xo = random.randint(0, 14)
            yo = random.randint(0, 14)
        labyrinthe[yo][xo] = o


def check_move(lab, new_y, new_x):
    if 0 <= new_y < len(lab) and 0 <= new_x < len(lab[new_y]) and \
            lab[new_y][new_x] != "#":
        return True
    else:
        return False


def collect_item(y, x, lab, point):
    if lab[y][x] != " ":
        if lab[y][x] == "g":
            end_game(point)
        else:
            point = point + 1
            print(point)
    return point


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
    while True:
        display_labyrinthe(labyrinthe)
        user_input = input("appuyer sur un touche!")
        if user_input == 't':
            if check_move(labyrinthe, y - 1, x):
                point = collect_item(y - 1, x, labyrinthe, point)
                labyrinthe[y - 1][x] = 'm'
                labyrinthe[y][x] = ' '
                y = y - 1
        elif user_input == 'r':
            if check_move(labyrinthe, y, x + 1):
                point = collect_item(y, x + 1, labyrinthe, point)
                labyrinthe[y][x + 1] = 'm'
                labyrinthe[y][x] = ' '
                x = x + 1
        elif user_input == 'b':
            if check_move(labyrinthe, y + 1, x):
                point = collect_item(y + 1, x, labyrinthe, point)
                labyrinthe[y + 1][x] = 'm'
                labyrinthe[y][x] = ' '
                y = y + 1
        elif user_input == 'l':
            if check_move(labyrinthe, y, x - 1):
                point = collect_item(y, x - 1, labyrinthe, point)
                labyrinthe[y][x - 1] = 'm'
                labyrinthe[y][x] = ' '
                x = x - 1






main()
