# fonction  affichage du labyrhinte

# programme principal



def load_labyrinthe():
	lab=[]
	with open("map.txt") as file:
		for ligne in file:
			lab_line=[]
			for char in ligne:
				if char != '\n':
					lab_line.append(char)
			lab.append(lab_line)
	return lab		

def display_labyrinthe(labyrinthe): 
	for line in labyrinthe:
		
		print("".join(line))

def main():
	labyrinthe=load_labyrinthe()
	while True:
		display_labyrinthe(labyrinthe)
		user_input=input("appuyer sur un touche!")
		labyrinthe.append(user_input)
		print(labyrinthe)
        

                              

main()		




