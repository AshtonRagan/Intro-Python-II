# Implement a class to hold room information. This should have name and
# description attributes.


# room class should have a : name, desc, and a tuble/dict of directions

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.dirs = {"n": "empty", "e": "empty", "s": "empty", "w": "empty"}

    def setDir(self, n="empty", e="empty", s="empty", w="empty"):
        self.dirs["n"] = n
        self.dirs["e"] = e
        self.dirs["s"] = s
        self.dirs["w"] = w
