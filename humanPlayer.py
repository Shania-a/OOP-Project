from player import Player

class HumanPlayer(Player):
    """
    Human-controlled player.
    
        Inherits from:
            Player: Base player class that holds the game piece
    """
    def __init__(self, piece: str):
        """Create a human player.

        Args:
            piece (str): The symbol this player uses: "X" or "O".
        """
        super().__init__(piece)
        self.wins = 0 

    def make_move(self, board) -> int:
        """
        Ask the user for a move and return it as a board index.

        Expects the user to enter a number 1-9.

        Args:
            board: Board object with an available_moves() method.

        Returns:
            int: The chosen move index (0-8).
        """
        while True:
            user_input = input(f"Spelare {self.get_piece()}, välj ruta 1-9: ").strip()
            if user_input.isdigit():
                index = int(user_input) - 1
                if index in board.available_moves():
                    return index
            else:
                print("Ogiltigt val. Försök igen.")

    def __str__(self):
        """
        Return the players piece as its string representation.
        """
        return f"{self.get_piece()}"