from random import randint
from character import *
from equipement import *
from utilities import *


isFleeing = False


def calculateEnnemyHealthOrMana(level):
    health = max((level**2)*5 + randint(-10, 10), 10)
    return health


def chooseWeapon(player: Player):
    dist = abs(weapons[0].damage - player.maxHealth/4)
    weaponChoosed = (0, dist)
    for w in range(len(armors)):
        # print(f"{weapons[w].damage} - {player.maxHealth/5}")
        dist = abs(weapons[w].damage - player.maxHealth/4)
        if dist < weaponChoosed[1]:
            weaponChoosed = (w, dist)
    return max(weaponChoosed[0]-1, 0)
    # return 0  # standard option


def chooseArmor(eHealth):
    dist = abs(armors[0].protection - eHealth / 5)
    armorChoosed = (0, dist)
    for w in range(len(armors)):
        dist = abs(armors[w].protection - eHealth / 5)
        if dist < armorChoosed[1]:
            armorChoosed = (w, dist)
    return max(armorChoosed[0]-1, 0)
    # return 0  # standard option


def chooseNumberPotions(level):
    i = randint(0, level) // 3
    return i


def generateEnnemy(player: Player):
    eLevel = randint(1, player.level+2)
    eAttack = 10 + eLevel - randint(0, eLevel)
    eDodge = eLevel - eAttack + 20
    eHealth = calculateEnnemyHealthOrMana(eLevel)
    eMana = calculateEnnemyHealthOrMana(eLevel)
    eHPotion = chooseNumberPotions(eLevel)
    eMPotion = chooseNumberPotions(eLevel)
    eArmor = earmors[chooseArmor(eHealth)]
    eArmor.durability = eArmor.maxDurability
    eWeapon = eweapons[chooseWeapon(player)]
    eWeapon.durability = eWeapon.maxDurability
    eStrength = randint(1, player.level+2)
    ennemy = Ennemy(eHealth, eMana, eAttack, eDodge, eArmor, eWeapon, {"Health": eHPotion, "Mana": eMPotion}, [], eLevel, eStrength)
    return ennemy


def calculateXpLevels(level):
    xp = 0
    for i in range(0, level):
        xp += 100*(i+1)
    return xp


def playerTurn(player: Player, ennemy: Ennemy):
    global isFleeing
    done = False
    while not done:
        try:
            choice = int(input("Choose your action : 1 = attack | 2 = Drink a potion | 3 = Flee the fight | 4 = View Ennemy stats : "))
            while not (choice == 1 or choice == 2 or choice == 3 or choice == 4):
                choice = int(input("Enter a valid option !\nChoose your action : 1 = Attack | 2 = Drink a potion | 3 = Flee the fight | 4 = View Ennemy stats : "))
            if choice == 1:
                if player.achieveAttack():
                    damage = player.calculateDamage()
                    ennemy.takeDamage(damage)
                else:
                    print("You missed your attack !")
                done = True

            elif choice == 2:
                if player.potions["Health"] > 0:
                    player.utilisePotion("Health")
                done = True

            elif choice == 3:
                if randint(1, 20) <= player.flee:
                    isFleeing = True
                else:
                    print("You didn't manage to flee ! :(")
                done = True

            elif choice == 4:
                print("")
                print(ennemy)
        except:
            continue


def ennemyTurn(player: Player, ennemy: Ennemy):
    choice = ennemy.chooseStrategy()
    print(f"Ennemy choice is {choice}")
    if choice == 1:
        if ennemy.achieveAttack():
            damage = ennemy.calculateDamage()
            player.takeDamage(damage)
        else:
            print("The ennemy missed it's attack!")

    elif choice == 2:
        if ennemy.potions["Health"] > 0:
            ennemy.utilisePotion("Health")
            print("The ennemy took a health potion")


class Combat:
    def __init__(self):
        self.rounds = 0

    def turn(self, ennemy: Ennemy, player: Player):
        clearTerminal()
        print("===========================================")
        print(f"Turn {self.rounds} :\n")
        initiative = randint(0, 1)
        player.printCombatInfos()
        ennemy.printCombatInfos()
        if initiative == 1:  # the player play first
            print(f"The player attacks first.")
            print(f"\nYour Turn :\n")
            playerTurn(player, ennemy)
            print(f"\nEnemy's Turn\n")
            ennemyTurn(player, ennemy)
            if not isFleeing:
                input("\nPress enter to start a new turn")
        else:
            print(f"The ennemy attacks first.")
            print(f"\nEnemy's Turn\n")
            ennemyTurn(player, ennemy)
            print(f"\nYour Turn :\n")
            playerTurn(player, ennemy)
            if not isFleeing:
                input("\nPress enter to start a new turn")
        pass

    def combat(self, player: Player):
        flush_input()
        global isFleeing
        print("The fight will start !!!")
        ennemy = generateEnnemy(player)
        clearTerminal()
        print("You will fight : ")
        print(ennemy)
        input("\nPress enter to start the fight")
        while (ennemy.health > 0 and player.health > 0) and not isFleeing:  # boucle de combat
            self.rounds += 1
            self.turn(ennemy, player)
        clearTerminal()
        print("==================END OF THE FIGHT========================")
        if isFleeing:
            print("You successfully flew ")
            isFleeing = False
        elif player.health >= 0:
            print("You won !!")
            player.gainXp(ennemy)
            player.gainGold(ennemy)
            print(f"Your new xp is {player.xp}/{calculateXpLevels(player.level)}")
            if player.xp >= calculateXpLevels(player.level):
                print(f"LEVEL UP : {player.xp} / {calculateXpLevels(player.level)} xp")
                player.levelUp()
        else:
            print("You lost !")
        input("\nPress enter to go to the shop")
