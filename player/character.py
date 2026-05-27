class Character:
    def __init__(self,name,hp,attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self,target):
        target.hp-=self.attack_power

    def take_damage(self,damage):
        self.hp-=damage

    def is_alive(self):
        return self.hp>0


player = Character("Knight", 100, 20)
enemy = Character("Goblin", 50, 10)

player.attack(enemy)

print(enemy.hp)

if enemy.is_alive():
    print("Enemy is alive")
else:
    print("Enemy is dead")