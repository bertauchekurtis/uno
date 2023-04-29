# UnoGame.py
# kurtis bertauche
# cs 333 final project
# 4 26 2023

from UnoDeck import UnoDeck
from WildUnoCard import WildUnoCard
from Hand import Hand

class UnoGame():

    def __init__(self):
        self.drawDeck = UnoDeck()
        self.discardDeck = UnoDeck()
        self.currentColor = None

    def setupNewGame(self):
        self.drawDeck.clearDeck()
        self.drawDeck.fillDeck()
        self.drawDeck.shuffle()
        self.discardDeck.clearDeck()
        card = self.drawDeck.drawTopCard()
        while(isinstance(card, WildUnoCard)):
            self.drawDeck.addCardToBottom(card)
            card = self.drawDeck.drawTopCard()
        self.discardDeck.addCardToTop(card)
        self.currentColor = self.discardDeck.peekTopCard().getCardColor()

    def doInitialDeal(self, hands):
        # we give all of the players seven cards
        for i in range(0, 7):
            for hand in hands:
                hand.giveCardToHand(self.drawDeck.drawTopCard())

    def getTopCardString(self):
        string = "Card to play on top of:\n-"
        string += self.discardDeck.peekTopCard().getCardString()
        return string 
    
    def thereIsWinner(self, hands):
        for hand in hands:
            if len(hand.cards) == 0:
                return True
        return False
    
    def validateCardToPlay(self, card):
        # or if it's a wild card
        if(isinstance(card, WildUnoCard)):
            return True
        if(self.currentColor == card.color):
            return True
        if(self.discardDeck.peekTopCard().name == card.name):
            return True
        return False
    
    def handHasAValidMove(self, hand):
        for card in hand.cards:
            if self.validateCardToPlay(card):
                return True
        return False

    def giveCardToHand(self, hand):
        if self.drawDeck.isEmpty():
            topCard = self.discardDeck.drawTopCard()
            while(not self.discardDeck.isEmpty()):
                self.drawDeck.addCardToTop(self.discardDeck.drawTopCard())
                self.drawDeck.shuffle()
            self.discardDeck.addCardToTop(topCard)
        hand.giveCardToHand(self.drawDeck.drawTopCard())

    def doMove(self, card, nextHand):
        if(card.name == "Draw Two"):
            self.giveCardToHand(nextHand)
            self.giveCardToHand(nextHand)
        elif(card.name == "Skip"):
            nextHand.skipNextTurn = True
        elif(card.name == "Reverse"):
            nextHand.skipNextTurn = True
        self.currentColor = card.color
        self.discardDeck.addCardToTop(card)

    def doWildMove(self, card, color, nextHand):
        if(card.name == "Wild Draw Four"):
            for i in range(0,4):
                self.giveCardToHand(nextHand)
        self.discardDeck.addCardToTop(card)
        self.currentColor = color
