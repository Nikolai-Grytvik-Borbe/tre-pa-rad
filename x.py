import pygame
from piece import Piece

class X(Piece):
    def __init__(self, pos, player, board):
        super().__init__(pos, player, board)

        img_path = "img/x.png"
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(
            self.img, (board.tile_width, board.tile_height)
        )

        self.notation = "X"
