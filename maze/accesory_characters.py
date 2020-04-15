import pygame
""" list characters and accessory more initialization
"""
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
