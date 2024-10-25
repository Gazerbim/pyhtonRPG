from random import randint


class Armor:
    def __init__(self, protection, durability, value, magic_protection, name):
        self.name = name
        self.protection = protection
        self.magicProtection = magic_protection
        self.durability = durability
        self.maxDurability = durability
        self.value = value


class Weapon:
    def __init__(self, damage, durability, value, magic_damage, name):
        self.name = name
        self.damage = damage
        self.magicDamage = magic_damage
        self.durability = durability
        self.maxDurability = durability
        self.value = value


class Spell:
    pass


class Ennemy:
    def __init__(self, health, mana, atk, dodge, armor, weapon, potions, spells, level, strength):
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
        self.dodge = dodge
        self.strength = strength

    def calculateDamage(self):  # Calculate attack damage
        return self.weapon.damage + randint(1, 5) * self.strength

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
            print("Votre armure est cassée !")

    def chooseStrategy(self):
        if self.health/self.maxHealth < 0.1:
            return 2  # drink a potion
        else:
            return 1  # attack normally

    def utilisePotion(self, potion):
        if potion == "Health":
            self.potions[potion] -= 1
            self.health += 30 + self.level*5

    def __str__(self):
        return f"This enemy's perks are : Health = {self.health}/{self.maxHealth} | Mana = {self.mana}/{self.maxMana} | Attack = {self.atk} | Dodge = {self.dodge} | Strength = {self.strength}.\nHe owns a {self.armor.name} and a {self.weapon.name}."


class Player:
    def __init__(self, health, mana, atk, dodge, gold, strength):
        self.maxHealth = health
        self.health = health
        self.maxMana = mana
        self.mana = mana
        self.armor = None
        self.weapon = None
        self.xp = 0
        self.potions = {"Health": 0}
        self.spells = []
        self.level = 1
        self.atk = atk
        self.dodge = dodge
        self.gold = gold
        self.strength = strength

    def calculateDamage(self):  # Calculate attack damage
        return self.weapon.damage + randint(1, 5) * self.strength

    def achieveAttack(self):
        if randint(1, 20) <= self.atk:
            return True
        else:
            return False

    def levelUp(self):  # Apply the effects of a level up
        self.level += 1
        choice = int(input("Choose a perk to increase : 1 = attack | 2 = dodge | 3 = strength : "))
        if choice == 1:
            self.atk += 1
        elif choice == 2:
            self.dodge += 1
        elif choice == 3:
            self.strength += 1
        self.maxHealth += randint(10, 30)
        self.maxMana += randint(10, 30)
        self.health = self.maxHealth
        self.mana = self.maxMana
        print(f"You leveled up ! Your new stats are : Health = {self.maxHealth} | Mana = {self.maxMana} | Attack = {self.atk} | Dodge = {self.dodge} | Strength = {self.strength}")

    def gainXp(self, ennemy: Ennemy):  # Calculate the gain of xp
        self.xp += ennemy.level*20

    def takeDamage(self, damage):
        if self.armor.durability > 0:
            damageTook = max(damage - self.armor.protection, 0)
            self.armor.durability = max(self.armor.durability - damage, 0)
        else:
            damageTook = damage
        self.health -= damageTook
        if self.armor.durability == 0:
            print("Votre armure est cassée !")


    def utilisePotion(self, potion):
        if potion == "Health":
            self.potions[potion] -= 1
            self.health += 30 + self.level*5

    def __str__(self):
        return f"Your perks are : Health = {self.health}/{self.maxHealth} | Mana = {self.mana}/{self.maxMana} | Attack = {self.atk} | Dodge = {self.dodge} | Strength = {self.strength}.\nYou own a {self.armor.name} and a {self.weapon.name}."


"""Definition of objects"""
stick = Weapon(1, 100000, 0, 0, "Stick")
ironSword = Weapon(5, 100, 20, 0, "Iron Sword")
diamondSword = Weapon(20, 1000, 100, 0, "Diamond Sword")
energySword = Weapon(50, 5000, 500, 0, "Energy Sword")
masterSword = Weapon(100, 20000, 1000, 0, "Master Sword")
darkSword = Weapon(150, 50000, 1500, 0, "Dark Sword")

weapons = [stick, ironSword, diamondSword, energySword, masterSword, darkSword]

tunic = Armor(1, 100000, 0, 0, "Tunic")
ironArmor = Armor(5, 100, 20, 0, "Iron Armor")
diamondArmor = Armor(20, 1000, 100, 0, "Diamond Armor")
energyArmor = Armor(50, 5000, 500, 0, "Energy Armor")
draconicArmor = Armor(100, 20000, 3000, 0, "Draconic Armor")
eternalArmor = Armor(200, 100000000000, 5000, 0, "Eternal Armor")

armors = [tunic, ironArmor, diamondArmor, energyArmor, draconicArmor, eternalArmor]

"""Combat logic"""


def calculateEnnemyHealthOrMana(level):
    health = 50
    for i in range(1, level):
        health += randint(10, 30)
    return health


def chooseWeapon(player: Player):

    dist = abs(weapons[0].damage / 5 - player.health)
    weaponChoosed = (0, dist)
    for w in range(len(armors)):
        print(f"{weapons[w].damage / 5} - {player.health}")
        print(dist)
        dist = abs(weapons[w].damage/5 - player.health)
        if dist < weaponChoosed[1]:
            weaponChoosed = (w, dist)
    #return weaponChoosed[0]
    return 0


def chooseArmor(eHealth):
    dist = abs(armors[0].protection / 5 - eHealth)
    armorChoosed = (0, dist)
    for w in range(len(armors)):
        dist = abs(armors[w].protection/5 - eHealth)
        if dist < armorChoosed[1]:
            armorChoosed = (w, dist)
    #return armorChoosed[0]
    return 0


def chooseNumberPotions(level):
    i = randint(0, level) // 3
    return i


def generateEnnemy(player: Player):
    eLevel = randint(1, player.level+2)
    eAttack = 10 + eLevel - randint(0, eLevel)
    eDodge = eLevel - eAttack + 20
    eHealth = calculateEnnemyHealthOrMana(eLevel)
    eMana = calculateEnnemyHealthOrMana(eLevel)
    ePotion = chooseNumberPotions(eLevel)
    eArmor = armors[chooseArmor(eHealth)]
    eWeapon = weapons[chooseWeapon(player)]
    eStrength = randint(1, max(player.level-2, 1))
    ennemy = Ennemy(eHealth, eMana, eAttack, eDodge, eArmor, eWeapon, {"Health": ePotion}, [], eLevel, eStrength)
    return ennemy


def calculateXpLevels(level):
    xp = 0
    for i in range(1,level):
        xp += 100*i
    return xp


def playerTurn(player: Player, ennemy: Ennemy):
    print("Choose your action : 1 = attack | 2 = Drink a health potion")

    choice = int(input("Choose your action : 1 = attack | 2 = Drink a potion : "))
    while not (choice == 1 or choice == 2):
        choice = int(input("Enter a valid option !\nChoose your action : 1 = attack | 2 = Drink a potion : "))
    if choice == 1:
        if player.achieveAttack():
            damage = player.calculateDamage()
            ennemy.takeDamage(damage)
            print(f"You dealt {damage} damage points to your adversary")
        else:
            print("You missed your attack !")

    elif choice == 2:
        if player.potions["Health"] > 0:
            player.utilisePotion("Health")


def ennemyTurn(player: Player, ennemy: Ennemy):
    choice = ennemy.chooseStrategy()
    print(f"Ennemy choice is {choice}")
    if choice == 1:
        if ennemy.achieveAttack():
            damage = ennemy.calculateDamage()
            player.takeDamage(damage)
            print(f"The ennemy dealt you {damage} damage points !")
        else:
            print("The ennemy missed it's attack!")

    elif choice == 2:
        if ennemy.potions["Health"] > 0:
            ennemy.utilisePotion("Health")


class Combat:
    def __init__(self):
        self.rounds = 0

    def turn(self, ennemy: Ennemy, player: Player):
        print(f"Turn {self.rounds} !! :\n")
        initiative = randint(0, 1)
        print(player)
        print(ennemy)
        if initiative == 1:  # the player play first
            print(f"The player attacks first.")
            print(f"\nYour Turn :\n")
            playerTurn(player, ennemy)
            print(f"Enemy's Turn")
            ennemyTurn(player, ennemy)
        else:
            print(f"The ennemy attacks first.")
            print(f"Enemy's Turn")
            ennemyTurn(player, ennemy)
            print(f"\nYour Turn :\n")
            playerTurn(player, ennemy)
        pass

    def combat(self, player: Player):
        print("The fight will start !!!")
        ennemy = generateEnnemy(player)
        print(ennemy)
        while ennemy.health >= 0 and player.health >= 0:
            self.rounds += 1
            self.turn(ennemy, player)
        if player.health >= 0:
            player.gainXp(ennemy)
            if player.xp >= calculateXpLevels(player.level):
                player.levelUp()


player = Player(100, 100, 10, 10, 0, 1)
player.weapon = stick
player.armor = tunic

combat = Combat()
combat.combat(player)
