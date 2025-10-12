# menuSystem.py
from game import Game

class MenuSystem:
    """Boundary som visar meny, väljer spelläge och kör spelet."""

    def __init__(self):
        self.game = None  # sätts efter att användaren valt läge

    def run(self):
        while True:
            print("\n=== Game Menu ===")
            print("1) Starta Spel")
            print("2) Avsluta")
            choice = input("Val: ").strip()

            if choice == "1":
                mode = self.game_mode()
                self.game = Game(mode=mode)
                print(f"> Spelläge satt till: {mode}")
                self.run_game()

            elif choice == "2":
                print("Hejdå!")
                break

            else:
                print("Ogiltigt val. Ange 1, 2.")

    def game_mode(self) -> str:
        """
        Returnerar antingen:
          - 'human-vs-human'
          - 'human-vs-ai'
        """
        modes = {"1": "human-vs-human", "2": "human-vs-ai"}

        print("\n-- Välj spelläge --")
        print("1) Människa vs Människa")
        print("2) Människa vs AI")

        while True:
            choice = input("Val: ").strip()
            if choice in modes:
                return modes[choice]
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
          - get_current_turn(), moves_str()
        """
        g = self.game
        g.reset_game()
        print("\n-- Startar spelet --")

        while not g.is_over():
            g.print_board()
            print(f"Drag: {g.get_current_turn()}")
            g.play_turn()

        g.print_board()
        w = g.winner()
        if w:
            print(f"Vinnare: {w}")
        else:
            print("Oavgjort.")


if __name__ == "__main__":
    menu = MenuSystem()
    menu.run()
