# TestUnoDeck.py
# kurtis bertauche
# cs 333 final project
# 4 26 2023

import unittest
from UnoDeck import UnoDeck
from UnoCard import UnoCard

class TestUnoCard(unittest.TestCase):

    def setUp(self):
        self.UnoDeck = UnoDeck()

    def test_constructor(self):
        self.assertTrue(len(self.UnoDeck.cards) == 0,
                        "Deck was not initialized empty")
        
    def test_fill_deck(self):
        self.UnoDeck.fillDeck()
        self.assertTrue(len(self.UnoDeck.cards) == 96,
                        "Incorrect number of cards in deck")
        
    def test_addCardToTop(self):
        self.UnoDeck.fillDeck()
        card = UnoCard("Red", "Seven")
        self.UnoDeck.addCardToTop(card)
        self.assertEqual(self.UnoDeck.cards[0],
                         card,
                         "Card not correct added to top of deck")
        
    def test_addCardToBottom(self):
        self.UnoDeck.fillDeck()
        card = UnoCard("Red", "Seven")
        self.UnoDeck.addCardToBottom(card)
        self.assertEqual(self.UnoDeck.cards[96],
                         card,
                         "Card not correctly added to bottom of deck")

    def test_isEmpty_true(self):
        self.assertTrue(self.UnoDeck.isEmpty(),
                        "Deck is empty, but not indicated so")
        
    def test_isEmpty_false(self):
        self.UnoDeck.fillDeck()
        self.assertFalse(self.UnoDeck.isEmpty(),
                         "Deck is not empty, but indicated so")
        
    def test_drawTopCard(self):
        card = UnoCard("Red", "Seven")
        self.UnoDeck.fillDeck()
        self.UnoDeck.addCardToTop(card)
        self.assertEqual(self.UnoDeck.drawTopCard(),
                         card,
                         "Draw top card did not work as it should")