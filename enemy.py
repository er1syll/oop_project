from player.character import Character

class Enemy(Character):
    def __init__(self,name,hp,attack_power):
        super().__init__(name,hp,attack_power)