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
        if thisPlayer.finalValue > 21:
            thisPlayer.finalValue = 0  # busted
        if thisDealer.finalValue > 21:
            thisDealer.finalValue = 0  # busted

        thisPlayer.giveResult(thisPlayer.finalValue >= thisDealer.finalValue)


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

for i in range(1000000):
    theDealer.begin(shoe, players)
    theDealer.deal(shoe, players)
    getResults(theDealer, players)
    reset(theDealer, players, shoe)

for finishedPlayer in players:
    print(finishedPlayer.getRecap(10))
