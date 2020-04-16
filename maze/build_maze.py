#! /usr/bin/env python3
# coding:utf-8
# creating a maze from a txt file
def load_labyrinthe():
    lab = []
    m_position_x = 0
    m_position_y = 0
    with open("../map.txt") as file:
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
if __name__ == '__main__':
    main()
