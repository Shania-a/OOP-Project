import random
from player import Player

class Computer(Player):
    """Dator-spelare – väljer ett slumpmässigt ledigt drag."""
    def __init__(self, piece: str):
        super().__init__(piece)

    def make_move(self, board) -> int:
        moves = board.available_moves(type="ai")
        if not moves:
            # Borde inte hända om Game kollar is_over() korrekt,
            # men vi skyddar oss ändå:
            raise RuntimeError("Inga lediga drag kvar för AI.")
        return random.choice(moves)
