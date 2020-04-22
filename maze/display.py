import pygame


class Display:
    def __init__(self):
        """ list characters and self more initialization
        """
        pygame.init()
        size = (15 * 30, 15 * 30)
        self.screen = pygame.display.set_mode(size)
        self.assets = dict()

        self.load_assets()
        self.prepare_assets()

    def load_assets(self):
        self.assets["wall"] = pygame.image.load('ressource/mur.png')\
                                    .convert_alpha()
        self.assets["background"] = pygame.image.load('ressource/fond.jpg')\
                                          .convert_alpha()
        self.assets["mc_gyver"] = pygame.image.load('ressource/macGyver.png')\
                                        .convert_alpha()
        self.assets["guardian"] = pygame.image.load('ressource/Gardien.png')\
                                        .convert_alpha()
        self.assets["needle"] = pygame.image.load('ressource/aiguille.png')\
                                        .convert_alpha()
        self.assets["syringe"] = pygame.image.load('ressource/seringue.png')\
                                        .convert_alpha()
        self.assets["bottle_ether"] = pygame.image.load('ressource/ether.png')\
                                        .convert_alpha()

    def prepare_assets(self):
        """
        Transform assets that are not at the right size.
        """
        self.assets["mc_gyver"] = pygame.transform.scale(self.assets["mc_gyver"]
                                                         , (30, 30))
        self.assets["guardian"] = pygame.transform.scale(self.assets["guardian"]
                                                         , (30, 30))
        self.assets["needle"] = pygame.transform.scale(self.assets["needle"]
                                                       , (30, 30))
        self.assets["syringe"] = pygame.transform.scale(self.assets["syringe"]
                                                        , (30, 30))
        self.assets["bottle_ether"] = pygame.transform.scale(self.assets["bottle_ether"]
                                                             , (30, 30))

    def display_labyrinthe(self, labyrinth):
        for y, line in enumerate(labyrinth):
            for x, case in enumerate(line):
                if case == "#":
                    self.screen.blit(self.assets["wall"], (x * 30, y * 30))
                elif case == " ":
                    self.screen.blit(self.assets["background"], (x * 30, y * 30))
                elif case == "m":
                    self.screen.blit(self.assets["mc_gyver"], (x * 30, y * 30))
                elif case == "g":
                    self.screen.blit(self.assets["guardian"], (x * 30, y * 30))
                elif case == "a":
                    self.screen.blit(self.assets["needle"], (x * 30, y * 30))
                elif case == "b":
                    self.screen.blit(self.assets["syringe"], (x * 30, y * 30))
                elif case == "c":
                    self.screen.blit(self.assets["bottle_ether"], (x * 30, y * 30))
        pygame.display.flip()
