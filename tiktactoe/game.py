# game.py
from board import Board
from humanPlayer import HumanPlayer
from computer import Computer

class Game:
    """
    Privata fält + getters/setters (inga @property).
    """

    def __init__(self, mode: str = "human-vs-ai"):
        self.__board = Board()
        if mode == "human-vs-human":
            self.__x_player = HumanPlayer("X")
            self.__o_player = HumanPlayer("O")
        elif mode == "human-vs-ai":
            self.__x_player = HumanPlayer("X")
            self.__o_player = Computer("O")
        else:
            raise ValueError("Endast 'human-vs-human' eller 'human-vs-ai' stöds.")
        self.__current_turn = "X"
        self.__moves: list[tuple[str, int]] = []

    # --- getters/setters ---
    def get_board(self) -> Board:
        return self.__board

    def get_moves(self) -> list[tuple[str, int]]:
        return self.__moves

    def get_current_turn(self) -> str:
        return self.__current_turn

    def set_current_turn(self, turn: str) -> None:
        if turn not in ("X", "O"):
            raise ValueError("turn måste vara 'X' eller 'O'")
        self.__current_turn = turn

    def get_x_player(self):
        return self.__x_player

    def get_o_player(self):
        return self.__o_player

    # --- intern hjälp ---
    def __current_player(self):
        return self.__x_player if self.__current_turn == "X" else self.__o_player

    # --- publikt spel-API ---
    def play_turn(self) -> None:
        player = self.__current_player()
        while True:
            idx = player.make_move(self.__board)
            if self.__board.place(idx, player.get_piece()):
                self.__moves.append((player.get_piece(), idx))
                break
            print("Rutan är upptagen. Välj en annan.")
        if not self.is_over():
            self.__current_turn = "O" if self.__current_turn == "X" else "X"

    def is_over(self) -> bool:
        return self.__board.game_end()

    def winner(self) -> str:
        w = self.__board.winner()
        return w if w else ""

    def print_board(self) -> str:
        s = str(self.__board)
        print(s)
        return s

    def moves_str(self) -> str:
        if not self.__moves:
            return "(inga drag ännu)"
        return ", ".join(f"{p}:{i+1}" for p, i in self.__moves)

    def reset_game(self) -> None:
        self.__board.reset_board()
        self.__current_turn = "X"
        self.__moves.clear()
