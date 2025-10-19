class Board:
    """Encapsulates the Tic Tac Toe board state and rule checks."""

    def __init__(self):
        """Initialize an empty 3x3 board represented as 9 string cells."""
        self.__cells = [""] * 9

    def get_cells(self) -> tuple[str, ...]:
        """
        Return an view of the current board cells.

        Returns:
            tuple[str, ...]: A 9-item tuple with values "", "X" or "O".
        """
        return tuple(self.__cells)

    def set_cell(self, index: int, piece: str) -> None:
        """
        Directly set a cell value without rule validation.

        Args:
            index (int): Cell index in range 0 - 8.
            piece (str): Typically "X" or "O", or "" to clear.

        Raises:
            IndexError: If index is outside 0 - 8.
        """
        if 0 <= index < 9:
            self.__cells[index] = piece
        else:
            raise IndexError("index must be 0 - 8")

    def reset_board(self) -> None:
        """Clear the board to its initial empty state."""
        self.__cells = [""] * 9

    def place(self, index: int, piece: str) -> bool:
        """
        Place a piece on the board if the move is valid.

        Args:
            index (int): Cell index in range 0 - 8.
            piece (str): Usually "X" or "O".

        Returns:
            bool: True if the move was applied; False if the cell was occupied
                  or the index was out of range.
        """
        if 0 <= index < 9 and self.__cells[index] == "":
            self.__cells[index] = piece
            return True
        return False

    def available_moves(self) -> list[int]:
        """
        List indexes that are currently empty.

        Returns:
            list[int]: Zero-based indexes for all playable cells.
        """
        return [index for index, cell in enumerate(self.__cells) if cell == ""]

    def is_full(self) -> bool:
        """
        Check if the board has no empty cells.

        Returns:
            bool: True if all cells are filled; otherwise False.
        """
        return all(cell != "" for cell in self.__cells)

    def winner(self) -> str:
        """
        Determine the current winner if any.

        Returns:
            str: "X" or "O" if there is a winning line, otherwise "".
        """
        lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for a, b, c in lines:
            if self.__cells[a] and self.__cells[a] == self.__cells[b] == self.__cells[c]:
                return self.__cells[a]
        return ""

    def game_end(self) -> bool:
        """
        Check if the game is over.

        Returns:
            bool: True if someone has won or the board is full, else False.
        """
        return self.winner() != "" or self.is_full()

    def __str__(self) -> str:
        """
        Render a human-readable board.

        Empty cells are shown as their show position: 1 - 9.
        Filled cells show "X" or "O".

        Returns:
            str: A multi-line string depicting the board.
        """
        def valjue(index): 
            return self.__cells[index] if self.__cells[index] else str(index + 1)

        rows = [
            f" {valjue(0)} | {valjue(1)} | {valjue(2)} ",
            "---+---+---",
            f" {valjue(3)} | {valjue(4)} | {valjue(5)} ",
            "---+---+---",
            f" {valjue(6)} | {valjue(7)} | {valjue(8)} ",
        ]
        return "\n".join(rows)
