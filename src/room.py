from item import Item

# Implement a class to hold room information. This should have name and
# description attributes.


# room class should have a : name, desc, and a tuble/dict of directions

class Room:
    def __init__(self, name, desc, item="non"):
        self.name = name
        self.desc = desc
        self.dirs = {"n": "", "e": "", "s": "", "w": ""}
        self.item = item

    def setDir(self, n="empty", e="empty", s="empty", w="empty"):
        self.dirs["n"] = n
        self.dirs["e"] = e
        self.dirs["s"] = s
        self.dirs["w"] = w
