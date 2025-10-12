from board import Board
from humanPlayer import HumanPlayer
from computer import Computer

class Game:
    """
    Privata fält + getters/setters.
    """

    def __init__(self, mode: str = "1" or "2"):
        self.__board = Board()
        if mode == "1":
            self.__x_player = HumanPlayer("X")
            self.__o_player = HumanPlayer("O")
        elif mode == "2":
            self.__x_player = Computer("X")
            self.__o_player = HumanPlayer("O")
        else:
            raise ValueError("Endast 'human vs human' eller 'human vs computer' stöds.")
        self.__current_turn = "X"

    def get_board(self) -> Board:
        return self.__board

    def get_current_turn(self) -> str:
        return self.__current_turn

    def set_current_turn(self, turn: str) -> None:
        self.__current_turn = turn

    def get_x_player(self) -> str:
        return self.__x_player

    def get_o_player(self) -> str:
        return self.__o_player

    def __current_player(self) -> str:
        return self.__x_player if self.__current_turn == "X" else self.__o_player

    def play_turn(self) -> None:
        player = self.__current_player()
        while True:
            selected_index = player.make_move(self.__board)
            if self.__board.place(selected_index, player.get_piece()):
                break
            print("Rutan är upptagen. Välj en annan.")
        if not self.is_over():
            self.__current_turn = "O" if self.__current_turn == "X" else "X"

    def is_over(self) -> bool:
        return self.__board.game_end()

    def winner(self) -> str:
        return self.__board.winner()

    def print_board(self) -> None:
        print(str(self.__board))

    def reset_game(self) -> None:
        self.__board.reset_board()
        self.__current_turn = "X"
