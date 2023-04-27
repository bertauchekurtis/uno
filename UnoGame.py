# UnoGame.py
# kurtis bertauche
# cs 333 final project
# 4 26 2023

from UnoDeck import UnoDeck
from WildUnoCard import WildUnoCard
from Hand import Hand

class UnoGame():

    def __init__(self):
        self.deck = UnoDeck()
        self.discard = UnoDeck()
        self.playerHand = Hand("Player")
        self.computerHand = Hand("Computer")
        self.gameActive = False

    def setUpGame(self):
        self.deck.fillDeck()
        self.deck.shuffle()
        self.gameActive = True
        for i in range(0, 7):
            card = self.deck.drawTopCard()
            self.playerHand.giveCardToHand(card)
            card = self.deck.drawTopCard()
            self.computerHand.giveCardToHand(card)
        self.discard.addCardToTop(self.deck.drawTopCard())

    # this checks a card against the top card (to be played on top of)
    def validateMove(self, card):
        if(isinstance(card, WildUnoCard)):
           return True
        if(self.deck.cards[0].name == card.name or self.deck.cards[0].color == card.color):
            return True
        return False
    
    # this gets the string to print of the top card
    def getTopCardString(self):
        return "Top Card: " + self.discard.cards[0].getCardString()
    
    # adds a card to discard
    def addCardToDiscard(self, card):
        self.discard.addCardToTop(card)

    # this returns TRUE if the player has a possible move, FALSE otherwise
    def playerHasValidMove(self, card):
        for card in self.playerHand.cards:
            valid = self.validateMove(card)
            if(valid):
                return True
        return False

    # this returns TRUE if the computer has a possible move, FALSE otherwise
    def computerHasValidMove(self, card):
        for card in self.computerHand.cards:
            valid = self.validateMove(card)
            if(valid):
                return True
        return False

    # this confirms that the move that the player has chosen is valid (based on index)
    # if it is, returns TRUE
    # otherwise, returns FALSE
    def confirmValidPlayerMove(self, position):
        # first, make sure index is valid
        if(not self.playerHand.validatePosition(position)):
            return False
        # then make sure card is playable
        tryCard = self.playerHand.peekCardFromHandByPosition(position)
        if(not self.validateMove(tryCard)):
            return False
        return True
    
    # this checks if someone has won the game
    def thereIsWinner(self):
        if len(self.playerHand.cards) == 0 or len(self.computerHand.cards) == 0:
            return True
        return False




