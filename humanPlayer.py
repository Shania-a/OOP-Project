from player import Player

class HumanPlayer(Player):
    """Mänsklig spelare – tar input från användaren."""
    def __init__(self, piece: str):
        super().__init__(piece)

    def make_move(self, board) -> int:
        while True:
            raw = input(f"Spelare {self.get_piece()}, välj ruta 1-9: ").strip()
            if raw.isdigit():
                idx = int(raw) - 1
                if idx in board.available_moves(type="human"):
                    return idx
            print("Ogiltigt val. Försök igen.")

    def __str__(self):
        return f"{self.get_piece()}"