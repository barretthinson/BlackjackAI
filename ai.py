__author__ = 'Barrett Hinson'
import random
import queue


class Strategy(object):
    def __init__(self, incStrat1, incStrat2):
        self.timesUsed = 0
        self.wins = 0

        if incStrat1 is not None and incStrat2 is not None:
            self.hitLessThan = (incStrat1.hitLessThan + incStrat2.hitLessThan) // 2
            self.dealerShowing = (incStrat1.dealerShowing + incStrat2.dealerShowing) // 2
        else:
            self.hitLessThan = random.randint(2, 20)
            self.dealerShowing = random.randint(1, 11)

        self.hitOnSoft = random.randint(0, 1)  # binary choice to hit or stay on a soft hand
        self.andCondition = random.randint(0, 1)  # binary choice to and/or the two determinants
        # binary choice on whether we care if the dealer's shown is above or below our threshold
        self.dealerAbove = random.randint(0, 1)

    def doHit(self, hand, dealerHand):
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
                return True
        elif self.andCondition == 0:  # we or the determinants
            if self.dealerCondition(dealerHand) or self.playerCondition(handValue, acesAs11):
                return True
        return False

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

    def updateLossRating(self, win):
        self.timesUsed += 1
        if win:
            self.wins += 1
        return (1-(self.wins / self.timesUsed))/(self.timesUsed**.05)  # + 1/(self.timesUsed**2)

    def getLossRating(self):
        if self.timesUsed == 0:
            return 0
        return (1-(self.wins / self.timesUsed))/(self.timesUsed**.05)  # + 1/(self.timesUsed**2)

    def getStratText(self):
        hitOnSoftT = "hits if on soft " if self.hitOnSoft == 1 else "hits if less than "
        andCondT = "and" if self.andCondition == 1 else "or"
        dealerAboveT = ">= " if self.dealerAbove == 1 else "<= "
        text = "Wins: "+("{0:.2f}".format(self.wins/self.timesUsed * 100))+"% out of "+str(self.timesUsed)+" games Strategy: player "+hitOnSoftT+str(self.hitLessThan)+"s "
        text += andCondT+" if the dealer is showing "+dealerAboveT+str(self.dealerShowing)
        return text


class Ai(object):
    def __init__(self):
        self.stratList = queue.PriorityQueue(maxsize=0)
        self.currentStrat = Strategy(None, None)
        self.stratNumber = 0
        self.stratList.put((1, self.stratNumber, self.currentStrat))
        self.stratNumber += 1

    def getFirstChoice(self, myHand, dealerHand):
        self.currentStrat = self.chooseStrat()
        return self.currentStrat.doHit(myHand, dealerHand)

    def getChoice(self, myHand, dealerHand):
        return self.currentStrat.doHit(myHand, dealerHand)

    def chooseStrat(self):
        methodOfChoice = random.randint(1, 100)

        if 1 <= methodOfChoice <= 60:  # 60% of the time get next strategy
            return self.stratList.get(False)[2]
        elif 61 <= methodOfChoice <= 80:  # 20% of the time create new strategy from scratch
            return Strategy(None, None)
        else:  # remaining 20% of the time combine the top 2 strategies into a hybrid strategy
            strat1 = self.stratList.get(False)[2]
            self.stratList.put((strat1.getLossRating(), self.stratNumber, strat1))
            self.stratNumber += 1

            strat2 = self.stratList.get(False)[2]
            self.stratList.put((strat2.getLossRating(), self.stratNumber, strat2))
            self.stratNumber += 1

            return Strategy(strat1, strat2)

    def getResult(self, win):
        ratio = self.currentStrat.updateLossRating(win)
        self.stratList.put((ratio, self.stratNumber, self.currentStrat))
        self.stratNumber += 1

    def recap(self, topNum):
        text = "top "+str(topNum)+" strategies that this my ai found\n"
        index = 1
        while index <= topNum and not self.stratList.empty():
            strat = self.stratList.get(False)[2]
            if strat.timesUsed > 10:  # ignores trivially low match counts
                text += "\t #"+str(index)+" --- "+strat.getStratText()+"\n"
                index += 1
        return text
