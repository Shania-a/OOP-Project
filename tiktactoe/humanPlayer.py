from abc import ABC, abstractmethod
from player import Player

class HumanPlayer(Player):
    def __init__(self):
        pass

    def make_move(self):
        return "Human Test"
