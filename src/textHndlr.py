from clear import clear_terminal
import textwrap



def textHndlr(p, r):
    clear_terminal()
    global msg
    global error
    global empty
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
    return textwrap.fill(msg) + endln
