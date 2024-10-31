import os
import time
import string
import keyboard
from character import *

class ChooseWidget:
    def __init__(self):
        self.choice_list = []
        self.cursor = 0
        self.isRunning = True
        self.escaped = False

    def add_choice(self, choice):
        self.choice_list.append(choice)

    def debugShow(self):
        print("Choices : " + str(self.choice_list))
        print("Cursor : " + str(self.cursor))

    def keyListener(self):
        while True:
            if keyboard.is_pressed('up'):
                self.onUp()
                break

            if keyboard.is_pressed('down'):
                self.onDown()
                break

            if keyboard.is_pressed('enter'):
                self.onEnter()
                break

            if keyboard.is_pressed('esc'):
                self.isRunning = False
                self.escaped = True
                break

    def onEnter(self):
        self.isRunning = False

    def onUp(self):
        if self.cursor == 0:
            self.cursor = len(self.choice_list)-1
        else:
            self.cursor -= 1

    def onDown(self):
        if self.cursor == len(self.choice_list)-1:
            self.cursor = 0
        else:
            self.cursor += 1
        

    def display(self):
        for i in range(0, len(self.choice_list)):
            if i == self.cursor:
                print(str(i + 1) + " : " + self.choice_list[i] + " <--")
            
            else:
                print(str(i + 1) + " : " + self.choice_list[i])

    def run(self, prefix=""):
        while self.isRunning:
            #self.debugShow()
            if prefix:
                print(prefix)
            self.display()
            time.sleep(0.1)
            self.keyListener()
            os.system("cls")

        
        if not self.escaped:
            return self.cursor

class BigTitle:
    def __init__(self):
        self.font = [["■■■■■", "■■■■■", "■■■■■", "■■■■ ", "■■■■■", "■■■■■", " ■■■ ", "■   ■", "■■■■■", "■■■■■", "■   ■", "■    ", "■   ■", "■   ■", "■■■■■", "■■■■ ", "■■■■■", "■■■■ ", "■■■■■", "■■■■■", "■   ■", "■   ■", "■ ■ ■", "■   ■", "■   ■", "■■■■■"],
                     ["■   ■", "■   ■", "■    ", "■   ■", "■    ", "■    ", "■    ", "■   ■", "  ■  ", "  ■  ", "■  ■ ", "■    ", "■■ ■■", "■■  ■", "■   ■", "■   ■", "■   ■", "■   ■", "■    ", "  ■  ", "■   ■", "■   ■", "■ ■ ■", " ■ ■ ", " ■ ■ ", "   ■ "],
                     ["■   ■", "■■■■ ", "■    ", "■   ■", "■■■  ", "■■■  ", "■  ■■", "■■■■■", "  ■  ", "  ■  ", "■■   ", "■    ", "■ ■ ■", "■ ■ ■", "■   ■", "■   ■", "■ ■ ■", "■■■■■", "■■■■■", "  ■  ", "■   ■", "■   ■", "■ ■ ■", "  ■  ", "  ■  ", "  ■  "],
                     ["■■■■■", "■   ■", "■    ", "■   ■", "■    ", "■    ", "■   ■", "■   ■", "  ■  ", "  ■  ", "■ ■  ", "■    ", "■   ■", "■  ■■", "■   ■", "■■■■■", "■■■■■", "■ ■■ ", "    ■", "  ■  ", "■   ■", " ■ ■ ", " ■ ■ ", " ■ ■ ", "  ■  ", " ■   "],
                     ["■   ■", "■■■■■", "■■■■■", "■■■■ ", "■■■■■", "■    ", " ■■■ ", "■   ■", "■■■■■", "■■   ", "■   ■", "■■■■■", "■   ■", "■   ■", "■■■■■", "■    ", "   ■ ", "■   ■", "■■■■■", "  ■  ", "■■■■■", "  ■  ", " ■ ■ ", "■   ■", "  ■  ", "■■■■■"]]
    
    def printFont(self, text, separator = "\t"):
        alphabet = string.ascii_uppercase
        out = ""
        for i in range(0, 5):
            for c in text.upper():
                out += self.font[i][alphabet.index(c)] + separator
            out += "\n"
        
        print(out)

    def debugFont(self):
        for char in self.font:
            print(char+"\n")

"""def MakeStrip(title, outlines = "=", fill = " ", width = os.get_terminal_size()[0], height = 5):
    out = ""
    out += outlines*width + "\n"
    while len(out.split("\n")) != height//2 + 1:
        out += fill*width + "\n"
    
    out += title.center(width, fill)

    while len(out.split("\n")) != height - 1:
        out += fill*width + "\n"
    
    out += outlines*width + "\n"

    print(out)"""


def CenterText(text, fill = " "):
    for line in text.split("\n"):
        print(line.center(os.get_terminal_size()[0], fill))