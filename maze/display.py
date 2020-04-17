#! /usr/bin/env python3
# coding:utf-8

import pygame
from maze import accesory_characters


def display_labyrinthe(labyrinthe):
    print(labyrinthe)
    for y, line in enumerate(labyrinthe):
        for x, case in enumerate(line):
            if case == "#":
                accesory_characters.screen.blit(accesory_characters.wall, (x * 30, y * 30))
            elif case == " ":
                accesory_characters.screen.blit(accesory_characters.fond, (x * 30, y * 30))
            elif case == "m":
                accesory_characters.screen.blit(accesory_characters.mc_gyver, (x * 30, y * 30))
            elif case == "g":
                accesory_characters.screen.blit(accesory_characters.guardian, (x * 30, y * 30))
            elif case == "a":
                accesory_characters.screen.blit(accesory_characters.needle, (x * 30, y * 30))
            elif case == "b":
                accesory_characters.screen.blit(accesory_characters.syringe, (x * 30, y * 30))
            elif case == "c":
                accesory_characters.screen.blit(accesory_characters.bottle_ether, (x * 30, y * 30))
    pygame.display.flip()
