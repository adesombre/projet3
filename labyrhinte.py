# fonction  affichage du labyrhinte
labyrinthe = open("map.txt")# Ici, ouvrir le fichier

    # affiche labyrinthe
def affiche_labyrinthe():
    labyrinthe = open("map.txt")
    for ligne in labyrinthe.readlines():
        print(ligne)
    labyrinthe.close()


# programme principal

affiche_labyrinthe()
