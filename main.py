from equipement import *
from character import *
from shop import *
from combat import *
from spells import *
from forms import *


def main():
    title = BigTitle()
    title.printFont("HARD")
    title.printFont("FIGHT")
    player = Player(100, 100, 10, 1, 0, 2)
    while player.health > 0:
        handleShop(player)
        combat = Combat()
        combat.combat(player)


# ability point

if __name__ == '__main__':
    main()
