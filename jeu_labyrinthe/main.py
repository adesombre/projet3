import pygame
from pygame.locals import*

pygame.init()
size=x,y=640,480
xm,ym=0,0
xg,yg=100,100
screen=pygame.display.set_mode(size)
bg=pygame.image.load('structures.png')
bg1=pygame.transform.scale(bg,(x,y))
mac=pygame.image.load('macGyver.png')
gardien=pygame.image.load('Gardien.png')


continuer=True
while continuer:
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			continuer= False
		elif event.type ==KEYDOWN and event.key ==K_a :
			xm=xm+5
		elif event.type ==KEYDOWN and event.key ==K_q :
			xm=xm-5
		elif event.type ==KEYDOWN and event.key ==K_z :
			ym=ym+5
		elif event.type ==KEYDOWN and event.key ==K_s :
			ym=ym-5
	screen.blit( bg1,(0,0))

	screen.blit(mac,(xm,ym))
	screen.blit(gardien,(xg,yg))
	
	xg+=1


	pygame.display.flip()