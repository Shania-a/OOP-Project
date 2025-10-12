from player import Player

class HumanPlayer(Player):
    """Mänsklig spelare tar input från användaren."""
    def __init__(self, piece: str):
        super().__init__(piece)

    def make_move(self, board) -> int:
        while True:
            user_input = input(f"Spelare {self.get_piece()}, välj ruta 1-9: ").strip()
            if user_input.isdigit():
                index = int(user_input) - 1
                if index in board.available_moves():
                    return index
            else:
                print("Ogiltigt val. Försök igen.")

    def __str__(self):
        return f"{self.get_piece()}"