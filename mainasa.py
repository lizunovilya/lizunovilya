from Character import character
from assassin import Assassin

player1 = character('Vasya', health=100, damage=1)
player2 = Assassin('Petya', health=50, damage=2)


print(player1)
print(player2)


while player1.health > 0 and player2.health:
    player1.attack(player2)
    player2.attack(player1)
    Character_damage = player1.damage
    Assassin_damage = player2.damage

    print(f'{player1.name} нанес {Character_damage} урона ')
    print(f'{player2.name} нанес {Assassin_damage} урона ')
    print(player1)
    print(player2)