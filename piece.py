import pygame

class Piece:
	def __init__(self, pos, player, board):
		self.pos = pos
		self.x = pos[0]
		self.y = pos[1]
		self.player = player

