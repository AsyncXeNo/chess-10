from utils.logger import Logger
from chess.pieces.piece import Piece
from chess.square import Square


class King(Piece):
    def __init__(self, color: int, square: Square, moved: bool=False):
        self.logger = Logger("chess/pieces/king")
        super().__init__(color, square)

        self.moved = False

        self.symbol = "k"
        self.range = 1

        self.offsets = [
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1)
        ]

    def can_castle(self):
        return not self.moved

    def can_move_to(self):
        positions = []

        for offset in self.offsets:
            pos = self.get_square().get_position()
            for _ in range(self.range):
                pos += offset
                if not (pos[0] > 8 or pos[1] > 8 or pos[0] < 1 or pos[1] < 1):
                    positions.append(pos)
        
        
        positions = [self.get_board().get_square_by_pos(pos[0], pos[1]) for pos in positions]
        return positions

    def can_move_to_special(self):
        if self.can_castle():
            pass

    def can_move_to_legally(self, square:Square):
        enemy_pieces = self.board.get_pieces(self.get_opposite_color())
        ally_pieces = self.board.get_pieces(self.get_color())
        for piece in enemy_pieces:
            if square in piece.can_move_to():
                return False
        for piece in ally_pieces:
            if piece.get_square().get_position() == square.get_position():
                return False

        return True

    def move(self, square:Square):
        self.moved = True
        if self.can_move_to_legally(square):
            self.square.clear()
            square.set_piece(self)
        else:
            self.logger.log_error(f"King at position {self.square.get_position_str()} cannot move to square {square.get_position_str()}.")
            raise Exception(f"King at position {self.square.get_position_str()} cannot move to square {square.get_position_str()}.")
        
        