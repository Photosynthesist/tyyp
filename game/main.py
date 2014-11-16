#IMPORTING
import pygame	#Importing libraries
from pygame.locals import *
from constants import * #Importing our own files
from classes import *
from functions import *
pygame.init()

#VARIABLES
clock = pygame.time.Clock()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
done = False

print(width,height,sep=" ")
'''
clock:			Abbreviation
width, height:	Use pygame.display.Info() to grab native resolution.
done:			Used to loop main program loop.
'''

#INITIATION
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Tyyp")

#MAIN PROGRAM LOOP
while not done:
	#Event grabber
	for event in pygame.event.get():
		if event.type == pygame.QUIT:	#Close button
			done = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				done = True
	
	#Game Logic
	
	#Drawing Code
	Screen.draw(screen)
	pygame.display.flip()
	clock.tick(FRAMERATE)
	
pygame.quit()