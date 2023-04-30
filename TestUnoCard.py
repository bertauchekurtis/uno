# TestWildCard.py
# kurtis bertauche
# cs 333 final project
# 4 26 2023

import unittest
from UnoCard import UnoCard

class TestUnoCard(unittest.TestCase):

    def setUp(self):
        self.UnoCard = UnoCard("Red", "Seven")

    def test_constructor_redSeven(self):
        self.assertTrue(self.UnoCard.color == "Red" and self.UnoCard.name == "Seven",
                        "Card was not constructed correctly")
        
    def test_getCardName_redSeven(self):
        self.assertEqual(self.UnoCard.getCardName(),
                         "Seven",
                         "Card did not return correct name")
        
    def test_getCardColor_redSeven(self):
        self.assertEqual(self.UnoCard.getCardColor(),
                         "Red",
                         "Card did not return correct color")
        
    def test_getCardString_redSeven(self):
        self.assertEqual(self.UnoCard.getCardString(),
                         "Red Seven",
                         "Card did not return correct string")

if __name__ == '__main__':
    unittest.main()

