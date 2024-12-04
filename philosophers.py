import cards, fields, players, effects


class basicPhilosopher:
    def __init__(self, name, description=None, player=None):
        self.invalid = False
        self.id = -1
        self.name = name
        self.player = player
        self.description = description
        self.hp = 10
        self.energyCards: [cards.energyCard] = []
        self.effects: [effects.basicEffect] = []

    def setID(self, id):
        print(f"philosopher {id} set")
        self.id = id
    def getPlayer(self):
        return self.player

    def setPlayer(self, player: players.player):
        self.player = player

    def reduceEnergy(self, energyCards: [int]):
        print(f"reduceEnergy receive cards: {energyCards}")
        # energyCards: 能量卡排列组合
        energyCardsRemain = energyCards[:]
        for energyCard in self.energyCards:
            if energyCard.used:
                continue
            if energyCard.energy in energyCardsRemain:
                energyCard.use()
                energyCardsRemain.remove(energyCard.energy)
                print(f"set energyCard {energyCard.id} used")

        if len(energyCardsRemain) != 0:
            print("False")
            return False

        print("True")
        return True


    def checkValidEnergy(self, energyCards: [int]):

        # energyCards: 能量卡排列组合
        # 统计能量卡组合
        requiredEnergyCards = {}  # {1: 3} 三张1能量的卡 or {3: 1} 一张3能量的卡
        for energy in energyCards:
            if energy not in requiredEnergyCards:
                requiredEnergyCards[energy] = 0
            requiredEnergyCards[energy] += 1

        # 统计合法能量卡
        validEnergyCards = {}  # {1: 3, 2: 1, 3: 2}
        for energyCard in self.energyCards:
            if not energyCard.used:
                if energyCard.energy not in validEnergyCards:
                    validEnergyCards[energyCard.energy] = 0
                validEnergyCards[energyCard.energy] += 1

        # 统计能量卡组合是否为合法能量卡的一个子集
        print(f"requiredEnergyCards: {requiredEnergyCards}, valid: {validEnergyCards}")
        for cost in requiredEnergyCards:
            if (cost not in validEnergyCards) or validEnergyCards[cost] < requiredEnergyCards[cost]:
                return False

        return True

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


PhilosopherTypeToPhilosopher = {1: testPhilosopher}
