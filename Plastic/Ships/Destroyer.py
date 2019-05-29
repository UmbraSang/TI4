from Plastic.Ships import CapitalShip


class Destroyer(CapitalShip):

    def __init__(self):
        CapitalShip.__init__(self)
        # TODO: Refactor into visitor for unit upgrades?
        self.cost = 1
        self.numDice = 1
        self.hit = 9
        self.capacity = 0
        self.production = 0
        self.move = 2

        self.antiFighterDice = 2
        self.antiFighterHit = 9
        #

    def antiFighter(self):
        # Expand to be able to display rolls
        successes = 0
        for x in range(self.antiFighter):
            if self.roll() >= self.antiFighterHit:
                successes += 1
        return successes
