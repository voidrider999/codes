import random

class Player:
    def __init__(self, name, strong):
        self.name = name
        self.hp = 10
        self.strength = strong

    def hit(self):
        self.hp -= 1

    def powerup(self, n):
        self.strength += n

    def eat(self, food):
        if food == 'apple':
            self.hp += 5
        elif food == 'cheese':
            self.hp += 10
        elif food == 'mushroom':
            self.hp -= 5
        else:
            self.hp += 1

    def fight(self, other):
        self.hp -= other.strength
        other.hp -= self.strength
    
    def random_fight(self, other):
        self_hits = random.randint(0, other.strength)
        self.hp -= self_hits

        other_hits = random.randint(0, self.strength)
        other.hp -= other_hits

    def is_dead(self):
        return self.hp <= 0

player1 = Player('bob', 1)
player2 = Player('jay', 2)

player1.hit()
player1.powerup(10)
print(player1.name, player1.hp, player1.strength)

player2.hit()
player2.hit()
player2.eat('cheese')
print(player2.name, player2.hp)

player1.fight(player2)
print(player1.hp, player2.hp)

player1.random_fight(player2)
print(f'{player1.name} is dead({player1.hp}): {player1.is_dead()}')
print(f'{player2.name} is dead({player2.hp}): {player2.is_dead()}')
