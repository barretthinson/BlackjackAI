__author__ = 'Barrett Hinson'


class Dealer(object):
    def __init__(self, strategy):
        self.hand = []
        if strategy == 1:
            self.strategy = "stand on all 17s"
        else:
            self.strategy = "hit on soft 17s"

    def begin(self, deck, players):
        for i in range(2):
            for player in players:
                player.hand.append(deck.draw())
            self.hand.append(deck.draw())

    def deal(self, deck, players):
        for player in players:
            player.takeTurn(deck)
        self.takeTurn(deck)

    def takeTurn(self, deck):
        handValue = 0
        for card in self.hand:
            handValue += card.value

        while handValue < 17:
            newCard = deck.draw()
            self.hand.append(newCard)
            handValue += newCard.value

        if self.strategy == "hit on soft 17s" and handValue == 17 and self.isSoft():
            self.hand.append(newCard)

    def isSoft(self):
        for card in self.hand:
            if card.value == 11:
                return True
        return False
