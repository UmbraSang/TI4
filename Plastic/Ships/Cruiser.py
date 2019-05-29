from Plastic.Ships import CapitalShip


class Cruiser(CapitalShip):

    def __init__(self):
        CapitalShip.__init__(self)
        # TODO: Refactor into visitor for unit upgrades?
        self.cost = 2
        self.numDice = 1
        self.hit = 7
        self.capacity = 0
        self.production = 0
        self.move = 2
        #
