# TestWildUnoCard.py
# kurtis bertauche
# cs 333 final project
# 4 26 2023

import unittest
from WildUnoCard import WildUnoCard

class TestWildUnoCard(unittest.TestCase):

    def setUp(self):
        self.WildUnoCard = WildUnoCard("Wild Draw Four")

    def test_constructor_wildDrawFour(self):
        self.assertTrue(self.WildUnoCard.name == "Wild Draw Four",
                        "Wild Card was not constructed correctly")
        
    def test_getCardString_wildDrawFour(self):
        self.assertEqual(self.WildUnoCard.getCardString(),
                         "Wild Draw Four",
                         "Wild Card did not return correct string")