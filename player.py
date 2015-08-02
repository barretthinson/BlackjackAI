__author__ = 'Barrett Hinson'

import ai


class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.finalValue = 0
        self.myAI = ai.Ai()

    def takeTurn(self, deck, dealerHand):
        hit = self.myAI.getFirstChoice(self.hand, dealerHand)
        while hit:
            self.hand.append(deck.draw())
            if self.bust():
                break
            hit = self.myAI.getChoice(self.hand, dealerHand)  # check ai's choice again with new hand
        self.finalValue = self.getHandValue()

    def giveResult(self, win):
        self.myAI.getResult(win)

    def bust(self):
        return self.getHandValue() > 21

    def getHandValue(self):
        acesAs11 = 0
        handValue = 0

        # calculates the current value of the hand
        for card in self.hand:
            handValue += card.value
            if card.value == 11:
                acesAs11 += 1

        # begins to count aces as 1 instead of 11 as necessary
        if handValue > 21 and acesAs11 > 0:
            for card in self.hand:
                if card.value == 11 and handValue > 21:
                    card.value = 1
                    handValue -= 10

        return handValue

    def getRecap(self, topNum):
        text = self.name+"'s "+self.myAI.recap(topNum)+"\n"
        return text
