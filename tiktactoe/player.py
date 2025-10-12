from abc import ABC, abstractmethod 
from board import Board

class Player(ABC):

    def __init__(self, piece: str):
        self.piece = piece

    @abstractmethod
    def make_move() -> None:
        ...