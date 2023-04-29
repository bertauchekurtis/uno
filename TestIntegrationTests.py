# TestIntegrationTests.py
# kurtis bertauche
# cs 333 final project
# 4 29 2023

from UnoGame import UnoGame
from UnoCard import UnoCard
from WildUnoCard import WildUnoCard
from Hand import Hand
import unittest

class TestIntegrationTests(unittest.TestCase):

    def setUp(self):
        self.game = UnoGame()
        self.player = Hand("player")
        self.computer = Hand("computer")

    def test_setupNewGame(self):
        self.game.setupNewGame()
        self.assertTrue(len(self.game.discardDeck.cards) == 1 and
                        self.game.currentColor is not None and
                        len(self.game.drawDeck.cards) == 95,
                        "Game not initialized correctly")
        
    def test_doInitialDealWith2Hands(self):
        self.game.setupNewGame()
        self.game.doInitialDeal([self.player, self.computer])
        self.assertTrue(len(self.player.cards) == 7 and
                        len(self.computer.cards) == 7 and
                        len(self.game.drawDeck.cards) == 81,
                        "Initial deal did not deal the correct number of cards to players")
        
    def test_getTopCardString(self):
        card = UnoCard("Red", "Seven")
        self.game.setupNewGame()
        self.game.discardDeck.addCardToTop(card)
        self.assertEqual(self.game.getTopCardString(),
                         "Card to play on top of:\n-Red Seven",
                         "Top card string not generated correctly")
        
    def test_ThereIsWinnerNoWinner(self):
        self.game.setupNewGame()
        self.game.doInitialDeal([self.player, self.computer])
        self.assertFalse(self.game.thereIsWinner([self.player, self.computer]),
                         "Falsely identified a winner when there was none")
        
    def test_ThereIsWinnerWithWinner(self):
        self.game.setupNewGame()
        self.game.doInitialDeal([self.player, self.computer])
        self.player.cards = []
        self.assertTrue(self.game.thereIsWinner([self.player, self.computer]),
                        "Failed to identify that there was a winner.")
        
    def test_validateCardToPlayWithWild(self):
        wildCard = WildUnoCard("Wild")
        self.assertTrue(self.game.validateCardToPlay(wildCard),
                        "Wild card should always be a valid play.")
        
    def test_validateCardToPlayWithColor(self):
        card = UnoCard("Blue", "Eight")
        self.game.currentColor = "Blue"
        self.assertTrue(self.game.validateCardToPlay(card),
                        "Blue card not validated when color is blue")
        
    def test_validateCardToPlayWithNumber(self):
        card = UnoCard("Blue", "Eight")
        card2 = UnoCard("Red", "Eight")
        self.game.discardDeck.addCardToTop(card)
        self.assertTrue(self.game.validateCardToPlay(card2),
                        "Number card not validated when number is same.")

    def test_handHasAValidMove(self):
        card = UnoCard("Blue", "Eight")
        card2 = UnoCard("Red", "Eight")
        self.game.discardDeck.addCardToBottom(card)
        self.player.giveCardToHand(card2)
        self.assertTrue(self.game.handHasAValidMove(self.player),
                        "Player has valid move but it was not identified")
        
    def test_handHasAValidMoveNoMove(self):
        card = UnoCard("Blue", "Eight")
        card2 = UnoCard("Red", "Nine")
        self.game.discardDeck.addCardToBottom(card)
        self.player.giveCardToHand(card2)
        self.assertFalse(self.game.handHasAValidMove(self.player),
                        "Player has valid move but it was not identified")
        
    def test_giveCardToHand(self):
        self.game.setupNewGame()
        self.game.giveCardToHand(self.player)
        self.assertTrue(len(self.player.cards) == 1,
                        "Did not correctly give a card to the provided hand.")
        
    def test_doMoveDrawTwo(self):
        card = UnoCard("Red", "Draw Two")
        self.game.setupNewGame()
        self.game.doMove(card, self.computer)
        self.assertTrue(len(self.computer.cards) == 2 and
                        self.game.currentColor == "Red" and
                        self.game.discardDeck.cards[0] == card,
                        "Draw Two card did not get played correctly.")
        
    def test_doMoveSkip(self):
        card = UnoCard("Red", "Skip")
        self.game.setupNewGame()
        self.game.doMove(card, self.computer)
        self.assertTrue(self.computer.skipNextTurn == True and
                        self.game.discardDeck.cards[0] == card,
                        "Skip card did not get played correctly")

    def test_doMoveReverse(self):
        card = UnoCard("Red", "Reverse")
        self.game.setupNewGame()
        self.game.doMove(card, self.computer)
        self.assertTrue(self.computer.skipNextTurn == True and
                        self.game.discardDeck.cards[0] == card,
                        "Skip card did not get played correctly")
        
    def test_doMoveNormal(self):
        card = UnoCard("Red", "Seven")
        self.game.setupNewGame()
        self.game.doMove(card, self.computer)
        self.assertTrue(self.game.discardDeck.cards[0] == card,
                        "Card not correctly played")
        
    def test_doWildMoveDrawFour(self):
        card = WildUnoCard("Wild Draw Four")
        self.game.setupNewGame()
        self.game.doWildMove(card, "Blue", self.player)
        self.assertTrue(self.game.currentColor == "Blue" and
                        self.game.discardDeck.cards[0] == card and
                        len(self.player.cards) == 4,
                        "Wild draw four card did not get played correctly")