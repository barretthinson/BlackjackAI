__author__ = 'Barrett Hinson'
import deck
import dealer
import player


def getPlayers(number):
    newPlayers = []
    for i in range(number):
        newPlayers.append(player.Player("Player " + str(i)))
    return newPlayers

shoe = deck.Deck(6)
shoe.shuffle()
players = getPlayers(5)
theDealer = dealer.Dealer(1)

theDealer.begin(shoe, players)
theDealer.deal(shoe, players)
