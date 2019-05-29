class Race:

    myRace = ''
    # abilities

    # actions
    def tactical(self, destinationTile):
        #activate
        if destinationTile.canActivate():
            #select ships
            fleet = None
            #move:
                #move ships
            destinationTile.activated(self.myRace, fleet)
                #pds
            #space combat
                #anti-fighter
                #retreat
                #fight
                #casualties
                #retreat
            #invasion
                #bombard
                #drop infantry
                #pds
                #fight
                #resolve victor
            #production
            return
        else:
            #refund action
            return

    def strategic(self):
        #primary
        #secondary
        return

    def actionCard(self):
        #action card
        return

    def endRound(self):
        #remove from turn tracker
        return
