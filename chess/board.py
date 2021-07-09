from chess.constants import BASE_FEN
from utils.logger import Logger
from chess.constants import BASE_FEN


class Board(object):
    def __init__(self, fen=BASE_FEN):
        self.logger = Logger("chess/board")

        self.logger.log_neutral(f"Creating a board with fen string <{fen}>.")
        
        self.fen = fen
        self.setup()

    def setup(self):
        pass