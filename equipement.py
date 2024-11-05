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

"""Player def"""
stick = Weapon(1, 100000, 0, 0, "Stick")
ironSword = Weapon(5, 100, 20, 0, "Iron Sword")
diamondSword = Weapon(20, 1000, 100, 0, "Diamond Sword")
energySword = Weapon(50, 5000, 500, 0, "Energy Sword")
masterSword = Weapon(100, 20000, 1000, 0, "Master Sword")
darkSword = Weapon(200, 50000, 1500, 0, "Dark Sword")
woodenSword = Weapon(3, 50, 5, 0, "Wooden Sword")
bronzeSword = Weapon(8, 200, 50, 0, "Bronze Sword")
silverSword = Weapon(15, 600, 75, 0, "Silver Sword")
platinumSword = Weapon(30, 1500, 300, 0, "Platinum Sword")
mythrilSword = Weapon(75, 10000, 750, 0, "Mythril Sword")
voidSword = Weapon(150, 40000, 2000, 0, "Void Sword")

weapons = [woodenSword,  ironSword, bronzeSword, silverSword, diamondSword, platinumSword, energySword, mythrilSword, masterSword, voidSword, darkSword]

tunic = Armor(1, 100000, 0, 0, "Tunic")
ironArmor = Armor(5, 100, 20, 0, "Iron Armor")
diamondArmor = Armor(10, 1000, 100, 0, "Diamond Armor")
energyArmor = Armor(25, 5000, 500, 0, "Energy Armor")
draconicArmor = Armor(50, 20000, 3000, 0, "Draconic Armor")
eternalArmor = Armor(100, 100000000000, 5000, 0, "Eternal Armor")
leatherArmor = Armor(2, 200, 10, 0, "Leather Armor")
chainmailArmor = Armor(7, 300, 30, 0, "Chainmail Armor")
steelArmor = Armor(12, 800, 150, 5, "Steel Armor")
adamantineArmor = Armor(20, 2000, 400, 0, "Adamantine Armor")
celestialArmor = Armor(40, 10000, 2000, 0, "Celestial Armor")
abyssalArmor = Armor(80, 60000, 4000, 0, "Abyssal Armor")

armors = [leatherArmor, ironArmor, chainmailArmor, diamondArmor, steelArmor, adamantineArmor, energyArmor, celestialArmor, draconicArmor, abyssalArmor, eternalArmor]

tabPotions = [("Health", 20), ("Mana", 20)]  # list of all types of potions (Name, price)

"""Ennemy def"""

estick = Weapon(1, 100000, 0, 0, "Stick")
eironSword = Weapon(5, 100, 20, 0, "Iron Sword")
ediamondSword = Weapon(20, 1000, 100, 0, "Diamond Sword")
eenergySword = Weapon(50, 5000, 500, 0, "Energy Sword")
emasterSword = Weapon(100, 20000, 1000, 0, "Master Sword")
edarkSword = Weapon(200, 50000, 1500, 0, "Dark Sword")
ewoodenSword = Weapon(3, 50, 5, 0, "Wooden Sword")
ebronzeSword = Weapon(8, 200, 50, 0, "Bronze Sword")
esilverSword = Weapon(15, 600, 75, 0, "Silver Sword")
eplatinumSword = Weapon(30, 1500, 300, 0, "Platinum Sword")
emythrilSword = Weapon(75, 10000, 750, 0, "Mythril Sword")
evoidSword = Weapon(150, 40000, 2000, 0, "Void Sword")

eweapons = [estick, ewoodenSword, eironSword, ebronzeSword, esilverSword, ediamondSword, eplatinumSword, eenergySword, emythrilSword, emasterSword, evoidSword, edarkSword]

etunic = Armor(1, 100000, 0, 0, "Tunic")
eironArmor = Armor(5, 100, 20, 0, "Iron Armor")
ediamondArmor = Armor(10, 1000, 100, 0, "Diamond Armor")
eenergyArmor = Armor(25, 5000, 500, 0, "Energy Armor")
edraconicArmor = Armor(50, 20000, 3000, 0, "Draconic Armor")
eeternalArmor = Armor(100, 100000000000, 5000, 0, "Eternal Armor")
eleatherArmor = Armor(2, 200, 10, 0, "Leather Armor")
echainmailArmor = Armor(7, 300, 30, 0, "Chainmail Armor")
esteelArmor = Armor(12, 800, 150, 5, "Steel Armor")
eadamantineArmor = Armor(20, 2000, 400, 0, "Adamantine Armor")
ecelestialArmor = Armor(40, 10000, 2000, 0, "Celestial Armor")
eabyssalArmor = Armor(80, 60000, 4000, 0, "Abyssal Armor")

earmors = [etunic, eleatherArmor, eironArmor, echainmailArmor, ediamondArmor, esteelArmor, eadamantineArmor, eenergyArmor, ecelestialArmor, edraconicArmor, eabyssalArmor, eeternalArmor]
