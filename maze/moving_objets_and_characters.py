#! /usr/bin/env python3
# coding:utf-8
import random
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

if __name__ == "__main__":
    pass