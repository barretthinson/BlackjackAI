__author__ = 'Barrett Hinson'
import deck
import dealer
import player


def getPlayers(number):
    newPlayers = []
    for i in range(number):
        newPlayers.append(player.Player("Player " + str(i)))
    return newPlayers


def getResults(thisDealer, thePlayers):
    for thisPlayer in thePlayers:
        if thisPlayer.finalValue >= thisDealer.finalValue:
            thisPlayer.giveResult(True)
        else:
            thisPlayer.giveResult(False)


shoe = deck.Deck(6)
shoe.shuffle()
players = getPlayers(1)
theDealer = dealer.Dealer(2)

theDealer.begin(shoe, players)
theDealer.deal(shoe, players)

getResults(theDealer, players)

