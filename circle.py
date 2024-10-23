import pygame
from piece import Piece

class Circle(Piece):
    def __init__(self, pos, player, board):
        super().__init__(pos, player, board)

        img_path = "img/circle.png"
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(
            self.img, (board.tile_width, board.tile_height)
        )

        self.notation = "C"
