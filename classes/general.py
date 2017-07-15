class Combatant(object):
    def __init__(self,name):
        self.name = name
        self.health = 1
        self.corruption = 0
        self.strength = 0
        self.defense = 0
        self.description = "Nothing to write home about."
    def displayStats(self):
        # print("__________________")
        print("HP: "+str(self.health))
        print("Str: "+str(self.strength))
        print("Def: "+str(self.defense))
        print("")
        # print("__________________")
    def attack(self, target):
        target.health -= (self.strength - target.defense)
        # print(target.name+" took "+str(self.strength)+" damage")
        return target.health
    def die(self, description = " was killed!"):
        if (self.health < 1):
            print(self.name + description)
