from general import Combatant

class Human(Combatant):
    def __init__(self,name):
        super(Human, self).__init__(self)
        self.name = name
        self.health = 100
        self.strength = 10
        self.defense = 5
        self.description = "An ordinary human."

class Blighted(Combatant):
    def __init__(self,name):
        super(Blighted, self).__init__(self)
        self.name = name
        self.health = 150
        self.corruption = 80
        self.strength = 15
        self.description = "A common, run-of-the-mill victim of corruption. Teeming with the stuff, just looking at this creature feels wrong."
