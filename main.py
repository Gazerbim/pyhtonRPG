from character import *
from utilities import *
from shop import *
from combat import *
from Widgets import *
import time

def main():
    title = BigTitle()
    clearTerminal()
    title.centerFont("METARUNNERS")
    time.sleep(2)
    clearTerminal()
    player = Player(100, 100, 10, 1, 0, 2)
    player.xp = 100
    player.spells = [heal]
    while player.health > 0 and True:
        handleShop(player)
        combat = Combat()
        combat.combat(player)


# meta point

if __name__ == '__main__':
    main()
