from os import write
from random import randint
from utilities import *
from equipement import *
from Widgets import *


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

        self.maxAttack = atk
        self.atk = atk

        self.maxFlee = flee
        self.flee = flee

        self.maxStrength = strength
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
            self.armor.durability = max(self.armor.durability - damage, 0)
        else:
            damageTook = damage
        self.health -= damageTook
        if self.armor.durability == 0:
            pass
        return damageTook

    def haveSpell(self, category):
        for spell in self.spells:
            if spell.category == category:
                return True
        return False

    def returnSpells(self, category):
        tabSpell = []
        for spell in self.spells:
            if spell.category == category:
                tabSpell.append(spell)
        return tabSpell

    def canUseOneSpell(self, tabSpells):
        for spell in tabSpells:
            if spell.manaCost <= self.mana:
                return True
        return False

    def returnSpellCanLaunch(self, tabSpell):
        tabSpellCanUse = []
        for spell in tabSpell:
            if spell.manaCost <= self.mana:
                tabSpellCanUse.append(spell)
        return tabSpellCanUse

    def chooseStrategy(self):
        while True:
            if self.health/self.maxHealth < 0.1 and self.potions["Health"] > 0:
                return 2  # drink a health potion
            elif self.health/self.maxHealth < 0.1 and self.haveSpell("Heal") and self.canUseOneSpell(self.returnSpells("Heal")):
                return 6  # use a healing spell
            elif (not self.canUseOneSpell(self.spells) or self.mana/self.maxMana < 0.2) and self.potions["Mana"] > 0:
                return 3  # drink a mana potion
            else:
                choice = randint(1, 5)
                if choice == 1 or choice == 2 or choice == 3:
                    return 1  # attack normally
                elif choice == 4:
                    if self.haveSpell("Buff") and self.canUseOneSpell(self.returnSpells("Buff")):
                        return 4  # use a buff spell
                elif choice == 5:
                    if self.haveSpell("Debuff") and self.canUseOneSpell(self.returnSpells("Debuff")):
                        return 5  # use a debuff spell

    def usePotion(self, potion):
        if potion == "Health":
            self.potions[potion] -= 1
            self.health = min(self.health + 30 + self.level * 5, self.maxHealth)
        if potion == "Mana":
            self.potions[potion] -= 1
            self.mana = min(self.mana + 30 + self.level * 5, self.maxMana)

    def printCombatInfos(self):
        string = f"Ennemy : HP = {self.health}/{self.maxHealth} | Mana = {self.mana}/{self.maxMana}\nYou own : "
        for i in tabPotions:
            string += f"{self.potions[i[0]]} {i[0]} potion | "
        print(string + "\n")
        return string + "\n"

    def __str__(self):
        spellsName = []
        for spell in self.spells:
            spellsName.append(spell.name)
        return f"This enemy's perks are : Level = {self.level} | Health = {self.health}/{self.maxHealth} | Mana = {self.mana}/{self.maxMana} | Attack = {self.atk}+({self.atk-self.maxAttack}) | Strength = {self.strength}+({self.strength-self.maxStrength}).\nHe owns a {self.armor.name}, a {self.weapon.name}\nHe possesses {self.potions['Health']} health potions and {self.potions['Mana']} mana potions.\nHis spell are : {spellsName}\n"


class Player:
    def __init__(self, health, mana, atk, flee, gold, strength, pseudo):
        self.pseudo = pseudo

        self.maxHealth = health
        self.health = health

        self.maxMana = mana
        self.mana = mana

        self.weapon = stick
        self.armor = tunic
        self.xp = 0
        self.potions = {"Health": 0, "Mana": 0}
        self.spells = []

        self.level = 1

        self.maxAttack = atk
        self.atk = atk

        self.maxFlee = flee
        self.flee = flee

        self.maxStrength = strength
        self.strength = strength

        self.gold = gold

        self.quit = False

    def resetBetweenCombats(self):
        self.atk = self.maxAttack
        self.flee = self.maxFlee
        self.strength = self.maxStrength
        self.health = min(self.health + 15, self.maxHealth)
        self.mana = min(self.mana + 15, self.maxMana)

    def calculateDamage(self):  # Calculate attack damage
        if self.weapon.durability > 0:
            damage = self.weapon.damage + randint(1, 5) * self.strength
            self.weapon.durability = max(self.weapon.durability - damage, 0)
        else:
            damage = randint(1, 5) * self.strength
        if self.weapon.durability <= 0:
            return damage, True
        return damage, False

    def achieveAttack(self):
        if randint(1, 20) <= self.atk:
            return True
        else:
            return False

    def giveSpell(self):
        if 1 <= self.level <= 5:
            ind1 = 0
            ind2 = 0
            while ind1 == ind2:
                ind1 = randint(0, len(playerTierSpells[1]) - 1)
                ind2 = randint(0, len(playerTierSpells[1]) - 1)
            tabSpell = [playerTierSpells[1][ind1], playerTierSpells[1][ind2]]
        elif 6 <= self.level <= 10:
            ind1 = 0
            ind2 = 0
            ind3 = randint(0, len(playerTierSpells[1]) - 1)
            while ind1 == ind2:
                ind1 = randint(0, len(playerTierSpells[2]) - 1)
                ind2 = randint(0, len(playerTierSpells[2]) - 1)
            tabSpell = [playerTierSpells[1][ind3], playerTierSpells[2][ind1], playerTierSpells[2][ind2]]
        elif 11 <= self.level:
            ind1 = randint(0, len(playerTierSpells[1]) - 1)
            ind2 = randint(0, len(playerTierSpells[2]) - 1)
            ind3 = randint(0, len(playerTierSpells[3]) - 1)
            tabSpell = [playerTierSpells[1][ind1], playerTierSpells[2][ind2], playerTierSpells[2][ind3]]
        return tabSpell

    def chooseSpell(self, tabSpells):
        while True:
            clearTerminal()
            widget = ChooseWidget()
            widget.set_flag("AllowSeveralSameOption", True)
            for spell in tabSpells:
                widget.add_choice(spell.name)
            widget.add_choice("Take no spell")
            string = "Choose a spell to learn : \nYour spells : ["
            for s in self.spells:
                string += s.name + ", "
            string += "]\n"
            widget.setPrefix(string)
            choice = widget.run() - 1
            flush_input()
            if choice == len(tabSpells):
                return "You didn't choose a spell"
            clearTerminal()
            widget = ChooseWidget()
            widget.set_flag("AllowSeveralSameOption", True)
            widget.add_choice("Take the spell")
            widget.add_choice("Return to the spell choice")
            widget.setPrefix(f"{tabSpells[choice].name} :\n{tabSpells[choice].description}\nCost : {tabSpells[choice].manaCost} mana\n")
            choice2 = widget.run()
            flush_input()
            if choice2 == 2:
                continue
            else:
                if tabSpells[choice] in self.spells:
                    print("You already have this spell !")
                    input("Press Enter to continue...")
                    continue
                self.spells.append(tabSpells[choice])
                clearTerminal()
                return f"You choosed the spell '{tabSpells[choice].name}'"

    def levelUp(self):  # Apply the effects of a level up
        self.level += 1
        widget = ChooseWidget()
        widget.add_choice(f"Attack {self.maxAttack} : +1")
        widget.add_choice(f"Flee {self.maxFlee} : +1")
        widget.add_choice(f"Strength {self.maxStrength} : +2")
        widget.setPrefix("Choose the ability you want to increase : \n")
        choice = widget.run()
        clearTerminal()
        flush_input()
        if choice == 1:
            self.atk += 1
            self.maxAttack += 1
        elif choice == 2:
            self.flee += 1
            self.maxFlee += 1
        elif choice == 3:
            self.strength += 2
            self.maxStrength += 2
        self.maxHealth += randint(10, 30)
        self.maxMana += randint(10, 30)
        self.health = self.maxHealth
        self.mana = self.maxMana
        if self.level % 2 == 0:
            tabSpell = self.giveSpell()
            print(self.chooseSpell(tabSpell))
        print(f"You leveled up ! Your new stats are : Health = {self.maxHealth} | Mana = {self.maxMana} | Attack = {self.atk} | Flee = {self.flee} | Strength = {self.strength}")

    def gainXp(self, ennemy: Ennemy):  # Calculate the gain of xp
        xpGained = ennemy.level*20 + randint(-5, 5) * ennemy.level + randint(0, 10)
        self.xp += xpGained
        print(f"You gained {xpGained} xp.")
        return xpGained

    def gainGold(self, ennemy: Ennemy):
        goldGained = ennemy.level * 20 + randint(-5, 5) * ennemy.level + randint(0, 10)
        self.gold += goldGained
        print(f"You gained {goldGained} gold.")

    def takeDamage(self, damage):
        if self.armor.durability > 0:
            damageTook = max(damage - self.armor.protection, 0)
            self.armor.durability = max(self.armor.durability - damage, 0)
        else:
            damageTook = damage
        self.health -= damageTook
        if self.armor.durability == 0:
            return damageTook, True
        return damageTook, False

    def usePotion(self, potion):
        if potion == "Health":
            self.potions[potion] -= 1
            self.health = min(self.health + 30 + self.level*5, self.maxHealth)
        if potion == "Mana":
            self.potions[potion] -= 1
            self.mana = min(self.mana + 30 + self.level * 5, self.maxMana)

    def printCombatInfos(self):
        string = f"{self.pseudo} : HP = {self.health}/{self.maxHealth} | Mana = {self.mana}/{self.maxMana}\nYou own : "
        for i in tabPotions:
            string += f"{self.potions[i[0]]} {i[0]} potion | "
        print(string + "\n")
        return string + "\n"

    def __str__(self):
        return f"{self.pseudo} : Health = {self.health}/{self.maxHealth} | Mana = {self.mana}/{self.maxMana} | Xp = {self.xp} |Attack = {self.atk}+({self.atk-self.maxAttack}) | Flee = {self.flee}+({self.flee-self.maxFlee}) | Strength = {self.strength}+({self.strength-self.maxStrength}).\nYou own a {self.armor.name} ({self.armor.durability}/{self.armor.maxDurability} durability), a {self.weapon.name} ({self.weapon.durability}/{self.weapon.maxDurability} durability)\nYou possess {self.potions['Health']} health potions and {self.potions['Mana']} mana potions.\n"


class Spell:
    def __init__(self, name, description, manaCost, category):
        self.name = name
        self.description = description
        self.category = category
        self.manaCost = manaCost

        # Player attributes
        self.isAttackProp = False
        self.attackAttribute = 0
        self.isFleeProp = False
        self.fleeAttribute = 0
        self.isStrengthProp = False
        self.strengthAttribute = 0
        self.isDamageProp = False
        self.damage = 0

        # Ennemy attributes
        self.isEAttackProp = False
        self.eAttackAttribute = 0
        self.isEFleeProp = False
        self.eFleeAttribute = 0
        self.isEStrengthProp = False
        self.eStrengthAttribute = 0
        self.isEDamageProp = False
        self.eDamage = 0

    def applySpellOnPlayer(self, ennemy: Ennemy, player: Player):
        if self.isEAttackProp:
            player.atk = max(round(player.atk + player.atk * self.eAttackAttribute/100), 0)
        else:
            player.atk = max(player.atk + self.eAttackAttribute, 0)

        if self.isEFleeProp:
            player.flee = max(round(player.flee + player.flee * self.eFleeAttribute / 100), 0)
        else:
            player.flee = max(player.flee + self.eFleeAttribute, 0)

        if self.isEStrengthProp:
            player.strength = max(round(player.strength + player.strength * self.eStrengthAttribute / 100), 0)
        else:
            player.strength = max(player.strength + self.eStrengthAttribute, 0)

        if self.isEDamageProp:
            player.health = max(round(player.health + player.health * self.eDamage / 100), 1)
        else:
            player.health = max(player.health + self.eDamage, 0)

        # Effect on Ennemy

        if self.isAttackProp:
            ennemy.atk = max(round(ennemy.atk + ennemy.atk * self.attackAttribute / 100), 0)
        else:
            ennemy.atk = max(ennemy.atk + self.attackAttribute, 0)

        if self.isFleeProp:
            ennemy.flee = max(round(ennemy.flee + ennemy.flee * self.fleeAttribute / 100), 0)
        else:
            ennemy.flee = max(ennemy.flee + self.fleeAttribute, 0)

        if self.isStrengthProp:
            ennemy.strength = max(round(ennemy.strength + ennemy.strength * self.strengthAttribute / 100), 0)
        else:
            ennemy.strength = max(ennemy.strength + self.strengthAttribute, 0)

        if self.isDamageProp:
            ennemy.health = max(round(ennemy.health + ennemy.health * self.damage / 100), 1)
        else:
            ennemy.health = max(ennemy.health + self.damage, 0)

    def applySpellOnEnnemy(self, ennemy: Ennemy, player: Player):
        if self.isEAttackProp:
            ennemy.atk = max(round(ennemy.atk + ennemy.atk * self.eAttackAttribute / 100), 0)
        else:
            ennemy.atk = max(ennemy.atk + self.eAttackAttribute, 0)

        if self.isEFleeProp:
            ennemy.flee = max(round(ennemy.flee + ennemy.flee * self.eFleeAttribute / 100), 0)
        else:
            ennemy.flee = max(ennemy.flee + self.eFleeAttribute, 0)

        if self.isEStrengthProp:
            ennemy.strength = max(round(ennemy.strength + ennemy.strength * self.eStrengthAttribute / 100), 0)
        else:
            ennemy.strength = max(ennemy.strength + self.eStrengthAttribute, 0)

        if self.isEDamageProp:
            ennemy.health = max(round(ennemy.health + ennemy.health * self.eDamage / 100), 1)
        else:
            ennemy.health = max(ennemy.health + self.eDamage, 0)

        # Effect on Player

        if self.isAttackProp:
            player.atk = max(round(player.atk + player.atk * self.attackAttribute / 100), 0)
        else:
            player.atk = max(player.atk + self.attackAttribute, 0)

        if self.isFleeProp:
            player.flee = max(round(player.flee + player.flee * self.fleeAttribute / 100), 0)
        else:
            player.flee = max(player.flee + self.fleeAttribute, 0)

        if self.isStrengthProp:
            player.strength = max(round(player.strength + player.strength * self.strengthAttribute / 100), 0)
        else:
            player.strength = max(player.strength + self.strengthAttribute, 0)

        if self.isDamageProp:
            player.health = max(round(player.health + player.health * self.damage / 100), 1)
        else:
            player.health = max(player.health + self.damage, 0)

    def applySpell(self, isPlayer, ennemy: Ennemy, player: Player):
        if isPlayer:
            self.applySpellOnEnnemy(ennemy, player)
        else:
            self.applySpellOnPlayer(ennemy, player)

"""=========Spell definition==========="""
oneHpSpell = Spell("Lunar Attack", "Set the ennemy's life to 1% and reduce your attack by 10 and your life by 50", 100, "Debuff")  # met a un hp et debuff attack
oneHpSpell.isEDamageProp = True
oneHpSpell.eDamage = -99
oneHpSpell.attackAttribute = -10
oneHpSpell.damage = -50

heal = Spell("Simple Heal", "Heal a small amount of health", 15, "Heal")
heal.damage = 15

betterHeal = Spell("High Heal", "Heal a medium amount of health", 40, "Heal")
betterHeal.damage = 50

superHeal = Spell("Super Heal", "Heal a high amount of health", 70, "Heal")
superHeal.damage = 100

weakness1 = Spell("Light Weakness", "Reduce the ennemy's strength by 20%", 20, "Debuff")
weakness1.eStrengthAttribute = 20
weakness1.isEStrengthProp = True

weakness2 = Spell("Heavy Weakness", "Reduce the ennemy's strength by 50%", 100, "Debuff")
weakness2.eStrengthAttribute = 50
weakness2.isEStrengthProp = True

reinforcement = Spell("Reinforcement", "Increase strength by 5", 30, "Buff")
reinforcement.strengthAttribute = 5

berserk = Spell("Berserk Fury", "Triple strength but reduce attack", 50, "Buff")
berserk.strengthAttribute = 200
berserk.isStrengthProp = True
berserk.attackAttribute = -50
berserk.isAttackProp = True

coward = Spell("Coward", "Increase chances to flee the fight but reduce attack", 50, "Buff")
coward.fleeAttribute = 5
coward.attackAttribute = -50
coward.isAttackProp = True

revitalization = Spell("Revitalization", "Restores a moderate amount of health and slightly increases flee chance", 60, "Heal")
revitalization.damage = 40
revitalization.fleeAttribute = 5

flameStrike = Spell("Flame Strike", "Deals 40 damage to the enemy and reduces their strength by 10%", 70, "Debuff")
flameStrike.eDamage = -40
flameStrike.eStrengthAttribute = -10
flameStrike.isEStrengthProp = True

iceBarrier = Spell("Ice Barrier", "Deals 20 damage to the enemy and reduces their flee chance by 20%", 50, "Debuff")
iceBarrier.eDamage = -20  # Inflige 30 dégâts à l'ennemi
iceBarrier.eFleeAttribute = -20
iceBarrier.isEFleeProp = True

cripple = Spell("Cripple", "Reduces enemy's attack and strength by 15%", 45, "Debuff")
cripple.eAttackAttribute = -30
cripple.isEAttackProp = True
cripple.eStrengthAttribute = -30
cripple.isEStrengthProp = True

mightyBlow = Spell("Mighty Blow", "Increases attack by 25%", 40, "Buff")
mightyBlow.attackAttribute = 25
mightyBlow.isAttackProp = True

sacrifice = Spell("Sacrifice", "Deals 70 damage to the enemy but reduces your health by 30", 60, "Debuff")
sacrifice.eDamage = -70  # Deals 70 direct damage to the enemy
sacrifice.damage = -30  # Reduces player's health by 30 points

overload = Spell("Overload", "Doubles attack but halves strength", 50, "Buff")
overload.attackAttribute = 100  # Increases attack by 100% (doubles)
overload.isAttackProp = True
overload.strengthAttribute = -50  # Reduces strength by 50%
overload.isStrengthProp = True

soulDrain = Spell("Soul Drain", "Drains enemy's strength but lowers attack", 60, "Debuff")
soulDrain.eStrengthAttribute = -90  # Lowers enemy's strength by 90%
soulDrain.isEStrengthProp = True
soulDrain.StrengthAttribute = 10
soulDrain.attackAttribute = -10  # Reduces player's attack by 10 points

powerSurge = Spell("Power Surge", "Increases strength by 40 but lowers health by 50", 150, "Buff")
powerSurge.strengthAttribute = 40  # Increases strength by 40 points
powerSurge.damage = -70  # Decreases player's health by 70%
powerSurge.isDamageProp = True

vampireBite = Spell("Vampire Bite", "Drain health from the ennemy", 50, "Heal")
vampireBite.damage = 20
vampireBite.eDamage = 20

infernoBlast = Spell("Inferno Blast", "Deals 100 damage to the enemy but costs 30 health", 120, "Debuff")
infernoBlast.eDamage = -100  # Deals 100 damage to the enemy
infernoBlast.damage = -30  # Reduces player's health by 30 points

precision = Spell("Precision", "Slightly increase attack", 40, "Buff")
precision.attackAttribute = 20
precision.isAttackProp = True
"""==========Spell Array============"""
tierSpells = {1: [heal, reinforcement, iceBarrier, cripple, mightyBlow, overload, vampireBite, precision], 2: [betterHeal, weakness2, berserk, flameStrike, sacrifice, soulDrain], 3: [superHeal, infernoBlast]}  # Spells that the ennemy can use
playerTierSpells = {1: [heal, reinforcement, cripple, mightyBlow, overload, vampireBite, precision], 2: [betterHeal, weakness2, berserk, revitalization, flameStrike, sacrifice, soulDrain], 3: [superHeal, oneHpSpell, infernoBlast]}  # Spells that the player can use
