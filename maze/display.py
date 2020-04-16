#! /usr/bin/env python3
# coding:utf-8
import accesory_characters
import moving_objets_and_characters
import pygame
def display_labyrinthe(labyrinthe):
    for y, line in enumerate(labyrinthe):
        for x, case in enumerate(line):
            if case == "#":
                accesory_characters.screen.blit(accesory_characters.w, (x * 30, y * 30))
            elif case == " ":
                accesory_characters.screen.blit(accesory_characters.f, (x * 30, y * 30))
            elif case == "m":
                accesory_characters.screen.blit(accesory_characters.m, (x * 30, y * 30))
            accesory_characters.screen.blit(accesory_characters.g, (1 * 30, 1 * 30))
    moving_objets_and_characters.objet(labyrinthe)
    accesory_characters.screen.blit(accesory_characters.a, (x, y))
    pygame.display.flip()
if __name__ == "__main__":
    pass
