class MenuSystem:
    """
    <<Boundary>> MenuSystem
    - game: Game (objekt som har metoderna set_mode, start, is_over, step)
    """

    def __init__(self, game):
        self.game = game

    def run(self):
        while True:
            print("\n=== Game Menu ===")
            print("1) Välj spelläge")
            print("2) Starta spel")
            print("3) Avsluta")
            choice = input("Val: ").strip()

            if choice == "1":
                mode = self.game_mode()
                self.game.set_mode(mode)
                print(f"> Spelläge satt till: {mode}")
            elif choice == "2":
                self.run_game()
            elif choice == "3":
                print("Hejdå!")
                break
            else:
                print("Ogiltigt val. Ange 1, 2 eller 3.")

    def game_mode(self):
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
        Antaganden om game-API:
          - start() -> None
          - is_over() -> bool
          - step() -> None
        """
        print("\n-- Startar spelet --")
        self.game.start()
        while not self.game.is_over():
            self.game.step()
        print("-- Spelet slut --")


# När din riktiga Game är klar:
# from mygame import MyGame
# if __name__ == "__main__":
#     menu = MenuSystem(MyGame())
#     menu.run()
