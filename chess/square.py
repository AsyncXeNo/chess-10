from utils.logger import Logger
from chess.constants import FILE
from chess.board import Board


class Square(object):
    def __init__(self, file:int, rank:int, board:Board):
        self.logger = Logger("chess/square")

        self.file = file
        self.rank = rank
        self.board = board

        self.piece = None

    def get_position(self):
        return (self.file, self.rank)

    def get_position_str(self):
        return f"{FILE[self.file]}{self.rank}"
    
    def get_piece(self):
        return self.piece

    def set_piece(self, piece):
        self.piece = piece
        piece.set_board(self.board)

    def clear(self):
        self.piece = None