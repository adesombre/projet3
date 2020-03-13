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
    return lab, m_position_x, m_position_y


def display_labyrinthe(labyrinthe):
    for line in labyrinthe:
        print("".join(line))


def objet(labyrinthe):
    object = ["a", "b", "c"]

    for o in object:
        xo = random.randint(0, 14)
        yo = random.randint(0, 14)
        while labyrinthe[yo][xo] == "#":
            xo = random.randint(0, 14)
            yo = random.randint(0, 14)
        labyrinthe[yo][xo] = o


def main():
    labyrinthe, x, y = load_labyrinthe()
    objet(labyrinthe)
    while True:
        display_labyrinthe(labyrinthe)
        user_input = input("appuyer sur un touche!")
        p=0
        if user_input == 't':
            # y - 1 est la case au dessus
            if labyrinthe[y - 1][x] != '#':
                if 'm' != objet(labyrinthe):

                    print("point")

                labyrinthe[y - 1][x] = 'm'
                labyrinthe[y][x] = ' '
                y = y - 1
        elif user_input == 'r':
            if labyrinthe[y][x + 1] != '#':
                if 'm' != objet(labyrinthe):
                    print("point")
                labyrinthe[y][x + 1] = 'm'
                labyrinthe[y][x] = ' '
                x = x + 1
        elif user_input == 'l':
            if labyrinthe[y][x - 1] != '#':
                if 'm' != objet(labyrinthe):
                    print("point")
                labyrinthe[y][x - 1] = 'm'
                labyrinthe[y][x] = ' '
                x = x - 1
        elif user_input == 'b':
            if labyrinthe[y + 1][x] != '#':
                if 'm' != objet(labyrinthe):
                    print("point")
                labyrinthe[y + 1][x] = 'm'
                labyrinthe[y][x] = ' '
                y = y + 1


main()
def prend_objet():
    point=0
    if 'm' != objet(labyrinthe):
        print("point")
        point = point +1
    return point