

class Item:
    def __init__(self, name, desc, itype="useable"):
        self.name = name
        self.desc = desc
        self.itype = itype

    def __str__(self):
        return f"{self.name}, {self.desc}"

useableItems = {
    "birdSkull": Item("Bird Skull", "An old dingy skull belonging to a bird of some sorts"),
    "rustyKey": Item("Rusty Key", "An old key, very worn down.")
}
