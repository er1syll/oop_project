class BattleSystem:
    def start_battle(self,player,enemy):
        while player.is_alive() and enemy.is_alive():
            player.attack(enemy)
            enemy.attack(player)
            print(player.hp)
            print(enemy.hp)
        if player.is_alive():
            print("Player wins")
        else:
            print("Enemy wins")

    def player_turn(self,player,enemy):
        player.attack(enemy)

    def enemy_turn(self,player,enemy):
        enemy.attack(player)

    def check_winner(self,player,enemy):
        return 'player' if player.is_alive() else 'enemy'

