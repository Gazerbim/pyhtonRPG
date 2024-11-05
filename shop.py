from random import randint
from character import *
from equipement import *
from utilities import *
from Widgets import *

def buyWeapon(player: Player):
    while True:
        widget = ChooseWidget()
        clearTerminal()
        prefix = "\n=======================WEAPON SHOP=====================\n"
        prefix += player.__str__()
        prefix += f"\nGold : {player.gold}€\n"
        prefix += "What you can buy : \n"
        for weapon in range(len(weapons)):
            widget.add_choice(f"{weapons[weapon].name} (+{weapons[weapon].damage} dmg) | {weapons[weapon].value}€")
        widget.add_choice(f"Quit the menu :")
        widget.setPrefix(prefix)
        widget.run()
        choice = widget.cursor
        if choice == len(weapons):  # Quit the menu
            break
        if player.gold < weapons[choice].value:
            print("You don't have enough money !")
            continue
        player.weapon = weapons[choice]
        player.gold -= weapons[choice].value
        player.weapon.durability = player.weapon.maxDurability
        print(f"{weapons[choice].name} has been bought")


def buyArmor(player: Player):
    while True:
        widget = ChooseWidget()
        clearTerminal()
        prefix = "\n=======================ARMOR SHOP=====================\n"
        prefix += player.__str__()
        prefix += f"\nGold : {player.gold}€\n"
        prefix += "What you can buy : \n"
        for armor in range(len(armors)):
            widget.add_choice(f"{armors[armor].name} (+{armors[armor].protection} protection) | {armors[armor].value}€")
        widget.add_choice(f"Quit the menu :")
        widget.setPrefix(prefix)
        widget.run()
        choice = widget.cursor
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
        player.armor.durability = player.armor.maxDurability
        print(f"{armors[choice].name} has been bought")


def buyPotion(player: Player):
    while True:
        widget = ChooseWidget()
        clearTerminal()
        prefix = "\n=======================POTION SHOP=====================\n"
        prefix += player.__str__()
        prefix += f"\nGold : {player.gold}€\n"
        prefix += "What you can buy : \n"
        for potion in range(len(tabPotions)):
            widget.add_choice(f"{tabPotions[potion][0]} potion | {tabPotions[potion][1]}€")
        widget.add_choice(f"Quit the menu :")
        widget.setPrefix(prefix)
        widget.run()
        choice = widget.cursor
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
        prefix = "\n=======================SHOP=====================\n"
        prefix += player.__str__()
        prefix += f"\nGold : {player.gold}€\n"
        widget = ChooseWidget()
        widget.add_choice("Buy Weapons")
        widget.add_choice("Buy Armors")
        widget.add_choice("Buy Potions")
        widget.add_choice("Quit the shop")
        widget.add_choice("Back to the main menu")
        widget.setPrefix(prefix)
        widget.run()
        choice = widget.cursor
        if choice == 0:
            buyWeapon(player)
        elif choice == 1:
            buyArmor(player)
        elif choice == 2:
            buyPotion(player)
        elif choice == 3:
            break
        elif choice == 4:
            player.quit = True
            break
