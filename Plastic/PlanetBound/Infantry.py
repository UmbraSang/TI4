from Plastic import FootSoldier


class Infantry(FootSoldier):
    genSynth = 0

    def __init__(self):
        FootSoldier.__init__(self)
        # TODO: Refactor into visitor for unit upgrades?
        self.cost = 1
        self.numDice = 1
        self.hit = 8
        self.capacity = 0
        self.production = 0
        #

    def death(self):
        if self.roll() >= self.genSynth:
            self.location = None
            #TODO: change to purgatory then implement checks for planet placement
