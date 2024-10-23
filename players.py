import philosophers, cards, fields, effects


class player:
    def __init__(self, name):
        self.name = name
        self.philosophers = []

    def addPhilosopher(self, philosopher):
        newPhilosopher = philosopher(self)
        newPhilosopher.setPlayer(self)
        self.philosophers.append(newPhilosopher)
