# TestHand.py
# kurtis bertauche
# cs 333 final project
# 4 26 2023

import unittest
from Hand import Hand
from UnoCard import UnoCard
from WildUnoCard import WildUnoCard

class TestHand(unittest.TestCase):

    def setUp(self):
        self.hand = Hand("Player")

    def test_construcotr(self):
        self.assertTrue(len(self.hand.cards) == 0 and 
                        self.hand.name == "Player" and 
                        self.hand.skipNextTurn is False,
                        "Did not construct hand properly")
        
    def test_giveCardToPlayer(self):
        card = UnoCard("Red", "Seven")
        self.hand.giveCardToHand(card)
        self.assertEqual(self.hand.cards[0],
                         card,
                         "Card not correctly given to player")
        
    def test_takeCardFromHandByPosition(self):
        card1 = UnoCard("Red", "Seven")
        card2 = UnoCard("Red", "Eight")
        card3 = WildUnoCard("Wild")
        self.hand.giveCardToHand(card1)
        self.hand.giveCardToHand(card2)
        self.hand.giveCardToHand(card3)
        card = self.hand.takeCardFromHandByPosition(1)
        self.assertTrue(card == card2 and
                        self.hand.cards[0] == card1 and
                        self.hand.cards[1] == card3,
                        "Card not correctly removed from hand")
        
    def test_takeCardFromHandByPositionInvalidPosition(self):
        self.assertFalse(self.hand.takeCardFromHandByPosition(12),
                         "Invalid position not flagged in takeCardByPosition function.")
        
    def test_peekCardFromHandByPosition(self):
        card1 = UnoCard("Red", "Seven")
        card2 = UnoCard("Red", "Eight")
        card3 = WildUnoCard("Wild")
        self.hand.giveCardToHand(card1)
        self.hand.giveCardToHand(card2)
        self.hand.giveCardToHand(card3)
        card = self.hand.peekCardFromHandByPosition(1)
        self.assertTrue(card == card2 and
                        self.hand.cards[0] == card1 and
                        self.hand.cards[1] == card2 and
                        self.hand.cards[2] == card3,
                        "Peek did not find the correct card.")
        
    def test_peekCardFromHandByPositionInvalidPosition(self):
        self.assertFalse(self.hand.validatePosition(12),
                         "Invalid position not flagged as false.")
        
    def test_getHandString(self):
        card1 = UnoCard("Red", "Seven")
        card2 = UnoCard("Red", "Eight")
        card3 = WildUnoCard("Wild")
        self.hand.giveCardToHand(card1)
        self.hand.giveCardToHand(card2)
        self.hand.giveCardToHand(card3)
        string = self.hand.getHandString()
        self.assertEqual(string,
                         "1. Red Seven\n2. Red Eight\n3. Wild")
        
    def test_getHandStringNoCards(self):
        self.assertEqual(self.hand.getHandString(),
                         "No cards in hand.",
                         "Incorrect string returned when player has no cards")
        
    def test_validatePositionTrue(self):
        card1 = UnoCard("Red", "Seven")
        card2 = UnoCard("Red", "Eight")
        card3 = WildUnoCard("Wild")
        self.hand.giveCardToHand(card1)
        self.hand.giveCardToHand(card2)
        self.hand.giveCardToHand(card3)
        self.assertTrue(self.hand.validatePosition(1),
                        "Position is valid but function returned false")
        
    def test_validatePositionFalse(self):
        card1 = UnoCard("Red", "Seven")
        card2 = UnoCard("Red", "Eight")
        card3 = WildUnoCard("Wild")
        self.hand.giveCardToHand(card1)
        self.hand.giveCardToHand(card2)
        self.hand.giveCardToHand(card3)
        self.assertFalse(self.hand.validatePosition(5),
                        "Position is not valid but function returned true")


