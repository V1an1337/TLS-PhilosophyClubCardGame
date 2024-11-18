import philosophers, fields, players, effects, skills
from enum import Enum


class state(Enum):
    chooseTarget = 0
    becomingTarget = 1
    determinedTarget = 2
    becomedTarget = 3
    useStart = 4
    using = 5
    useEnd = 6
    useAfter = 7


Field = fields.getField()
CardManager = Field.getCardManager()
PhilosopherManager = Field.getPhilosopherManager()


class basicCard:
    def __init__(self, name, description, cost: int):
        self.id = CardManager.addCard(self)

        self.name = name
        self.description = description
        self.cost = cost  # 耗费一张能量值为n的能量卡

        self.attacker = None
        self.target = None
        self.state = 0  # [指定目标时，成为目标时，指定目标后，成为目标后，使用结算开始，使用结算，使用结算结束，使用结算后]
        self.finished = False

        self.respondedCards = [] # 可以并只能响应此牌的卡（不包含无懈可击，转移目标等）

    def use(self, attacker, target):
        self.attacker = attacker
        self.target = target

    def canBeRespondedBy(self, card):
        if type(card) in self.respondedCards:
            return True
        return False

    def chooseTarget(self, attacker, target):  # 指定目标时
        self.state = 0

        # check targetID is valid
        self.attacker, self.target = attacker, target
        if self.target:
            self.state = 1
            self.becomingTarget()

    def becomingTarget(self):  # 成为目标时：等待目标可被响应的过程
        self.state = 1
        # 无转移目标
        self.determinedTarget()


    def determinedTarget(self):  # 指定目标后
        self.state = 2
        self.becomedTarget()

    def becomedTarget(self):  # 成为目标后
        self.state = 3
        if len(self.respondedCards) == 0:
            self.useStart()
        else:
            # 等待目标出牌
            # 如果目标卡牌 invalid，则进入useStart
            pass

    def useStart(self):  # 使用结算开始
        self.state = 4
        self.using()

    def using(self):  # 使用结算
        self.state = 5
        self.use(self.attacker, self.target)
        self.useEnd()

    def useEnd(self):  # 使用结算结束
        self.state = 6
        self.useAfter()

    def useAfter(self):  # 使用结算后
        self.state = 7
        self.finish()
        # 若装备牌，则置入装备区

    def finish(self):
        self.finished = True


class energyCard(basicCard):
    name = "Energy Card"
    description = f"Give you N energy"
    cost = 0

    def __init__(self, philosopher, energy):  # philosopher 永远放在参数第一位, player同理

        super().__init__(self.name, self.description, self.cost)
        self.energy = energy
        self.philosopher = philosopher
        self.used = False

    def add(self, target=None):
        if not target:
            target = self.philosopher
        target.addEnergy(self)

    def reset(self):
        self.used = False

    def use(self, attakcer=None, target=None):  # Add Energy card to philosopher
        self.used = True


class hpCard(basicCard):
    name = "HP Card"
    description = f"Give you N hp"
    cost = 1

    def __init__(self, hp):
        super().__init__(self.name, self.description, self.cost)
        self.hp = hp

    def use(self, attacker, target=None):
        self.attacker = attacker
        self.target = target
        if not target:
            target = attacker
        skills.addHP(target)


class attackCard(basicCard):
    name = "Attack Card"
    description = f"Attack a player"
    cost = 1

    def __init__(self):
        super().__init__(self.name, self.description, self.cost)

        # self.canBeRespondedBy = [healCard]

    def use(self, attacker, target):
        self.attacker = attacker
        self.target = target
        skills.attack(attacker, target)


class healCard(basicCard):
    name = "Heal Card"
    description = f"Give a 3-rounds heal effect to a player"
    cost = 1

    def __init__(self):
        super().__init__(self.name, self.description, self.cost)

    def use(self, attacker, target=None):
        self.attacker = attacker
        self.target = target
        if not target:
            target = attacker
        effect = effects.healEffect(target, 1, 3)
        target.addEffect(effect)
