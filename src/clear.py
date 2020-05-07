from os import system, name

# Credit to 2020 Lambda School Tl: Michael Nunes


def clear_terminal():
    if name == "nt":
        # Windows
        system("cls")
    else:
        # Linux / Mac
        system("clear")
