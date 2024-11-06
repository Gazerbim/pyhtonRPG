from character import *
from Widgets import *
from utilities import *
from shop import *
from combat import *
import pickle
import os
import time
from random import randint


class Metagame:
    def __init__(self):
        self.metapoints = 0
        self.player = None
        self.isQuitting = False
        self.isPlayerLoaded = False
        self.pseudo = ""

        # base attributes for the beginning of a run
        self.baseHealth = 100
        self.baseMana = 100
        self.baseAttack = 10
        self.baseStrength = 1
        self.baseFlee = 1
        self.baseGold = 50
        self.numberBaseSpell = 1

        self.xpGained = 0

    def resetEquipement(self):
        for weapon in weapons:
            weapon.durability = weapon.maxDurability
        for armor in armors:
            armor.durability = armor.maxDurability

    def startNewGame(self):
        clearTerminal()
        self.pseudo = input("What is your nickname ? /!\ If you take a nickname that is already used it will delete the other player's save !: ")
        clearTerminal()
        self.player = Player(100, 100, 10, 1, 50, 1, self.pseudo)
        self.resetEquipement()
        self.isPlayerLoaded = True
        self.baseHealth = 100
        self.baseMana = 100
        self.baseAttack = 10
        self.baseStrength = 1
        self.baseFlee = 1
        self.baseGold = 50
        self.numberBaseSpell = 0
        self.xpGained = 0
        self.metapoints = 0

    def increaseBaseAttributes(self):
        while True:
            clearTerminal()
            widget = ChooseWidget()
            widget.setPrefix(f"Choose the attributes to increase.\nYou have {self.metapoints} MeP.\n")
            widget.add_choice(f"Increase base health ({self.baseHealth}) : 100 MeP")
            widget.add_choice(f"Increase base mana ({self.baseMana}) : 100 MeP")
            widget.add_choice(f"Increase base attack ({self.baseAttack}) : {200*(self.baseAttack-9)} MeP")
            widget.add_choice(f"Increase base flee ({self.baseFlee}) : {200*(self.baseFlee)} MeP")
            widget.add_choice(f"Increase base strength ({self.baseStrength}) : {100*(self.baseStrength)} MeP")
            widget.add_choice("Return to the meta-menu")
            choice = widget.run()
            if choice == 1 and self.metapoints >= 100:
                self.baseHealth += 5
                self.metapoints -= 100
            elif choice == 2 and self.metapoints >= 100:
                self.baseMana += 5
                self.metapoints -= 100
            elif choice == 3 and self.metapoints >= 200*(self.baseAttack-9):
                self.metapoints -= 200*(self.baseAttack-9)
                self.baseAttack += 1
            elif choice == 4 and self.metapoints >= 200*(self.baseFlee):
                self.metapoints -= 200*(self.baseFlee)
                self.baseFlee += 1
            elif choice == 5 and self.metapoints >= 100*(self.baseStrength):
                self.metapoints -= 100*(self.baseStrength)
                self.baseStrength += 1
            elif choice == 6:
                break

    def increaseStartingMoney(self):
        while True:
            clearTerminal()
            widget = ChooseWidget()
            widget.setPrefix(f"Choose what to increase.\nYou have {self.metapoints} MeP.\n")
            widget.add_choice(f"Increase base money by 10 ({self.baseGold}) : {self.baseGold*2} MeP")
            widget.add_choice(f"Increase base number of spells (max : {len(playerTierSpells[1])}) ({self.numberBaseSpell}) : {500*self.numberBaseSpell} MeP")
            widget.add_choice("Return to the meta-menu")
            choice = widget.run()
            if choice == 1 and self.metapoints >= self.baseGold*2:
                self.metapoints -= self.baseGold*2
                self.baseGold += 10
            elif choice == 2 and self.metapoints >= 500*self.numberBaseSpell and self.numberBaseSpell < len(playerTierSpells[1]):
                self.metapoints -= 500*self.numberBaseSpell
                self.numberBaseSpell += 1
            elif choice == 3:
                break

    def createPlayer(self):
        self.player = Player(self.baseHealth, self.baseMana, self.baseAttack, self.baseFlee, self.baseGold, self.baseStrength, self.pseudo)
        self.player.armor.durability = self.player.armor.maxDurability
        self.player.weapon.durability = self.player.weapon.maxDurability
        tabInd = []
        while len(tabInd) < self.numberBaseSpell:
            ind = randint(0, len(playerTierSpells[1])-1)
            if not (ind in tabInd):
                tabInd.append(ind)
        for i in tabInd:
            self.player.spells.append(playerTierSpells[1][i])

    def fullGame(self):
        while True:
            self.runGame()
            if self.player.quit:
                break
            self.metaMenu()
            self.createPlayer()

    def metaMenu(self):
        while True:
            clearTerminal()
            widget = ChooseWidget()
            widget.add_choice("Increase base attributes")
            widget.add_choice("Increase starting money or number of starting spells")
            widget.add_choice("Create spells [NOT WORKING]")
            widget.add_choice("Start a new run")
            widget.setPrefix(f"Congratulations! You finished a run!\nThis is the meta-menu, where you can buy persistent upgrades for your character.\nYou currently have {self.metapoints} metapoints.\n")
            choice = widget.run()-1
            if choice == 0:
                self.increaseBaseAttributes()
            if choice == 1:
                self.increaseStartingMoney()
            if choice == 2:
                # self.createSpell()
                pass
            if choice == 3:
                break


    def runGame(self):
        while self.player.health > 0 and not self.player.quit:
            handleShop(self.player)
            if self.player.quit:
                break
            combat = Combat()
            self.xpGained += combat.combat(self.player)
        if not self.player.quit:
            self.metapoints += self.xpGained
            self.endRun()

    def endRun(self):  # all the stuff that will prepare another game
        self.xpGained = 0


    def saveGame(self):
        self.player.quit = False
        if not os.path.exists("saves"):
            os.makedirs("saves")

        save_data = {
            'baseGold': self.baseGold,
            'baseFlee': self.baseFlee,
            'baseMana': self.baseMana,
            'baseAttack': self.baseAttack,
            'baseHealth': self.baseHealth,
            'baseStrength': self.baseStrength,
            'numberBaseSpell': self.numberBaseSpell,
            'xpGained': self.xpGained,
            'metapoints': self.metapoints,
            'player': self.player,
            'pseudo': self.pseudo
        }

        with open(f"saves/{self.player.pseudo}.pkl", "wb") as save_file:
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
            self.baseGold = save_data['baseGold']
            self.baseFlee = save_data['baseFlee']
            self.baseMana = save_data['baseMana']
            self.baseAttack = save_data['baseAttack']
            self.baseHealth = save_data['baseHealth']
            self.baseStrength = save_data['baseStrength']
            self.numberBaseSpell = save_data['numberBaseSpell']
            self.xpGained = save_data['xpGained']
            self.pseudo = save_data['pseudo']
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
            if self.isPlayerLoaded:
                if choice == 1:
                    self.player.quit = False
                    self.fullGame()
                elif choice == 2:
                    self.saveGame()
                elif choice == 3:
                    self.startNewGame()
                    self.fullGame()
                elif choice == 4:
                    self.loadGame()
                    self.fullGame()
                elif choice == 5:
                    self.tuto()
                elif choice == 6:
                    self.isQuitting = True
                    exit()
            else:
                if choice == 1:
                    self.startNewGame()
                    self.fullGame()
                elif choice == 2:
                    self.loadGame()
                    self.fullGame()
                elif choice == 3:
                    self.tuto()
                elif choice == 4:
                    self.isQuitting = True
