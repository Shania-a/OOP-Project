from abc import ABC, abstractmethod

class Player(ABC):
    """
    Abstract base class for players with a private piece: "X" or "O".
    """

    def __init__(self, piece: str):
        """Create a player with the given piece."""
        self.set_piece(piece) 

    def get_piece(self) -> str:
        """Return the players piece."""
        return self.__piece

    def set_piece(self, value: str) -> None:
        """Set the players piece."""
        self.__piece = value

    @abstractmethod
    def make_move(self, board) -> int:
        """
        Returns a indxed from 0-8 where the player wants to place their piece.
        Abstract: implemented in subclass.
        """
        pass

