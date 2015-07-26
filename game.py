__author__ = 'Barrett Hinson'
import deck
import dealer
import player


def getPlayers(number):
    newPlayers = []
    for ind in range(number):
        newPlayers.append(player.Player("Player " + str(ind)))
    return newPlayers


def getResults(thisDealer, thePlayers):
    for thisPlayer in thePlayers:
        if thisPlayer.finalValue >= thisDealer.finalValue:
            thisPlayer.giveResult(True)
        else:
            thisPlayer.giveResult(False)


def reset(thisDealer, thePlayers, theDeck):
    discardPile = []
    discardPile.extend(thisDealer.hand)
    thisDealer.hand = []
    for thisPlayer in thePlayers:
        discardPile.extend(thisPlayer.hand)
        thisPlayer.hand = []
    theDeck.shuffleIn(discardPile)

shoe = deck.Deck(6)
shoe.shuffle()
players = getPlayers(5)
theDealer = dealer.Dealer(2)

for i in range(1):
    theDealer.begin(shoe, players)
    theDealer.deal(shoe, players)
    getResults(theDealer, players)
    reset(theDealer, players, shoe)
