from os import write
from random import randint
from utilities import *
from equipement import *


class Ennemy:
    def __init__(self, health, mana, atk, flee, armor, weapon, potions, spells, level, strength):
        self.maxHealth = health
        self.health = health
        self.maxMana = mana
        self.mana = mana
        self.armor = armor
        self.weapon = weapon
        self.potions = potions
        self.spells = spells
        self.level = level
        self.atk = atk
        self.flee = flee
        self.strength = strength

    def calculateDamage(self):  # Calculate attack damage
        if self.weapon.durability > 0:
            damage = self.weapon.damage + randint(1, 5) * self.strength
            self.weapon.durability = max(self.weapon.durability - damage, 0)
        else:
            damage = randint(1, 5) * self.strength
        return damage

    def achieveAttack(self):
        if randint(1, 20) <= self.atk:
            return True
        else:
            return False

    def takeDamage(self, damage):
        if self.armor.durability > 0:
            damageTook = max(damage - self.armor.protection, 0)
            print(f"You made {damageTook} damage to the ennemy !")
            self.armor.durability = max(self.armor.durability - damage, 0)
        else:
            damageTook = damage
            print(f"You made {damageTook} damage to the ennemy !")
        self.health -= damageTook
        if self.armor.durability == 0:
            pass

    def chooseStrategy(self):
        if self.health/self.maxHealth < 0.1 and self.potions["Health"] > 0:
            return 2  # drink a potion
        else:
            return 1  # attack normally

    def utilisePotion(self, potion):
        if potion == "Health":
            self.potions[potion] -= 1
            self.health = min(self.health + 30 + self.level * 5, self.maxHealth)

    def printCombatInfos(self):
        print(f"Ennemy : HP = {self.health}/{self.maxHealth} | Mana = {self.mana}/{self.maxMana}")
        string = ""
        for i in tabPotions:
            string += f"{self.potions[i[0]]} {i[0]} potion | "
        print("You own : " + string + "\n")

    def __str__(self):
        return f"This enemy's perks are : Level = {self.level} | Health = {self.health}/{self.maxHealth} | Mana = {self.mana}/{self.maxMana} | Attack = {self.atk} | Strength = {self.strength}.\nHe owns a {self.armor.name}, a {self.weapon.name} and {self.potions['Health']} potions.\n"


class Player:

    def __init__(self, health, mana, atk, flee, gold, strength):
        self.pseudo = ""
        self.maxHealth = health
        self.health = health
        self.maxMana = mana
        self.mana = mana
        self.armor = None
        self.weapon = None
        self.xp = 0
        self.potions = {"Health": 0, "Mana": 0}
        self.spells = []
        self.level = 1
        self.atk = atk
        self.flee = flee
        self.gold = gold
        self.strength = strength
        self.initializePlayer()

    def initializePlayer(self):
        self.pseudo = input("What is your nickname ? : ")
        self.weapon = stick
        self.armor = tunic
        self.gold = 50

    def calculateDamage(self):  # Calculate attack damage
        if self.weapon.durability > 0:
            damage = self.weapon.damage + randint(1, 5) * self.strength
            self.weapon.durability = max(self.weapon.durability - damage, 0)
        else:
            damage = randint(1, 5) * self.strength
        return damage

    def achieveAttack(self):
        if randint(1, 20) <= self.atk:
            return True
        else:
            return False

    def levelUp(self):  # Apply the effects of a level up
        self.level += 1
        choice = int(input("Choose a perk to increase : 1 = attack | 2 = flee | 3 = strength : "))
        if choice == 1:
            self.atk += 1
        elif choice == 2:
            self.flee += 1
        elif choice == 3:
            self.strength += 1
        self.maxHealth += randint(10, 30)
        self.maxMana += randint(10, 30)
        self.health = self.maxHealth
        self.mana = self.maxMana
        print(f"You leveled up ! Your new stats are : Health = {self.maxHealth} | Mana = {self.maxMana} | Attack = {self.atk} | Flee = {self.flee} | Strength = {self.strength}")

    def gainXp(self, ennemy: Ennemy):  # Calculate the gain of xp
        xpGained = ennemy.level*20 + randint(-5, 5) * ennemy.level + randint(0, 10)
        self.xp += xpGained
        print(f"You gained {xpGained} xp.")

    def gainGold(self, ennemy: Ennemy):
        goldGained = ennemy.level * 20 + randint(-5, 5) * ennemy.level + randint(0, 10)
        self.gold += goldGained
        print(f"You gained {goldGained} gold.")

    def takeDamage(self, damage):
        if self.armor.durability > 0:
            damageTook = max(damage - self.armor.protection, 0)
            print(f"You took {damageTook} damage !")
            self.armor.durability = max(self.armor.durability - damage, 0)
        else:
            damageTook = damage
            print(f"You took {damageTook} damage !")
        self.health -= damageTook
        if self.armor.durability == 0:
            print("Your armor is broken ! (buy another)")

    def utilisePotion(self, potion):
        if potion == "Health":
            self.potions[potion] -= 1
            self.health = min(self.health + 30 + self.level*5, self.maxHealth)

    def printCombatInfos(self):
        print(f"{self.pseudo} : HP = {self.health}/{self.maxHealth} | Mana = {self.mana}/{self.maxMana}")
        string = ""
        for i in tabPotions:
            string += f"{self.potions[i[0]]} {i[0]} potion | "
        print("You own : " + string + "\n")

    def __str__(self):
        return f"{self.pseudo} : Health = {self.health}/{self.maxHealth} | Mana = {self.mana}/{self.maxMana} | Xp = {self.xp} |Attack = {self.atk} | Flee = {self.flee} | Strength = {self.strength}.\nYou own a {self.armor.name} ({self.armor.durability}/{self.armor.maxDurability} durability), a {self.weapon.name} ({self.weapon.durability}/{self.weapon.maxDurability} durability) and {self.potions['Health']} health potions."
