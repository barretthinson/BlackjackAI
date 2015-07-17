__author__ = 'Barrett Hinson'


class Dealer(object):
    def __init__(self, strategy):
        self.hand = []
        if strategy == 1:
            self.strategy = "stand on all 17s"
        else:
            self.strategy = "hit on soft 17s"

    def deal(self, deck, players):
        for player in players:
            pass
