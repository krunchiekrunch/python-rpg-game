import time
import random
# import pygame

class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.hp -= max(damage - self.defense, 0)

    def is_alive(self):
        return self.hp > 0

# make player and enemy (also set default hp and attack option count)
player = Character("You", 100, 10, 5)
enemy = Character("Blob", 100, 8, 3)

def attack(attacker, defender):
    damage = random.randint(attacker.attack - 2, attacker.attack + 2)
    defender.take_damage(damage)
    print(f"{attacker.name} attacks {defender.name} for {damage} damage!")

def defend(defender):
    print(f"{defender.name} defends.")

def special_attack(attacker, defender):
    damage = random.randint(attacker.attack * 2, attacker.attack * 3)
    defender.take_damage(damage)
    print(f"{attacker.name} uses a special attack on {defender.name} for {damage} damage!")

def heal(healer):
    heal_amount = random.randint(5, 10)
    healer.hp += heal_amount
    print(f"{healer.name} heals for {heal_amount} HP.")

start_time = time.time()
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time >= 300:
        print("Time's up!")
        break

    print("#####################################")

    print(f"Your HP: {player.hp}")
    print(f"Blob's HP: {enemy.hp}")

    actions = ["attack", "defend"]
    if player.hp <= 50:
        actions.append("heal")
    if random.random() < 0.3:  # 30% chance to give special attack, set to 1 to make it 100%
        actions.append("special attack")

    print(f"You can choose: {', '.join(actions)}")
    action = input("Choose your action: ")

    if action == "attack":
        attack(player, enemy)
        if not enemy.is_alive():
            print("""
            You defeated the blob!
            Thank you for playing!
            """)
            break
        attack(enemy, player)
        if not player.is_alive():
            print("""
            You were defeated by the blob...
            Thank you for playing!
            """)
            break

    elif action == "defend":
        defend(player)
        attack(enemy, player)
        if not player.is_alive():
            print("""
            You were defeated by the blob...
            Thank you for playing!
            """)
            break

    elif action == "special attack":
        special_attack(player, enemy)
        if not enemy.is_alive():
            print("""
            You defeated the blob!
            Thank you for playing!
            """)
            break
        attack(enemy, player)
        if not player.is_alive():
            print("""
            You were defeated by the blob...
            Thank you for playing!
            """)
            break

    elif action == "heal":
        heal(player)
        attack(enemy, player)
        if not player.is_alive():
            print("""
            You were defeated by the blob...
            Thank you for playing!
            """)
            break

    else:
        print("Unknown option, Please try again.")
