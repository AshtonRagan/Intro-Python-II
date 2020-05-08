from room import Room
from item import useableItems
from player import Player
from clear import clear_terminal
from textHndlr import *
import textwrap

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", useableItems["birdSkull"]),

    'foyer': Room("Foyer", """Dim light filters in from the south, Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),

}

# prints an items, itype in a room.
# print(room["outside"].item.itype)

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


def textHand(p, r):
    clear_terminal()
    global msg
    global error
    global empty
    global look
    endln = "\n what direction would you like to head in? (n,e,s,w)\n"

    if p.place == "intro":
        msg = "Welcome enter your name!: "
        return msg

    if p.place == "start":
        p.place = "outside"
        msg = f"{p.name} you start your adventure: {r[p.place].name}, {r[p.place].desc}"
        return textwrap.fill(msg) + endln

    if error == True:
        error = False
        endln = "\nerror pleasse try a valid option (n,e,s,w) or quit\n"
        return msg + endln

    if empty == True:
        empty = False
        endln = "\nSorry you can not go that way try a different direction (n,e,s,w)\n"
        return msg + endln

    msg = f"You are at: {r[p.place].name}, {r[p.place].desc}"
    if look == True:
        look = False
        if r[p.place].item != "non":
            p.handleInv("add", r[p.place].item)
            msg += f"\nYou have found: {r[p.place].item.name}, and added it to your inventory"
        else:
            msg += f"\nAs you look around the room you find no items\n"
    return textwrap.fill(msg) + endln


def commandHand(i, p, r):
    validInput = ["n", "e", "s", "w"]
    global error
    global empty
    global game
    global look

    if i in ["q", "quit"]:
        game = False
        clear_terminal()
        print("Game Ended")

    if p.place == "intro":
        p.name = i
        p.place = "start"
        return

    if i in validInput:
        local = r[p.place].dirs[i]
    elif i in ["look", "inv", "stats"]:
        if i == "look":
            look = True
            return

    else:
        error = True
        return
    if local == "empty":
        empty = True
        return
    else:
        p.place = local


game = True
empty = False
error = False
look = False

msg = ""
hero = Player("none", "intro")
# loop
while game is True:

    # text handler
    userInput = input(textHand(hero, room))

    # input handler
    commandHand(userInput, hero, room)
