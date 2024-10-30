from random import randint
from character import *
from equipement import *
from utilities import *


def buyWeapon(player: Player):
    while True:
        clearTerminal()
        print("\n=======================WEAPON SHOP=====================\n")
        print(player)
        print(f"Gold : {player.gold}€")
        string = "What you can buy : \n"
        for weapon in range(len(weapons)):
            string += f"\t{weapon} = {weapons[weapon].name} (+{weapons[weapon].damage} dmg) | {weapons[weapon].value}€ \n"
        string += f"\t{weapon + 1} = Quit the menu :"
        choice = int(input(string))
        if choice == len(weapons):  # Quit the menu
            break
        while choice >= len(weapons) or choice < 0:
            print("Wrong entry !")
            choice = int(input(string))
        if player.gold < weapons[choice].value:
            print("You don't have enough money !")
            continue
        player.weapon = weapons[choice]
        player.gold -= weapons[choice].value
        print(f"{weapons[choice].name} has been bought")


def buyArmor(player: Player):
    while True:
        clearTerminal()
        print("\n=======================ARMOR SHOP=====================\n")
        print(player)
        print(f"Gold : {player.gold}€")
        string = "What you can buy :\n"
        for armor in range(len(armors)):
            string += f"\t{armor} = {armors[armor].name} (+{armors[armor].protection} protection) | {armors[armor].value}€ \n"
        string += f"\t{armor + 1} = Quit the menu :"
        choice = int(input(string))
        if choice == len(armors):  # Quit the menu
            break
        while choice >= len(armors) or choice < 0:
            print("Wrong entry !")
            choice = int(input(string))
        if player.gold < armors[choice].value:
            print("You don't have enough money !")
            continue
        player.armor = armors[choice]
        player.gold -= armors[choice].value
        print(f"{armors[choice].name} has been bought")


def buyPotion(player: Player):
    while True:
        clearTerminal()
        print("\n=======================POTION SHOP=====================\n")
        print(player)
        print(f"Gold : {player.gold}€")
        string = "What you can buy \n"
        for potion in range(len(tabPotions)):
            string += f"\t{potion} = {tabPotions[potion][0]} potion | {tabPotions[potion][1]}€\n"
        string += f"\t{potion + 1} = Quit the menu :"
        choice = int(input(string))
        if choice == len(tabPotions):  # Quit the menu
            break
        while choice >= len(tabPotions) or choice < 0:
            print("Wrong entry")
            choice = int(input("Choose what you want to buy : 1 = health potions : "))
        if player.gold < tabPotions[choice][1]:
            print("You don't have enough money !")
            continue
        player.potions[tabPotions[choice][0]] += 1
        player.gold -= tabPotions[choice][1]
        print(f"{tabPotions[choice][0]} potion has been bought")


def handleShop(player: Player):
    while True:
        clearTerminal()
        print("\n=======================SHOP=====================\n")
        print(player)
        print(f"Gold : {player.gold}€")
        choice = int(input("Choose what you want to buy :\n\t1 = weapon \n\t2 = armor \n\t3 = potion \n\t4 = quit the shop : "))
        while not (choice == 1 or choice == 2 or choice == 3 or choice == 4):
            print("Wrong entry")
            choice = int(input("Choose what you want to buy :\n\t1 = weapon \n\t2 = armor \n\t3 = potion \n\t4 = quit the shop : "))
        if choice == 1:
            buyWeapon(player)
        elif choice == 2:
            buyArmor(player)
        elif choice == 3:
            buyPotion(player)
        elif choice == 4:
            break
