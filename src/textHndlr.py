
def TextHndlr(text, player, room):
    if player.place == "start":
        player.place = "outside"
        player.name = "start"
        return f"Name your character!: "
    if player.place == "outside":
        player.name = text
        return f"Welcome {player.name}, this is the start of your adventure you are {room[player.place].name},{room[player.place].desc}. What direction would you like to go? (n,e,s,w) "
