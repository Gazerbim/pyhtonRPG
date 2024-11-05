import os
import msvcrt
import character
import shutil


def list_files_in_directory(directory):
    # Vérifie si le répertoire existe
    if not os.path.exists(directory):
        print(f"The repertory '{directory}' does not exist.")
        return []

    # Récupère les noms de fichiers dans le répertoire
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

    return files


def flush_input():
    try:
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


def clearTerminal():
    os.system('cls')


def MakeStripes(title, outlines="=", fill=" ", width=shutil.get_terminal_size().columns, height=5):
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