from game import Game

class MenuSystem:
    """Boundary som visar meny, väljer spelläge och kör spelet."""

    def __init__(self):
        self.game = None 

    def run(self):
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
        Returnerar antingen: 1 eller 2 som sträng
        """

        print("\n-- Välj spelläge --")
        print("1) Människa vs Människa")
        print("2) Människa vs Computer")
        while True:
            choice = input("Val: ").strip()
            if choice == "1" or "2":
                return choice
            print("Ogiltigt val. Ange 1 eller 2.")

    def run_game(self):
        """
        Kör spelet tills det är över.
        Matchar Game-API vi byggt:
          - reset_game()
          - print_board()
          - play_turn()
          - is_over()
          - winner()
          - get_current_turn()
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
    menu = MenuSystem()
    menu.run()
