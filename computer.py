import random
from player import Player

class Computer(Player):
    """
    Computer controlled player
    Chooses a random free spot on the board

        Inherits from:
            Player: Base player class that holds the game piece
    """
    def __init__(self, piece: str):
        """
        Initialize a computer player

        Args:
            piece (str): The symbol inherited player uses on the board: "X" or "O"
        """
        super().__init__(piece)
        self.wins = 0 

    def make_move(self, board) -> int:
        """
        Select and return a random legal move.

        The method checks the board for all currently available moves and
        returns one of them at random.

        Args:
            board: An object representing the game board 

        Returns:
            int: The chosen move position.

        Raises:
            RuntimeError: If there are no legal moves remaining.
        """
        try:
            moves = board.available_moves()
            return random.choice(moves)
        except (IndexError, RuntimeError):
            print("Inga lediga drag kvar för AI.")
            return None
