import os
import string

class BigTitle:
    def __init__(self):
        self.font = [["■■■■■", "■■■■■", "■■■■■", "■■■■ ", "■■■■■", "■■■■■", " ■■■ ", "■   ■", "■■■■■", "■■■■■", "■   ■", "■    ", "■   ■", "■   ■", "■■■■■", "■■■■ ", "■■■■■", "■■■■ ", "■■■■■", "■■■■■", "■   ■", "■   ■", "■ ■ ■", "■   ■", "■   ■", "■■■■■", "     "],
                     ["■   ■", "■   ■", "■    ", "■   ■", "■    ", "■    ", "■    ", "■   ■", "  ■  ", "  ■  ", "■  ■ ", "■    ", "■■ ■■", "■■  ■", "■   ■", "■   ■", "■   ■", "■   ■", "■    ", "  ■  ", "■   ■", "■   ■", "■ ■ ■", " ■ ■ ", " ■ ■ ", "   ■ ", "     "],
                     ["■   ■", "■■■■ ", "■    ", "■   ■", "■■■  ", "■■■  ", "■  ■■", "■■■■■", "  ■  ", "  ■  ", "■■   ", "■    ", "■ ■ ■", "■ ■ ■", "■   ■", "■   ■", "■ ■ ■", "■■■■■", "■■■■■", "  ■  ", "■   ■", "■   ■", "■ ■ ■", "  ■  ", "  ■  ", "  ■  ", "     "],
                     ["■■■■■", "■   ■", "■    ", "■   ■", "■    ", "■    ", "■   ■", "■   ■", "  ■  ", "  ■  ", "■ ■  ", "■    ", "■   ■", "■  ■■", "■   ■", "■■■■■", "■■■■■", "■ ■■ ", "    ■", "  ■  ", "■   ■", " ■ ■ ", " ■ ■ ", " ■ ■ ", "  ■  ", " ■   ", "     "],
                     ["■   ■", "■■■■■", "■■■■■", "■■■■ ", "■■■■■", "■    ", " ■■■ ", "■   ■", "■■■■■", "■■   ", "■   ■", "■■■■■", "■   ■", "■   ■", "■■■■■", "■    ", "   ■ ", "■   ■", "■■■■■", "  ■  ", "■■■■■", "  ■  ", " ■ ■ ", "■   ■", "  ■  ", "■■■■■", "     "]]
    
    def printFont(self, text, separator = "\t"):
        alphabet = string.ascii_uppercase + " "
        out = ""
        for i in range(0, 5):
            for c in text.upper():
                out += self.font[i][alphabet.index(c)] + separator
            out += "\n"
        
        print(out)

    def centerFont(self, text, separator = "\t"):
        alphabet = string.ascii_uppercase + " "
        out = ""
        for i in range(0, int(os.get_terminal_size()[1]/2-4)):
            out += "\n"

        for i in range(0, 5):
            for c in text.upper():
                out += self.font[i][alphabet.index(c)] + separator

            out += "\n"

        for i in range(0, int(os.get_terminal_size()[1]/2-4)):
            out += "\n"

        print(out)


    def debugFont(self):
        for char in self.font:
            print(char+"\n")

def MakeStrip(title, outlines = "=", fill = " ", width = os.get_terminal_size()[0], height = 5):
    out = ""
    out += outlines*width + "\n"
    while len(out.split("\n")) != height//2 + 1:
        out += fill*width + "\n"
    
    out += title.center(width, fill)

    while len(out.split("\n")) != height - 1:
        out += fill*width + "\n"
    
    out += outlines*width + "\n"

    print(out)


def CenterText(text, fill = " "):
    for line in text.split("\n"):
        print(line.center(os.get_terminal_size()[0], fill))