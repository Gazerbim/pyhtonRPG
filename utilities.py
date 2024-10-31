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
