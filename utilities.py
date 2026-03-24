import os
import character
import shutil
import sys

def list_files_in_directory(directory):
    # Vérifie si le répertoire existe
    if not os.path.exists(directory):
        print(f"The repertory '{directory}' does not exist.")
        return []

    # Récupère les noms de fichiers dans le répertoire
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

    return files



def flush_input():
    """Clear any pending input from the standard input buffer.

    This function ensures that no stale or unintended data remains in stdin
    before reading user input interactively. On Windows, it uses the msvcrt
    module to discard characters from the input buffer. On POSIX-compliant
    systems (e.g., Linux, macOS...), it uses select to check for available
    input without blocking and either discards the data by reading or flushes
    it using termios.tcflush if stdin is a terminal.
    """
    try:
        if os.name == "nt":
            import msvcrt  # pylint: disable=import-outside-toplevel

            # For Windows systems, Check if there is any pending input in the
            # buffer Discard characters one at a time until the buffer is empty.
            while msvcrt.kbhit():
                msvcrt.getch()
        elif os.name == "posix":
            import select  # pylint: disable=import-outside-toplevel

            # For Unix-like systems, check if there's any pending input in
            # stdin without blocking.
            stdin, _, _ = select.select([sys.stdin], [], [], 0)
            if stdin:
                if sys.stdin.isatty():
                    # pylint: disable=import-outside-toplevel
                    from termios import TCIFLUSH, tcflush

                    # Flush the input buffer
                    tcflush(sys.stdin.fileno(), TCIFLUSH)
                else:
                    # Read and discard input (in chunks).
                    while sys.stdin.read(1024):
                        pass
    except ImportError:
        pass

def clearTerminal():
    os.system('cls' if os.name == "nt" else 'clear')


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
