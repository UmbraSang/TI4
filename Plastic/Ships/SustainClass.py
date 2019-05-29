from Plastic.Ships import CapitalShip


class SustainClass(CapitalShip):
    health = 2  # change this to upper/lower space to keep singleton?

    def __init__(self):
        CapitalShip.__init__(self)

    def bombard(self):
        # TODO: review for PDS interaction
        if self.canBombard:
            # Expand to be able to display rolls
            successes = 0
            for x in range(self.numDice):
                if self.roll() >= self.hit:
                    successes += 1
            return successes
