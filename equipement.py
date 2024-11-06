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
ironSword = Weapon(10, 100, 20, 0, "Iron Sword")
diamondSword = Weapon(40, 1000, 100, 0, "Diamond Sword")
energySword = Weapon(100, 5000, 500, 0, "Energy Sword")
masterSword = Weapon(200, 20000, 1000, 0, "Master Sword")
darkSword = Weapon(400, 50000, 1500, 0, "Dark Sword")
woodenSword = Weapon(5, 50, 5, 0, "Wooden Sword")
bronzeSword = Weapon(20, 200, 50, 0, "Bronze Sword")
silverSword = Weapon(30, 600, 75, 0, "Silver Sword")
platinumSword = Weapon(60, 1500, 300, 0, "Platinum Sword")
mythrilSword = Weapon(150, 10000, 750, 0, "Mythril Sword")
voidSword = Weapon(300, 40000, 2000, 0, "Void Sword")

weapons = [woodenSword,  ironSword, bronzeSword, silverSword, diamondSword, platinumSword, energySword, mythrilSword, masterSword, voidSword, darkSword]

tunic = Armor(1, 100000, 0, 0, "Tunic")
ironArmor = Armor(7, 100, 20, 0, "Iron Armor")
diamondArmor = Armor(15, 1000, 100, 0, "Diamond Armor")
energyArmor = Armor(40, 5000, 500, 0, "Energy Armor")
draconicArmor = Armor(70, 20000, 3000, 0, "Draconic Armor")
eternalArmor = Armor(150, 100000000000, 5000, 0, "Eternal Armor")
leatherArmor = Armor(3, 200, 10, 0, "Leather Armor")
chainmailArmor = Armor(10, 300, 30, 0, "Chainmail Armor")
steelArmor = Armor(20, 800, 150, 5, "Steel Armor")
adamantineArmor = Armor(30, 2000, 400, 0, "Adamantine Armor")
celestialArmor = Armor(50, 10000, 2000, 0, "Celestial Armor")
abyssalArmor = Armor(100, 60000, 4000, 0, "Abyssal Armor")

armors = [leatherArmor, ironArmor, chainmailArmor, diamondArmor, steelArmor, adamantineArmor, energyArmor, celestialArmor, draconicArmor, abyssalArmor, eternalArmor]

tabPotions = [("Health", 20), ("Mana", 20)]  # list of all types of potions (Name, price)

"""Ennemy def"""

estick = Weapon(1, 100000, 0, 0, "Stick")
eironSword = Weapon(10, 100, 20, 0, "Iron Sword")
ediamondSword = Weapon(40, 1000, 100, 0, "Diamond Sword")
eenergySword = Weapon(100, 5000, 500, 0, "Energy Sword")
emasterSword = Weapon(200, 20000, 1000, 0, "Master Sword")
edarkSword = Weapon(400, 50000, 1500, 0, "Dark Sword")
ewoodenSword = Weapon(5, 50, 5, 0, "Wooden Sword")
ebronzeSword = Weapon(20, 200, 50, 0, "Bronze Sword")
esilverSword = Weapon(30, 600, 75, 0, "Silver Sword")
eplatinumSword = Weapon(60, 1500, 300, 0, "Platinum Sword")
emythrilSword = Weapon(150, 10000, 750, 0, "Mythril Sword")
evoidSword = Weapon(300, 40000, 2000, 0, "Void Sword")

eweapons = [estick, ewoodenSword, eironSword, ebronzeSword, esilverSword, ediamondSword, eplatinumSword, eenergySword, emythrilSword, emasterSword, evoidSword, edarkSword]

etunic = Armor(1, 100000, 0, 0, "Tunic")
eironArmor = Armor(7, 100, 20, 0, "Iron Armor")
ediamondArmor = Armor(15, 100, 100, 0, "Diamond Armor")
eenergyArmor = Armor(40, 5000, 500, 0, "Energy Armor")
edraconicArmor = Armor(70, 20000, 3000, 0, "Draconic Armor")
eeternalArmor = Armor(150, 100000000000, 5000, 0, "Eternal Armor")
eleatherArmor = Armor(3, 200, 10, 0, "Leather Armor")
echainmailArmor = Armor(10, 300, 30, 0, "Chainmail Armor")
esteelArmor = Armor(20, 800, 150, 5, "Steel Armor")
eadamantineArmor = Armor(30, 2000, 400, 0, "Adamantine Armor")
ecelestialArmor = Armor(50, 10000, 2000, 0, "Celestial Armor")
eabyssalArmor = Armor(100, 60000, 4000, 0, "Abyssal Armor")

earmors = [etunic, eleatherArmor, eironArmor, echainmailArmor, ediamondArmor, esteelArmor, eadamantineArmor, eenergyArmor, ecelestialArmor, edraconicArmor, eabyssalArmor, eeternalArmor]
