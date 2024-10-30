from equipement import *
from character import *
from shop import *
from combat import *
from spells import *


def main():
    player = Player(100, 100, 10, 1, 0, 2)
    while player.health > 0:
        handleShop(player)
        combat = Combat()
        combat.combat(player)


if __name__ == '__main__':
    main()
