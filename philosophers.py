import cards, fields, players


class basicPhilosopher:
    def __init__(self, name, description=None, player=None):
        self.name = name
        self.player = player
        self.description = description
        self.hp = 10
        self.energyCards: [cards.energyCard] = []

    def setPlayer(self, player: players.player):
        self.player = player

    def addEnergy(self, energyCard: cards.energyCard):
        self.energyCards.append(energyCard)

    def loseEnergy(self, energyCard: cards.energyCard):
        self.energyCards.remove(energyCard)

    def addHP(self, hp: int):
        self.hp += hp

    def loseHP(self, hp: int):
        self.hp -= hp


class testPhilosopher(basicPhilosopher):
    def __init__(self, player: players.player):
        self.name = "testPhilosopher"
        self.description = "This is a test."
        super().__init__(self.name, description=self.description, player=player)
