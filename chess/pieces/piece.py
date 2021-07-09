from utils.logger import Logger
from chess.square import Square
from chess.board import Board


class Piece(object):
    def __init__(self, color:int, square:Square):
        self.logger = Logger("chess/pieces/piece")

        self.color = color
        self.square = square
        self.board = None

        self.validate()

    def validate(self):
        if self.color < 0 or self.color > 1 or type(self.color) != int:
            self.logger.log_error("Invalid color.")
            raise Exception("Invalid color.")

    def get_color(self):
        return self.color

    def get_opposite_color(self):
        return 0 if self.color == 1 else 1

    def get_color_str(self):
        return "WHITE" if self.color == 1 else "BLACK"

    def get_board(self):
        return self.board

    def set_board(self, board:Board):
        self.board = board

    def get_square(self):
        return self.square