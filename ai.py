__author__ = 'Barrett Hinson'
import random


class Strategy(object):
    def __init__(self, incStrat):
        self.incStrat = incStrat
        self.hitLessThan = random.randint(2, 20)
        self.dealerShowing = random.randint(1, 11)
        self.hitOnSoft = random.randint(0, 1) # binary choice to hit or stay on a soft hand
        self.andCondition = random.randint(0, 1) # binary choice to and/or the two determinants
        # binary choice on whether we care if the dealer's shown is above or below our threshold
        self.dealerAbove = random.randint(0, 1)

    def doHit(self, hand):
        if self.incStrat is None:
            return self.myStrat(hand)
        else:
            self.hitLessThan = (self.hitLessThan + self.incStrat.hitLessThan) // 2
            self.dealerShowing = (self.dealerShowing + self.incStrat.dealerShowing) // 2
            return self.myStrat(hand)

    def myStrat(self, hand, dealerHand):
        acesAs11 = 0
        handValue = 0

        # calculates the current value of the hand
        for card in hand:
            handValue += card.value
            if card.value == 11:
                acesAs11 += 1

        # begins to count aces as 1 instead of 11 as necessary
        if handValue > 21 and acesAs11 > 0:
            for card in hand:
                if card.value == 11 and handValue > 21:
                    card.value = 1
                    handValue -= 10

        # implement strategy
        if self.andCondition == 1:  # we and the determinants
            if self.dealerCondition(dealerHand) and self.playerCondition(handValue, acesAs11):
                pass
        else:  # we or the determinants
            if self.dealerCondition(dealerHand) and self.playerCondition(handValue, acesAs11):
                pass

    def playerCondition(self, handValue, acesAs11):
        if self.hitOnSoft == 1:
            if (handValue < self.hitLessThan) or (handValue == self.hitLessThan and acesAs11 > 0):
                return True
            else:
                return False
        else:
            if handValue < self.hitLessThan:
                return True
            else:
                return False

    def dealerCondition(self, dealerHand):
        if self.dealerAbove == 1:
            if dealerHand[0].value >= self.dealerShowing:
                return True
            else:
                return False
        else:
            if dealerHand[0].value <= self.dealerShowing:
                return True
            else:
                return False


class Ai(object):
    def __init__(self):
        self.WinRatio = 0

    def getChoice(self, myHand, dealerHand):
        pass


