import cards, players, fields
import philosophers
import skills


class basicEffect:
    def __init__(self, name, description, philosopher):
        self.name = name
        self.description = description
        self.philosopher = philosopher

        self.dead = False

    def update(self):
        pass

    def destroy(self):  # 待更新：1，移出哲学家状态区
        self.dead = True


class healEffect(basicEffect):
    def __init__(self, player, amount, turns):  # player 永远放在参数第一位
        self.name = "Heal Effect"
        self.description = f"Heals the player for {amount} HP for {turns} turns"
        super().__init__(self.name, self.description, player)
        self.amount = amount
        self.turnsLeft = turns

    def update(self):
        if self.turnsLeft:
            skills.addHP(self.philosopher, self.amount)
            self.turnsLeft -= 1
        else:
            self.destroy()
#

class damageEffect(basicEffect):
    def __init__(self, player, amount, turns):  # player 永远放在参数第一位
        self.name = "Damage Effect"
        self.description = f"Damage the player for {amount} HP for {turns} turns"
        super().__init__(self.name, self.description, player)
        self.amount = amount
        self.turnsLeft = turns

    def update(self):
        if self.turnsLeft:
            skills.loseHP(self.philosopher, self.amount)
            self.turnsLeft -= 1
        else:
            self.destroy()
