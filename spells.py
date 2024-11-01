from character import *

class Spell:
    def __init__(self, name, manaCost, description):
        self.name = name
        self.description = description
        self.manaCost = manaCost
        # Player attributes
        self.isAttackProp = False
        self.attackAttribute = 0
        self.isFleeProp = False
        self.FleeAttribute = 0
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

    def applySpellToPlayer(self, ennemy: Ennemy, player: Player):
        if self.isEAttackProp:
            player.attack = max(player.attack + player.attack * self.eAttackAttribute/100, 0)
        else:
            player.attack = max(player.attack + self.eAttackAttribute, 0)

        if self.isEFleeProp:
            player.flee = max(player.flee + player.flee * self.eFleeAttribute / 100, 0)
        else:
            player.flee = max(player.flee + self.eFleeAttribute, 0)

        if self.isEStrengthProp:
            player.strength = max(player.strength + player.strength * self.eStrengthAttribute / 100, 0)
        else:
            player.strength = max(player.strength + self.eStrengthAttribute, 0)

        if self.isEDamageProp:
            player.health = max(player.health + player.health * self.eDamage / 100, 0)
        else:
            player.health = max(player.health + self.eDamage, 0)

        # Effect on Ennemy

        if self.isAttackProp:
            ennemy.attack = max(ennemy.attack + ennemy.attack * self.attackAttribute / 100, 0)
        else:
            ennemy.attack = max(ennemy.attack + self.attackAttribute, 0)

        if self.isFleeProp:
            ennemy.flee = max(ennemy.flee + ennemy.flee * self.fleeAttribute / 100, 0)
        else:
            ennemy.flee = max(ennemy.flee + self.fleeAttribute, 0)

        if self.isStrengthProp:
            ennemy.strength = max(ennemy.strength + ennemy.strength * self.strengthAttribute / 100, 0)
        else:
            ennemy.strength = max(ennemy.strength + self.strengthAttribute, 0)

        if self.isDamageProp:
            ennemy.health = max(ennemy.health + ennemy.health * self.damage / 100, 0)
        else:
            ennemy.health = max(ennemy.health + self.damage, 0)

    def applySpellToEnnemy(self, ennemy: Ennemy, player: Player):
        if self.isEAttackProp:
            ennemy.attack = max(ennemy.attack + ennemy.attack * self.eAttackAttribute / 100, 0)
        else:
            ennemy.attack = max(ennemy.attack + self.eAttackAttribute, 0)

        if self.isEFleeProp:
            ennemy.flee = max(ennemy.flee + ennemy.flee * self.eFleeAttribute / 100, 0)
        else:
            ennemy.flee = max(ennemy.flee + self.eFleeAttribute, 0)

        if self.isEStrengthProp:
            ennemy.strength = max(ennemy.strength + ennemy.strength * self.eStrengthAttribute / 100, 0)
        else:
            ennemy.strength = max(ennemy.strength + self.eStrengthAttribute, 0)

        if self.isEDamageProp:
            ennemy.health = max(ennemy.health + ennemy.health * self.eDamage / 100, 0)
        else:
            ennemy.health = max(ennemy.health + self.eDamage, 0)

        # Effect on Player

        if self.isAttackProp:
            player.attack = max(player.attack + player.attack * self.attackAttribute / 100, 0)
        else:
            player.attack = max(player.attack + self.attackAttribute, 0)

        if self.isFleeProp:
            player.flee = max(player.flee + player.flee * self.fleeAttribute / 100, 0)
        else:
            player.flee = max(player.flee + self.fleeAttribute, 0)

        if self.isStrengthProp:
            player.strength = max(player.strength + player.strength * self.strengthAttribute / 100, 0)
        else:
            player.strength = max(player.strength + self.strengthAttribute, 0)

        if self.isDamageProp:
            player.health = max(player.health + player.health * self.damage / 100, 0)
        else:
            player.health = max(player.health + self.damage, 0)

    def applySpell(self, isPlayer, ennemy: Ennemy, player: Player):
        if isPlayer:
            self.applySpellToEnnemy(ennemy, player)
        else:
            self.applySpellToPlayer(ennemy, player)








"""=========Spell definition==========="""

returnSpell = Spell("Mirror Spell", "Mirror spells", 100)


oneHpSpell = Spell("1 HP", "Set the ennemy's life to 1% and reduce your attack by 10", 100)  # met a un hp et debuff attack
oneHpSpell.isEDamageProp = True
oneHpSpell.eDamage = -99
oneHpSpell.attackAttribute = -10

