def display_labyrinthe(labyrinthe):
    for y, line in enumerate(labyrinthe):
        for x, case in enumerate(line):
            if case == "#":
                screen.blit(w, (x * 30, y * 30))
            elif case == " ":
                screen.blit(f, (x * 30, y * 30))
            elif case == "m":
                screen.blit(m, (x * 30, y * 30))
            screen.blit(g, (1 * 30, 1 * 30))
    objet(labyrinthe)
    screen.blit(a, (x, y))
    pygame.display.flip()

