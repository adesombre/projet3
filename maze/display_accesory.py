import pygame


class Accessory:
    def init(self, mc_giver, guardian, ):
        """ list characters and accessory more initialization
        """
        pygame.init()
        size = (15 * 30, 15 * 30)
        screen = pygame.display.set_mode(size)
        self.wall = pygame.image.load('ressource/mur.png').convert_alpha()
        fond = pygame.image.load('ressource/fond.jpg').convert_alpha()
        self.mc_gyver = pygame.image.load('ressource/macGyver.png').convert_alpha()
        self.mc_gyver = pygame.transform.scale(self.mc_gyver, (30, 30))
        self.guardian = pygame.image.load('ressource/Gardien.png').convert_alpha()
        self.guardian = pygame.transform.scale(self.guardian, (30, 30))
        self.needle = pygame.image.load('ressource/aiguille.png').convert_alpha()
        self.needle = pygame.transform.scale(self.needle, (30, 30))
        self.syringe = pygame.image.load('ressource/seringue.png').convert_alpha()
        self.syringe = pygame.transform.scale(self.syringe, (30, 30))
        self.bottle_ether = pygame.image.load('ressource/ether.png').convert_alpha()
        self.bottle_ether = pygame.transform.scale(self.bottle_ether, (30, 30))


class Display:
    def display_labyrinthe(elf, labyrinthe):
        print(labyrinthe)
        for y, line in enumerate(labyrinthe):
            for x, case in enumerate(line):
                if case == "#":
                    Accessory.screen.blit(Accessory.wall, (x * 30, y * 30))
                elif case == " ":
                    Accessory.screen.blit(Accessory.fond, (x * 30, y * 30))
                elif case == "m":
                    Accessory.screen.blit(Accessory.mc_gyver, (x * 30, y * 30))
                elif case == "g":
                    Accessory.screen.blit(Accessory.guardian, (x * 30, y * 30))
                elif case == "a":
                    Accessory.screen.blit(Accessory.needle, (x * 30, y * 30))
                elif case == "b":
                    Accessory.screen.blit(Accessory.syringe, (x * 30, y * 30))
                elif case == "c":
                    Accessory.screen.blit(Accessory.bottle_ether, (x * 30, y * 30))
        pygame.display.flip()
