from Plastic.Ships import CapitalShip


class Carrier(CapitalShip):

    def __init__(self):
        CapitalShip.__init__(self)
        # TODO: Refactor into visitor for unit upgrades?
        self.cost = 3
        self.numDice = 1
        self.hit = 9
        self.capacity = 4
        self.production = 0
        self.move = 1
        #
