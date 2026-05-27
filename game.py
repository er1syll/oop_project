from player.warrior import Warrior
from player.mage import Mage
from enemy import Enemy
from battle import BattleSystem


class Game:

    def main_menu(self):

        print("=== MAIN MENU ===")
        print("1. Start Game")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            self.start_game()

        elif choice == "2":
            print("Goodbye!")

    def choose_character(self):

        print("Choose your character:")
        print("1. Warrior")
        print("2. Mage")

        choice = input("Enter choice: ")

        if choice == "1":
            return Warrior("Knight")

        elif choice == "2":
            return Mage("Merlin")

    def start_game(self):

        print("=== RPG Battle Game ===")

        player = self.choose_character()

        enemy = Enemy("Goblin", 50, 10)

        battle = BattleSystem()

        battle.start_battle(player, enemy)


game = Game()
game.start_game()
