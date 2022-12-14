from Character import character
from random import randint

class Assassin(character):
    max_damage = 1

    def __init__(self, name, health=100, damage=1, defence=0):
        character.__init__(self, name, health, damage, defence)
        self.max_health = self.health


    def attack(self, target):
        rendom = randint(1,15)
        if rendom == 3:
            total_damage = 100
        else:
            return
        target.take_damage(total_damage)
