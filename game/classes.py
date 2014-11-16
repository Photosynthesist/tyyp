#No classes yet.
#ALSO WRONG!

import pygame
from constants import *

'''
Button class.
So far, it only draws a rectangle of specified dimensions to the screen.
It will later on be made to respond to clicking.

To create a Button:
but1 = Button()
but1.init((top_left_X,top_left_Y),(bottom_right_X,bottom_right_Y))

'''
class Button():
	def init(self,tl,br):
		print(tl,br)
		self.tl = tl
		self.br = br
		self.width = br[0] - tl[0]
		self.height = br[1] - tl[1]
	def draw(self,screen):
		pygame.draw.rect(screen,GREY,(self.tl[0],self.tl[1],self.width,self.height))