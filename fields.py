import cards
import philosophers
import players
from stack import Stack

class cardManager:
    def __init__(self):
        self.cardID = 0
        self.cards = []

    def __getCardID(self):
        self.cardID += 1
        return self.cardID

    def addCard(self, card) -> int:
        self.cards.append(card)
        return self.__getCardID()

    def getCard(self, id):
        if not (1 <= id <= len(self.cards)):
            return None
        return self.cards[id - 1]  # id is 1-indexed


class philosopherManager:
    def __init__(self):
        self.philosopherID = 0
        self.philosophers = []

    def __getPhilosopherID(self):
        self.philosopherID += 1
        return self.philosopherID

    def addPhilosopher(self, philosopher, player):
        self.philosophers.append(philosopher)
        philosopher.setPlayer(player)
        philosopher.setID(self.__getPhilosopherID())
        return philosopher

    def removePhilosopher(self, id):
        # remove 不会把哲学家从列表中移出，而是invalid = True
        self.philosophers[id - 1].invalid = True

    def getPhilosopher(self, id):
        if not (1 <= id <= len(self.philosophers)):
            return None
        return self.philosophers[id - 1]  # id is 1-indexed


class field:
    def __init__(self):
        self.state = 0  # [0: setup, 1: normal, -1: error]
        self.graveYard: [cards.basicCard] = []
        self.cardManager = cardManager()
        self.philosopherManager = philosopherManager()

        self.currentProcessingCard = None
        # 创建一个栈

        self.cardStack = Stack()

        self.playerID = 0
        self.players = []

    def startGame(self):
        if self.state != 0:
            return False, "Game already started"
        if len(self.getPlayers()) < 2:
            return False, "Not enough players"

        self.state = 1
        return True, self.state

    def __getPlayerID(self):
        self.playerID += 1
        return self.playerID

    def addPlayer(self, name):
        if self.state != 0:
            return False, "Game already started"

        player = players.player(name)
        player_id = self.__getPlayerID()
        player.setPlayerID(player_id)

        self.players.append(player)
        return True, player_id

    def getPlayer(self, id) -> players.player:
        return self.players[id - 1]  # id is 1-indexed

    def getPlayers(self):
        return self.players

    def getCardManager(self):
        return self.cardManager

    def getPhilosopherManager(self):
        return self.philosopherManager

    def checkValidCard(self, philosopher_id, card_id, target_id, energyCards: [int]):  # 检测出牌是否合法

        # 检测出牌哲学家
        philosopher: philosophers.basicPhilosopher = self.philosopherManager.getPhilosopher(philosopher_id)
        if not philosopher or philosopher.invalid:
            return False, "Philosopher is invalid"
        # 检测目标是否合法
        target = self.philosopherManager.getPhilosopher(target_id)
        if not target or target.invalid:
            return False, "Target is invalid"
        # 检测牌是否合法
        card: cards.basicCard = self.cardManager.getCard(card_id)
        if not card:
            return False, "Card is invalid"

        # energyCards: 出牌组合 比如有哲学家拥有 [1,1,1,3] 想打出一张耗费3的卡，则可以选择使用 [1,1,1] 或 [3] 来打出，此变量表达了用户选择的能量卡组合
        # 检测当前能量卡组合是否合法

        if not sum(energyCards) == card.cost:
            return False, "Energy cards are invalid"
        # 检测当前能量卡组合是否足够
        if not philosopher.checkValidEnergy(energyCards):
            return False, "Energy card combination is not valid"
#
        return True, "Success"

    def pushToCardStack(self, card):
        # 入栈
        self.cardStack.push(card)
        # 设置当前处理卡
        self.currentProcessingCard = card


Field = field()


def getField() -> field:
    return Field


def setField(f):
    global Field
    Field = f
