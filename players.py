import philosophers, cards, fields, effects


class player:
    def __init__(self, name):
        self.name = name
        self.philosophers = []
        self.playerID = -1

    def setPlayerID(self,id):
        self.playerID = id

    def addPhilosopher(self, philosopher):
        newPhilosopher = philosopher(self)
        newPhilosopher.setPlayer(self)
        self.philosophers.append(newPhilosopher)
        