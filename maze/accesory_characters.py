#! /usr/bin/env python3
# coding:utf-8
import pygame
""" list characters and accessory more initialization
"""
pygame.init()
size = (15 * 30, 15 * 30)
screen = pygame.display.set_mode(size)
wall = pygame.image.load('ressource/mur.png').convert_alpha()
fond = pygame.image.load('ressource/fond.jpg').convert_alpha()
mc_gyver = pygame.image.load('ressource/macGyver.png').convert_alpha()
mc_gyver = pygame.transform.scale(mc_gyver, (30, 30))
guardian = pygame.image.load('ressource/Gardien.png').convert_alpha()
guardian = pygame.transform.scale(guardian, (30, 30))
needle = pygame.image.load('ressource/aiguille.png').convert_alpha()
needle = pygame.transform.scale(needle, (30, 30))
syringe = pygame.image.load('ressource/seringue.png').convert_alpha()
syringe = pygame.transform.scale(syringe, (30, 30))
bottle_ether = pygame.image.load('ressource/ether.png').convert_alpha()
bottle_ether = pygame.transform.scale(bottle_ether, (30, 30))
