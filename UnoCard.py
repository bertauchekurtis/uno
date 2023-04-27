# UnoCard.py
# kurtis bertauche
# 4 23 2023
# cs333 final project

class UnoCard:

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def getCardName(self):
        return self.name
    
    def getCardColor(self):
        return self.color
    
    def getCardString(self):
        return self.color + " " + self.name

