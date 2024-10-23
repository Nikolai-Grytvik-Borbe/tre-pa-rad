import pygame

from square import Square
from x import X
from circle import Circle


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile_width = width // 3
        self.tile_height = height // 3
        self.selected_piece = None
        self.turn = "X"

        self.game = [["", "", ""], ["", "", ""], ["", "", ""]]

        self.squares = self.generate_squares()

    def checkif_more_moves(self):
        for i in self.game:
            for j in i:
                if j == "":
                    return True
        return False
    
    def update_square(row, column, player):
        """player should either be "X" or "C" """
        self.game[row][column] = player

    def has_tre_pa_rad(self, player):
        # horizontal check
        for i in self.game:
            if i[0] == i[1] and i[1] == i[2]:
                if i[0] == player:
                    return True
        # vertical check
        for col in range(len(self.game)):
            if all(row[col] == self.game[0][col] for row in self.game):
                if self.game[0][col] == player:
                    return True
        # perpendicular check
        if self.game[0][0] == self.game[1][1] and self.game[0][0] == self.game[2][2]:
            if self.game[0][0] == player:
                return True
        elif self.game[2][2] == self.game[1][1] and self.game[2][2] == self.game[0][0]:
            if self.game[0][0] == player:
                return True
        return False

    def generate_squares(self):
        output = []
        for y in range(3):
            for x in range(3):
                output.append(Square(x, y, self.tile_width, self.tile_height))
        return output

    def get_square_from_pos(self, pos):
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square

    def handle_click(self, mx, my):
        x = mx // self.tile_width
        y = my // self.tile_height
        clicked_square = self.get_square_from_pos((x, y))

        if clicked_square.occupying_piece != None:
            return 0
        elif clicked_square.occupying_piece == None:
            if self.turn == "C":
                clicked_square.occupying_piece = Circle((x, y), "C", self)
                self.game[y][x] = "C"
                self.turn = "X"
            elif self.turn == "X":
                clicked_square.occupying_piece = X((x, y), "X", self)
                self.game[y][x] = "X"
                self.turn = "C"


    def draw(self, display):
        for square in self.squares:
            square.draw(display)

