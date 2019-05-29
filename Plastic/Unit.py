import random


class Unit:
    owner = None
    # change to reinforcements before assignment
    location = None
    health = 1  # change this to upper/lower space to keep singleton?

    cost = None
    numDice = None
    hit = None
    capacity = None
    production = None

    def __init__(self):
        # something useful
        x = 0

    def attack(self):
        # Expand to be able to display rolls
        successes = 0
        for x in range(self.numDice):
            if self.roll() >= self.hit:
                successes += 1
        return successes

    def roll(self):
        return random.randint(1, 10)

    def death(self):
        # self.location change/update
        return
