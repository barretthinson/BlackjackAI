__author__ = 'Barrett Hinson'


class Dealer(object):
    def __init__(self, strategy):
        self.hand = []
        self.finalValue = 0
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
            player.takeTurn(deck, self.hand)
        self.takeTurn(deck)

    def takeTurn(self, deck):
        handValue = 0
        acesAs11 = 0
        for card in self.hand:
            handValue += card.value
            if card.value == 11:
                acesAs11 += 1

        while handValue < 17 or (handValue <= 17 and self.strategy == "hit on soft 17s" and self.isSoft()):
            newCard = deck.draw()
            self.hand.append(newCard)
            handValue += newCard.value

            if newCard.value == 11:
                acesAs11 += 1

            if handValue > 21 and acesAs11 > 0:
                handValue -= 10  # make an ace count as 1 instead of 11
                acesAs11 -= 1
        self.finalValue = handValue

    def isSoft(self):
        for card in self.hand:
            if card.value == 11:
                return True
        return False
