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

tabPotions = [("Health", 20), ("Mana", 20)]  # list of all types of potions (Name, price)
