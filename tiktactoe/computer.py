from abc import ABC, abstractmethod
from player import Player

class Computer(Player):

    def __init__(self):
        pass

    def make_move(self):
        return "Computer test"