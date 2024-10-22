import philosophers, cards, fields


class player:
    def __init__(self, name):
        self.name = name
        self.philosophers = []

    def addPhilosopher(self, philosopher: philosophers.testPhilosopher):
        newPhilosopher = philosopher(self)
        newPhilosopher.setPlayer(self)
        self.philosophers.append(newPhilosopher)
