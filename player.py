from abc import ABC, abstractmethod

class Player(ABC):
    """Abstrakt bas-entity för spelare med privat pjäs ('X' eller 'O')."""

    def __init__(self, piece: str):
        self.set_piece(piece)   # settern skapar self.__piece direkt

    # --- getters/setters ---
    def get_piece(self) -> str:
        return self.__piece

    def set_piece(self, value: str) -> None:
        if value not in ("X", "O"):
            raise ValueError("piece måste vara 'X' eller 'O'")
        self.__piece = value

    # --- abstrakt spelgränssnitt ---
    @abstractmethod
    def make_move(self, board) -> int:
        """
        Ska returnera ett index (0..8) där spelaren vill spela.
        Abstrakt: måste implementeras i subklass.
        """
        pass

