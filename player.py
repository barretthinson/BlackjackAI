__author__ = 'Barrett Hinson'

import ai


class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.finalValue = 0
        self.myAI = ai.Ai()

    def takeTurn(self, deck, dealerHand):
        hit = self.myAI.getChoice(self.hand, dealerHand)
        while hit:
            self.hand.append(deck.draw())
            hit = self.myAI.getChoice(self.hand, dealerHand)  # check ai's choice again with new hand

    def giveResult(self, win):
        pass
