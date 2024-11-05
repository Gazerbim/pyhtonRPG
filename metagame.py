from character import *
from Widgets import *
from utilities import *
from shop import *
from combat import *
import pickle
import os
import time


class Metagame:
    def __init__(self):
        self.metapoints = 0
        self.player = None
        self.isQuitting = False
        self.isPlayerLoaded = False

    def resetEquipement(self):
        for weapon in weapons:
            weapon.durability = weapon.maxDurability
        for armor in armors:
            armor.durability = armor.maxDurability

    def startNewGame(self):
        clearTerminal()
        self.player = Player(100, 100, 10, 1, 0, 1)
        self.resetEquipement()
        self.isPlayerLoaded = True

    def metaMenu(self):
        pass

    def runGame(self):
        while self.player.health > 0 and not self.player.quit:
            handleShop(self.player)
            if self.player.quit:
                break
            combat = Combat()
            combat.combat(self.player)
        if not self.player.quit:
            self.endRun()

    def endRun(self):
        pass

    def saveGame(self):
        self.player.quit = False
        if not os.path.exists("saves"):
            os.makedirs("saves")

        save_data = {
            'metapoints': self.metapoints,
            'player': self.player
        }

        with open(f"saves/{self.player.pseudo}_level_{self.player.level}.pkl", "wb") as save_file:
            pickle.dump(save_data, save_file)
        print(f"Game saved as {self.player.pseudo}_level_{self.player.level}")

    def loadGame(self):
        clearTerminal()
        directory = "saves"
        lst = list_files_in_directory(directory)
        widget = ChooseWidget()
        for n in lst:
            widget.add_choice(n)
        choice = widget.run()-1
        flush_input()
        try:
            # Charge l'état de la partie
            with open(f"saves/{lst[choice]}", "rb") as save_file:
                save_data = pickle.load(save_file)
            self.metapoints = save_data['metapoints']
            self.player = save_data['player']
            print(self.player.pseudo)
            print(f"Game loaded from {lst[choice]}")
            flush_input()
            input("Press enter to start...\n")
            self.isPlayerLoaded = True
        except FileNotFoundError:
            print("Save file not found.")

    def mainMenu(self):
        clearTerminal()
        title = BigTitle()
        title.centerFont("METARUNNERS")
        time.sleep(2)
        clearTerminal()
        widget = ChooseWidget()
        if self.isPlayerLoaded:
            widget.add_choice("Back to Game")
            widget.add_choice("Save Game")
        widget.add_choice("New Game")
        widget.add_choice("Load Game")
        widget.add_choice("Tutorial")
        widget.add_choice("Quit Game")
        return widget.run()

    def tuto(self):
        pass

    def launch(self):
        while not self.isQuitting:
            choice = self.mainMenu()
            flush_input()
            if choice == 1 and self.isPlayerLoaded:
                self.player.quit = False
                self.runGame()
            elif choice == 2 and self.isPlayerLoaded:
                self.saveGame()
            elif choice == 1:
                self.startNewGame()
                self.runGame()
            elif choice == 2:
                self.loadGame()
                self.runGame()
            elif choice == 3:
                self.tuto()
            elif choice == 4:
                self.isQuitting = True
                break
