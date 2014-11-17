#No classes yet.
#ALSO WRONG!

import pygame
from constants import *

'''
Button class.
So far, it only draws a rectangle of specified dimensions to the screen.
It will later on be made to respond to clicking.

To create a Button:
but1 = Button((top_left_X,top_left_Y),(bottom_right_X,bottom_right_Y))

'''
class Button():
	def __init__(self,tl,br):
		print(tl,br)
		self.tl = tl
		self.br = br
		self.width = br[0] - tl[0]
		self.height = br[1] - tl[1]
		self.rectangle = (self.tl[0],self.tl[1],self.width,self.height)
	def draw(self,screen):
		pygame.draw.rect(screen,GREY,self.rectangle)
		#pygame.draw.rect(self.rect)
			