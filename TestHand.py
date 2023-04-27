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
        self.assertTrue(len(self.hand.cards) == 0 and self.hand.name == "Player",
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
        
    def test_getHandString(self):
        card1 = UnoCard("Red", "Seven")
        card2 = UnoCard("Red", "Eight")
        card3 = WildUnoCard("Wild")
        self.hand.giveCardToHand(card1)
        self.hand.giveCardToHand(card2)
        self.hand.giveCardToHand(card3)
        string = self.hand.getHandString()
        self.assertEqual(string,
                         "0. Red Seven\n1. Red Eight\n2. Wild")

