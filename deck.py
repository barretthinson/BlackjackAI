__author__ = 'Barrett Hinson'
import random


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        if 1 < value < 11:
            self.name = str(value) + " of " + str(suit)
        elif value == 11:
            self.name = "Jack of " + str(suit)
        elif value == 12:
            self.name = "Queen of " + str(suit)
        elif value == 13:
            self.name = "King of " + str(suit)
        else:
            self.name = "Ace of " + str(suit)


class Deck(object):
    def __init__(self, numDecks):
        self.deck = []
        suits = ['spades', 'hearts', 'clubs', 'diamonds']
        for deckNum in range(0, numDecks):
            singleDeck = []
            for suit in suits:
                for value in range(1, 14):
                    singleDeck.append(Card(value, suit))
            self.deck.extend(singleDeck)

    def shuffle(self):
        index = 0
        for card in self.deck:
            rand = random.randrange(index, len(self.deck))
            cardA = self.deck[rand]
            self.deck[rand] = card
            self.deck[index] = cardA
            index += 1

    def draw(self):
        return self.deck.pop()

    def shuffleIn(self, discardPile):
        self.deck.extend(discardPile)
        self.shuffle()
