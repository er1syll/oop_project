from player.character import Character

class Warrior(Character):
    def __init__(self,name):
        super().__init__(name,120,25)