from equipement import *
from character import *
from shop import *
from combat import *
from spells import *
from Widgets import *
import time

def main():
    title = BigTitle()
    clearTerminal()
    title.centerFont("HARD FIGHT")
    time.sleep(2)
    clearTerminal()
    player = Player(100, 100, 10, 1, 0, 2)
    while player.health > 0 and False:
        handleShop(player)
        combat = Combat()
        combat.combat(player)


# ability point

if __name__ == '__main__':
    main()
