from game import Game

class MenuSystem:
    """Boundary class that displays the menu, selects game mode and runs the game loop."""

    def __init__(self):
        """Initialize the menu system with no active Game instance."""
        self.game = None 
        

    def run(self) -> None:
        """
        Runs the menu loop.

        Shows the main menu until the user chooses to exit.
        Asks for a game mode, creates a Game instance
        and starts run_game() method to handle the gameplay loop.
        """
        while True:
            print("\n Tic-Tac-Toe! ")
            print("1) Starta Spel")
            print("2) Avsluta")
            choice = input("Val: ").strip()

            if choice == "1":
                selected_mode = self.game_mode()
                self.game = Game(mode=selected_mode)

                print(f"Spelläge satt till: {selected_mode}")
                self.run_game()

            elif choice == "2":
                print("Bye!")
                break

            else:
                print("Ogiltigt val. Ange 1, 2.")

    def game_mode(self) -> str:
        """
        Ask the user to choose a game mode.

        Returns:
            str: The selected option as a string, expected to be "1" or "2".
        """
        print("\n-- Välj spelläge --")
        print("1) Människa vs Människa")
        print("2) Människa vs Computer")
        while True:
            choice = input("Val: ").strip()
            if choice in ("1", "2"):
                return choice
            print("Ogiltigt val. Ange 1 eller 2.")

    def run_game(self) -> None:
        """
        Execute a playthrough using the current game instance.

        The method initializes the game, advances turns until a end-state is reached and then finalizes the session.

        Returns:
            None
         """
        game = self.game
        game.reset_game()
        print("\n-- Startar spelet --")

        while not game.is_over():
            game.print_board()
            print(f"Drag: {game.get_current_turn()}")
            game.play_turn()

        game.print_board()
        win = game.winner()
        if win:
            print(f"Vinnare: {win}")
        else:
            print("Oavgjort.")


if __name__ == "__main__":
    """Create and run the program"""
    menu = MenuSystem()
    menu.run()
