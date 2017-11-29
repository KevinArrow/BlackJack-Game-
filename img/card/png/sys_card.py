import pygame
pygame.init()

num = 0

class DefaultCard:
	def __str__(self):
		self.joker = 'x01.png'
		return "%s" %(self.joker)