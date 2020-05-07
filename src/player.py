# Write a class to hold player information, e.g. what room they are in
# currently.

# player class needs: name=string, health=int, inventory=list, place=string


class Player:
    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.health = 100
        self.inventory = []

    def setHealth(self, num):
        self.health = num

    def handleInv(self, action, item):
        if action == "add":
            self.inventory.append(item)
        elif action == "del":
            for i in self.inventory:
                if i == item:
                    self.inventory.remove(item)
                    return
                return print(f"item:{item} Was not found")
        else:
            return print(f"{action} Not a valid action!")
