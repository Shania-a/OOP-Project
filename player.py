from abc import ABC, abstractmethod

class Player(ABC):
    """
    Abstract base class for players with a private piece: "X" or "O".
    """

    def __init__(self, piece: str):
        """Create a player with the given piece."""
        self.__piece = piece.upper() 

    def get_piece(self) -> str:
        """Return the players piece."""
        return self.__piece

    @abstractmethod
    def make_move(self, board) -> int:
        """
        Returns an index from 0-8 where the player wants to place their piece.
        Abstract: implemented in subclass.
        """
        pass

