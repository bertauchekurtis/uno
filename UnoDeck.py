# UnoDeck.py
# kurtis bertauche
# cs 333 final project
# 4 26 2023

from UnoCard import UnoCard
from WildUnoCard import WildUnoCard
from random import shuffle

class UnoDeck:

    def __init__(self):
        self.cards = []

    def fillDeck(self):
        # first, add the cards that there are duplicates for
        colors = ["Red", "Blue", "Green", "Yellow"]
        numbers = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        for i in range(0, 2):
            for color in colors:
                for number in numbers:
                    self.cards.append(UnoCard(color, number))
        # then add the cards that there are one of 
        numbers = ["Zero", "Draw Two", "Reverse", "Skip"]
        for color in colors:
            for number in numbers:
                self.cards.append(UnoCard(color, number))
        # then add the wild cards
        for i in range(0, 4):
            self.cards.append(WildUnoCard("Wild Draw Four"))
            self.cards.append(WildUnoCard("Wild"))

    def shuffle(self):
        shuffle(self.cards)

    def addCardToTop(self, card):
        self.cards.insert(0, card)

    def addCardToBottom(self, card):
        self.cards.append(card)

    def drawTopCard(self):
        if not self.isEmpty():
            card = self.cards[0]
            self.cards.remove(self.cards[0])
            return(card)
        return False
        
    def isEmpty(self):
        if(len(self.cards) == 0):
            return True
        else:
            return False