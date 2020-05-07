from room import Room
from player import Player
from clear import clear_terminal
from textHndlr import *

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),

}


room["narrow"].setDir(n="treasure", w="foyer")
room["outside"].setDir(n="foyer")
room["foyer"].setDir(s="outside", n="overlook", e="narrow")
room["overlook"].setDir(s="foyer")
room["treasure"].setDir(s="narrow")


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def textTest(p, r):
    clear_terminal()
    global msg
    global error
    global empty
    if p.place == "intro":
        msg = "Welcome enter your name!: "
        return msg

    if p.place == "start":
        p.place = "outside"
        msg = f"{p.name} you start your adventure: {r[p.place].name}, {r[p.place].desc}\n what direction would you like to head in? (n,e,s,w)\n"
        return msg

    if error == True:
        error = False
        msg += "error pleasse try a valid option (n,e,s,w) or quit\n"
        return msg

    if empty == True:
        empty = False
        msg += "Sorry you can not go that way try a different direction (n,e,s,w)\n"
        return msg

    msg = f"{r[p.place].name}, {r[p.place].desc}\n what direction would you like to head in? (n,e,s,w)\n"
    return msg


def putTest(i, p, r):
    validInput = ["n", "e", "s", "w"]
    global error
    global empty
    if p.place == "intro":
        p.name = i
        p.place = "start"
        return

    if i in validInput:
        local = r[p.place].dirs[i]
        print(f"LOCAL: {local}")
    else:
        error = True
        return
    if local == "empty":
        empty = True
        return
    else:
        p.place = local


empty = False
error = False
msg = ""
p = Player("none", "intro")
# loop
while True:

    # text handler

    x = input(textTest(p, room))
    if x == "q" or x == "quit":
        clear_terminal()
        print("Game Ended")
        break

    # input handler
    putTest(x, p, room)
