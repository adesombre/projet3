import random


class Labyrinth:
    def __init__(self, map_path):
        self.lab = []
        self.load_labyrinth(map_path)
        self.randomize_objects()

    def load_labyrinth(self, map_path):
        lab = []
        with open(map_path) as file:
            for ligne in file:
                lab_line = []
                for char in ligne:
                    if char != '\n':
                        lab_line.append(char)
                lab.append(lab_line)
        self.lab = lab

    def find_player(self):
        """
        Find player position in labyrinth.
        :return: y, x position
        """
        for y, line in enumerate(self.lab):
            for x, char in enumerate(line):
                if char == "m":
                    return y, x
        return 0, 0

    def randomize_objects(self):
        objects = ["a", "b", "c"]
        for o in objects:
            xo = random.randint(0, 14)
            yo = random.randint(0, 14)
            while self.lab[yo][xo] != " ":
                xo = random.randint(0, 14)
                yo = random.randint(0, 14)

            self.lab[yo][xo] = o

    # mac giver character's move collision wall
    def check_move(self, new_y, new_x):
        if 0 <= new_y < len(self.lab) and 0 <= new_x < len(self.lab[new_y]) and \
                self.lab[new_y][new_x] != "#":
            return True
        else:
            return False

    def update_character(self, new_y, new_x):
        old_y, old_x = self.find_player()
        self.lab[old_y][old_x] = " "
        self.lab[new_y][new_x] = "m"

    def collect_item(self, y, x, point):
        if self.lab[y][x] != " ":
            if self.lab[y][x] == "g":
                self.end_game(point)
            else:
                point = point + 1
                print(point)
        return point

    def end_game(self, point):
        if point == 3:
            print("vous avez gagnee!!")
        else:
            print("vous avez perdu ...")
        exit()
