import cards, fields, players, effects


class basicPhilosopher:
    def __init__(self, name, description=None, player=None):
        self.name = name
        self.player = player
        self.description = description
        self.hp = 10
        self.energyCards: [cards.energyCard] = []
        self.effects: [effects.basicEffect] = []

    def setPlayer(self, player: players.player):
        self.player = player

    def addEnergy(self, energyCard):
        self.energyCards.append(energyCard)

    def loseEnergy(self, energyCard):
        self.energyCards.remove(energyCard)

    def addHP(self, hp: int):
        self.hp += hp

    def loseHP(self, hp: int):
        self.hp -= hp

    def setHP(self, hp: int):
        self.hp = hp

    def addEffect(self, effect):
        self.effects.append(effect)

    def updateEffects(self):
        new_effects = []
        for effect in self.effects:
            effect: effects.basicEffect

            effect.update()
            if effect.dead:  # 状态结束
                continue

            new_effects.append(effect)


class testPhilosopher(basicPhilosopher):
    def __init__(self, player: players.player):
        self.name = "testPhilosopher"
        self.description = "This is a test."
        super().__init__(self.name, description=self.description, player=player)
