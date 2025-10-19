from board import Board
from humanPlayer import HumanPlayer
from computer import Computer

class Game:
    """
    A game between two players on a Board
    Uses private fields with getter/setter methods.
    """
    def __init__(self, mode: str = "1" or "2"):
        """
        Create a new game.

        Args:
            mode (str): Game mode.
                - "1": human vs human
                - "2": computer (X) vs human (O)

        Raises:
            ValueError: If the mode is not supported.
        """
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
        """Return the game board."""
        return self.__board

    def get_current_turn(self) -> str:
        """Return whose turn it is: 'X' or 'O'."""
        return self.__current_turn

    def set_current_turn(self, turn: str) -> None:
        """Set whose turn it is.

        Args:
            turn (str): 'X' or 'O'.
        """
        self.__current_turn = turn

    def get_x_player(self) -> str:
        """Return the X player instance."""
        return self.__x_player

    def get_o_player(self) -> str:
        """Return the O player instance."""
        return self.__o_player

    def __current_player(self) -> str:
        """Return the player whose turn it is."""
        return self.__x_player if self.__current_turn == "X" else self.__o_player

    def play_turn(self) -> None:
        """Play a single turn.

        Asks the current player for a move until a legal move is made, places the piece on the board and switches turn unless the game is over.
        """
        player = self.__current_player()
        while True:
            selected_index = player.make_move(self.__board)
            if self.__board.place(selected_index, player.get_piece()):
                break
            print("Rutan är upptagen. Välj en annan.")
        if not self.is_over():
            self.__current_turn = "O" if self.__current_turn == "X" else "X"

    def is_over(self) -> bool:
        """Return True if the game has ended."""
        return self.__board.game_end()

    def winner(self) -> str:
        """Return the winner: "X" or "O" """
        return self.__board.winner()

    def print_board(self) -> None:
        """Print the board."""
        print(str(self.__board))

    def reset_game(self) -> None:
        """Reset the board and set the turn back to 'X'."""
        self.__board.reset_board()
        self.__current_turn = "X"
