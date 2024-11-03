import time
from random import randint
from character import *
from equipement import *
from utilities import *
from Widgets import *
from spells import *
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


def chooseSpells(player: Player):
    if 1 <= player.level <= 5:
        ind1 = 0
        ind2 = 0
        while ind1 == ind2:
            ind1 = randint(0, len(tierSpells[1]) - 1)
            ind2 = randint(0, len(tierSpells[1]) - 1)
        tabSpell = [tierSpells[1][ind1], tierSpells[1][ind2]]
    elif 6 <= player.level <= 10:
        ind1 = 0
        ind2 = 0
        ind3 = randint(0, len(tierSpells[1]) - 1)
        while ind1 == ind2:
            ind1 = randint(0, len(tierSpells[2]) - 1)
            ind2 = randint(0, len(tierSpells[2]) - 1)
        tabSpell = [tierSpells[1][ind3], tierSpells[2][ind1], tierSpells[2][ind2]]
    elif 11 <= player.level:
        ind1 = randint(0, len(tierSpells[1]) - 1)
        ind2 = randint(0, len(tierSpells[2]) - 1)
        ind3 = randint(0, len(tierSpells[3]) - 1)
        tabSpell = [tierSpells[1][ind1], tierSpells[2][ind2], tierSpells[2][ind3]]
    return tabSpell


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
    tabSpells = chooseSpells(player)
    ennemy = Ennemy(eHealth, eMana, eAttack, eDodge, eArmor, eWeapon, {"Health": eHPotion, "Mana": eMPotion}, tabSpells, eLevel, eStrength)
    return ennemy


def calculateXpLevels(level):
    xp = 0
    for i in range(0, level):
        xp += 100*(i+1)
    return xp


class Combat:
    def __init__(self):
        self.rounds = 0
        self.roundText = []
        self.done = False

    def chooseSpellToLaunch(self, player: Player):
        while True:
            clearTerminal()
            widget = ChooseWidget()
            for spell in player.spells:
                widget.add_choice(spell.name)
            widget.add_choice("Go back to the action menu")
            widget.setPrefix("Select a spell\n")
            choice = widget.run() - 1
            if choice == len(player.spells):
                self.done = False
                return
            clearTerminal()
            widget = ChooseWidget()
            widget.setPrefix(f"{player.spells[choice].name} : \n{player.spells[choice].description}\nCost : {player.spells[choice].manaCost} mana\n")
            widget.add_choice("Use spell")
            widget.add_choice("Go back to the spell menu")
            choice2 = widget.run()
            if choice2 == 1:
                return player.spells[choice]
            else:
                continue

    def choosePotion(self, player: Player):
        while True:
            clearTerminal()
            widget = ChooseWidget()
            for i in tabPotions:
                widget.add_choice(i[0] + f" | You have {player.potions[i[0]]}")
            widget.add_choice("Go back to the action menu")
            widget.setPrefix("Choose a potion to use:\n")
            choice = widget.run() - 1
            flush_input()
            if choice == len(tabPotions):
                self.done = False
                return
            if player.potions[tabPotions[choice][0]] <= 0:
                continue
            player.usePotion(tabPotions[choice][0])
            return tabPotions[choice][0]

    def returnRoundText(self):
        string = ""
        for i in self.roundText:
            string += i + "\n"
        return string

    def playerTurn(self, player: Player, ennemy: Ennemy):
        global isFleeing
        self.done = False
        while not self.done:
            try:
                clearTerminal()
                widget = ChooseWidget()
                widget.add_choice("Attack")
                widget.add_choice("Drink a potion")
                widget.add_choice("Flee the fight")
                widget.add_choice("Launch a spell")
                widget.add_choice("View Ennemy stats")
                widget.add_choice("View your stats")
                widget.setPrefix(self.returnRoundText())
                choice = widget.run()
                flush_input()
                clearTerminal()
                print(self.returnRoundText())
                if choice == 1:
                    if player.achieveAttack():
                        damage, isWBroken = player.calculateDamage()
                        s = ennemy.takeDamage(damage)
                        print(f"You dealt {s} damage to the ennemy")
                        self.roundText.append(f"You dealt {s} to the ennemy")
                        if isWBroken:
                            print("Your weapon is broken ! (buy another)")
                            self.roundText.append("Your weapon is broken ! (buy another)")
                    else:
                        print("You missed your attack !")
                        self.roundText.append("You missed your attack !")
                    self.done = True

                elif choice == 2:
                    self.done = True
                    potion = self.choosePotion(player)
                    clearTerminal()
                    print(self.returnRoundText())
                    print(f"You took a {potion} potion")
                    self.roundText.append(f"You took a {potion} potion")
                    if not self.done:
                        continue

                elif choice == 3:
                    if randint(1, 20) <= player.flee:
                        isFleeing = True
                    else:
                        print("You didn't manage to flee ! :(")
                        self.roundText.append("You didn't manage to flee ! :(")
                    self.done = True

                elif choice == 4:
                    self.done = True
                    clearTerminal()
                    launchedSpell = self.chooseSpellToLaunch(player)
                    if self.done:
                        if player.mana >= launchedSpell.manaCost:
                            player.mana = player.mana - launchedSpell.manaCost
                            launchedSpell.applySpellOnEnnemy(ennemy, player)
                            clearTerminal()
                            print(self.returnRoundText())
                            print(f"{launchedSpell.name} was lanched !")
                        else:
                            print("You don't have enough mana !")
                            self.roundText.append("You don't have enough mana !")
                        flush_input()
                        continue
                    else:
                        flush_input()
                        continue

                elif choice == 5:
                    print("")
                    self.roundText.append("")
                    print(ennemy)
                    self.roundText.append(ennemy.__str__())

                elif choice == 6:
                    print("")
                    self.roundText.append("")
                    print(player)
                    self.roundText.append(player.__str__())

            except Exception as e:
                print(e)
                flush_input()
                input()
                continue

    def ennemyTurn(self, player: Player, ennemy: Ennemy):
        choice = ennemy.chooseStrategy()
        if choice == 1:
            print("The ennemy attacks !")
            self.roundText.append("The ennemy attacks !")
            if ennemy.achieveAttack():
                damage = ennemy.calculateDamage()
                s, isABroken = player.takeDamage(damage)
                print(f"You took {s} damage !")
                self.roundText.append(f"You took {s} damage !")
                if isABroken:
                    print("Your armor is broken ! (buy another)")
                    self.roundText.append("Your armor is broken ! (buy another)")
            else:
                print("The ennemy missed it's attack!")
                self.roundText.append("The ennemy missed it's attack!")

        elif choice == 2:
            if ennemy.potions["Health"] > 0:
                ennemy.usePotion("Health")
                print("The ennemy took a health potion")
                self.roundText.append("The ennemy took a health potion")

        elif choice == 3:
            if ennemy.potions["Mana"] > 0:
                ennemy.usePotion("Mana")
                print("The ennemy took a mana potion")
                self.roundText.append("The ennemy took a mana potion")

        elif choice == 4:
            spells = ennemy.returnSpells("Buff")
            spellCanUse = ennemy.returnSpellCanLaunch(spells)
            if len(spellCanUse) > 1:
                ind = randint(0, len(spellCanUse) - 1)
            else:
                ind = 0
            spell = spellCanUse[ind]
            spell.applySpellOnPlayer(ennemy, player)
            print(f"The ennemy launched the spell '{spell.name}' ({spell.description})'")
            self.roundText.append(f"The ennemy launched the spell '{spell.name}' ({spell.description})'")

        elif choice == 5:
            spells = ennemy.returnSpells("Debuff")
            spellCanUse = ennemy.returnSpellCanLaunch(spells)
            if len(spellCanUse) > 1:
                ind = randint(0, len(spellCanUse) - 1)
            else:
                ind = 0
            spell = spellCanUse[ind]
            spell.applySpellOnPlayer(ennemy, player)
            print(f"The ennemy launched the spell '{spell.name}' ({spell.description})'")
            self.roundText.append(f"The ennemy launched the spell '{spell.name}' ({spell.description})'")

        elif choice == 6:
            spells = ennemy.returnSpells("Heal")
            spellCanUse = ennemy.returnSpellCanLaunch(spells)
            if len(spellCanUse) > 1:
                ind = randint(0, len(spellCanUse) - 1)
            else:
                ind = 0
            spell = spellCanUse[ind]
            spell.applySpellOnPlayer(ennemy, player)
            print(f"The ennemy launched the spell '{spell.name}' ({spell.description})'")
            self.roundText.append(f"The ennemy launched the spell '{spell.name}' ({spell.description})'")

    def turn(self, ennemy: Ennemy, player: Player):
        self.roundText = []  # set the prints to []
        clearTerminal()
        print("===========================================")
        self.roundText.append("===========================================")
        print(f"Turn {self.rounds} :\n")
        self.roundText.append(f"Turn {self.rounds} :\n")
        initiative = randint(0, 1)
        self.roundText.append(player.printCombatInfos())
        self.roundText.append(ennemy.printCombatInfos())
        if initiative == 1:  # the player play first
            print("The player attacks first.")
            self.roundText.append("The player attacks first.")
            print("\nYour Turn :\n")
            self.roundText.append("\nYour Turn :\n")
            self.playerTurn(player, ennemy)
            print("\nEnemy's Turn\n")
            self.roundText.append("\nEnemy's Turn :\n")
            self.ennemyTurn(player, ennemy)
            flush_input()
            if not isFleeing:
                input("\nPress enter to start a new turn")
        else:
            print(f"The ennemy attacks first.")
            self.roundText.append("The ennemy attacks first.")
            print(f"\nEnemy's Turn\n")
            self.roundText.append("\nEnemy's Turn :\n")
            self.ennemyTurn(player, ennemy)
            print(f"\nYour Turn :\n")
            self.roundText.append("\nYour Turn :\n")
            self.playerTurn(player, ennemy)
            flush_input()
            if not isFleeing:
                input("\nPress enter to start a new turn")

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
        player.resetBetweenCombats()
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
