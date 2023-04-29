# Hand.py
# kurtis bertauche
# 4 26 2023
# cs 333 final project

class Hand:

    def __init__(self, name):
        self.cards = []
        self.name = name
        self.skipNextTurn = False

    def takeCardFromHandByPosition(self, position):
        if(position < len(self.cards)):
            card = self.cards[position]
            self.cards.remove(self.cards[position])
            return(card)
        return False
    
    def peekCardFromHandByPosition(self, position):
        if(int(position) < len(self.cards)):
            card = self.cards[int(position)]
            return(card)
        return False      
    
    def giveCardToHand(self, card):
        self.cards.append(card)

    def validatePosition(self, position):
        if (int(position) > -1) and (int(position) < len(self.cards)):
            return True
        return False

    def getHandString(self):
        if(len(self.cards) > 0):
            string = ""
            for i, card in enumerate(self.cards):
                string += str(i + 1) + ". " + card.getCardString() + "\n"
            return string[:-1]
        return "No cards in hand."
