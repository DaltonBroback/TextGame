from races import Human, Blighted

class Scabbard(Human):
    def __init__(self):
        super(Scabbard, self).__init__(self)
        self.name = "Scabbard"
        self.health = 105
        self.strength = 20
        self.description = "A naive young hero chosen by a pixie to purify the world. His quest is a dangerous one, but he is prepared to do whatever it takes to complete it."

class Scab(Blighted):
    def __init__(self):
        super(Scab, self).__init__(self)
        self.name = "Scab"
        self.description = "Once an idealistic hero, Scabbard was betrayed by his pixie companion and corrupted as a consequence. In spite of everything he still wants to fight the good fight and use his destructive powers to protect the world."

class Cicatriz(Human):
    def __init__(self):
        super(Cicatriz, self).__init__(self)
        self.name = "Cicatriz"
        self.strength = 7
        self.defense = 20
        self.corruption = 20
        self.description = "A troubled girl from the lowlands, clever and quick witted. Talks her way out of most situations, but won't shy away from what needs to be done. Despite her kind heart, her mind is troubled and susceptible to corruption."

class Jurh(Human):
    def __init__(self):
        super(Jurh, self).__init__(self)
        self.name = "Jurh"
        self.defense = 30
        self.strength = 30
        self.description = "Noble of mind and strong of both heart and body, he has lost much more than a person should ever have to. He has outlived everyone he's ever known, however he has turned his tragedy into motivation."

class Sosho(Human):
    def __init__(self):
        super(Sosho, self).__init__(self)
        self.name = "Sosho"
        self.defense = 3
        self.corruption = -100
        self.description = "Shy and straightforward, and more than a little strange, Sosho has never seen the devestation of corruption firsthand, but the science of it fascinates her. She studied it independently and developed many rudimentary remedies, she has a natural immunity to corruption."
