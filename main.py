# main.py
# kurtis bertauche
# cs 333 final project
# 4 26 2023

from UnoGame import UnoGame

def main():
    
    print("====> Welcome to Uno! <====\n")
    print("You will play a game of Uno against the computer. Good luck!\n")

    game = UnoGame()
    game.setUpGame()

    print("The cards have been dealt and the game now begins.")
    print("Here is your current hand:")
    print(game.playerHand.getHandString())
    print("")
    print(game.getTopCardString())
    print("")

    while(not game.thereIsWinner()):
        print("Player: What move will you choose?")
        print(game.getTopCardString())
        print("Current hand:")
        print(game.playerHand.getHandString())
        choiceValid = False
        choice = ""
        while(not choiceValid):
            choice = input("Enter the index of the card you wish to play: ")
            choiceValid = game.confirmValidPlayerMove(int(choice))

if __name__ == "__main__":
    main()