class Board:
    """Kontrollerar brädets tillstånd och regler för tre-i-rad (3x3)."""

    def __init__(self):
        self.__cells = [""] * 9

    def get_cells(self) -> tuple[str, ...]:
        """Returnerar en oföränderlig vy av cellerna (mutera inte externt)."""
        return tuple(self.__cells)

    def set_cell(self, index: int, piece: str) -> None:
        """(Sällan behövd) Sätter en cell direkt, utan validering av regler."""
        if 0 <= index < 9:
            self.__cells[index] = piece
        else:
            raise IndexError("index måste vara 0..8")

    def reset_board(self) -> None:
        self.__cells = [""] * 9

    def place(self, index: int, piece: str) -> bool:
        if 0 <= index < 9 and self.__cells[index] == "":
            self.__cells[index] = piece
            return True
        return False

    def available_moves(self) -> list[int]: 
        return [index for index, cell in enumerate(self.__cells) if cell == ""]

    def is_full(self) -> bool:
        return all(cell != "" for cell in self.__cells)

    def winner(self) -> str:
        lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)             
        ]
        for a, b, c in lines:
            if self.__cells[a] and self.__cells[a] == self.__cells[b] == self.__cells[c]:
                return self.__cells[a]
        return ""

    def game_end(self) -> bool:
        return self.winner() != "" or self.is_full()

    def __str__(self) -> str:
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
