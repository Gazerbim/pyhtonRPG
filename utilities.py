import os
import msvcrt

def flush_input():
    try:
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def clearTerminal():
    os.system('cls')

def MakeStripes(title, outlines="=", fill=" ", width=os.get_terminal_size()[0], height=5):
    out = ""
    out += outlines * width + "\n"
    while len(out.split("\n")) != height // 2 + 1:
        out += fill * width + "\n"

    out += title.center(width, fill)

    while len(out.split("\n")) != height - 1:
        out += fill * width + "\n"

    out += outlines * width + "\n"

    print(out)


def CenterText(text, fill=" "):
    for line in text.split("\n"):
        print(line.center(os.get_terminal_size()[0], fill))