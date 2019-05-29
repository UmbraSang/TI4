from Board.Hazards import Hazard


class SuperNova(Hazard):

    def entry(self, ship):
        ship.isDead = True
        return
