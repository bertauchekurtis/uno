# TestUnoGame.py
# kurtis bertauche
# cs 333 final project
# 4 29 2023

import unittest
from UnoGame import UnoGame
from UnoDeck import UnoDeck

class TestHand(unittest.TestCase):

    def setUp(self):
        self.game = UnoGame()

    def testConstructor(self):
        self.assertTrue(isinstance(self.game.drawDeck, UnoDeck) and
                        isinstance(self.game.discardDeck, UnoDeck) and
                        self.game.currentColor is None,
                        "Uno game not correctly constructed.")
        
    ##### IMPORTANT ######
    # The rest of the functions for UnoGame.py are 
    # integration tests since they involve other units of code
    # They can be found in the integration test file
    ######################