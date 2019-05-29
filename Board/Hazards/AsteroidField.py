from Board.Hazards import Hazard


class AsteroidField(Hazard):

    def entry(self, ship):
        ship.isDead = True
        return
