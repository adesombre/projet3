objet = ['a', 'b', 'c']
ox = random.randint(0,15)
labyrinthe=[' ',' ','#',' ']
for o in objet:
   if labyrinthe[ox] != '#':
        labyrinthe[ox] = o