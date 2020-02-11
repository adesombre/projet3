# fonction  affichage du labyrhinte
def charge_labyrinthe():
    labyrinthe = open("map.txt")# Ici, ouvrir le fichier

    # affiche labyrinthe
def affiche_labyrinthe():
    labyrinthe = open("map.txt")
    for ligne in labyrinthe.readlines():
        print(ligne)


# programme principal
charge_labyrinthe()
affiche_labyrinthe()
