import random
from player import Player

class Computer(Player):
    """Datorspelare väljer ett slumpmässigt ledigt drag."""
    def __init__(self, piece: str):
        super().__init__(piece)

    def make_move(self, board) -> int:
        moves = board.available_moves()
        if not moves:
            raise RuntimeError("Inga lediga drag kvar för AI.")
        return random.choice(moves)
