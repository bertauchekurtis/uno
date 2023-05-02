# main.py
# kurtis bertauche
# cs 333 final project
# 4 26 2023

from UnoGame import UnoGame
from Hand import Hand
from WildUnoCard import WildUnoCard
from random import choice as rchoice

def main():
    
    print("====> Welcome to Uno! <====\n")
    print("You will play a game of Uno against your computer. Good luck!\n")


    wantsToPlay = True
    while(wantsToPlay):

        # define some things and setup
        game = UnoGame()
        player = Hand("Player")
        computer = Hand("Computer")
        game.setupNewGame()
        game.doInitialDeal([player, computer])

        # run the game
        while(not game.thereIsWinner([player, computer])):
            
            # get the player's move
            if(not player.skipNextTurn):
                validMove = False
                while(not validMove):
                    # first, we need to check if there 
                    # are any cards that the player CAN play
                    # if not, we need to draw cards for them
                    while(not game.handHasAValidMove(player)):
                        print("You don't have any playable cards!")
                        print("Adding a card to your deck ;)")
                        game.giveCardToHand(player)
                    print("\nPlayer, it is your turn:")
                    print(game.getTopCardString())
                    print("\nCards in your hand:")
                    print(player.getHandString())

                    intChoice = False
                    choice = None
                    while(not intChoice):
                        choice = input("Enter the index of the card you want to play: ")
                        try:
                            choice = int(choice)
                            intChoice = True
                        except TypeError:
                            print("Please enter a whole number.")
                    # check to make sure the index is valid
                    validMove = player.validatePosition(int(choice) - 1)
                    # print message if not valid choice
                    if(not validMove):
                        print("Invalid index, please try again.")
                    # check if the card is a valid to play card
                    if(validMove):
                        validMove = game.validateCardToPlay(
                            player.peekCardFromHandByPosition(int(choice) - 1))
                        if(not validMove):
                            print("Invalid move, please try again.")
                
                # at this point, we have the player's move and it is valid
                card = player.takeCardFromHandByPosition(int(choice - 1))
                if(isinstance(card, WildUnoCard)):
                    colors = ["Red", "Green", "Blue", "Yellow"]
                    inputgood = False
                    color = None
                    while(not inputgood):
                        print("Wild card! Choose your color:")
                        color = input("(Red, Green, Blue, Yellow): ")
                        if color in colors:
                            inputgood = True
                        else:
                            print("Color not recognized, please try again.")
                    game.doWildMove(card, color, computer)
                else:
                    game.doMove(card, computer)
            else:
                print("Your turn has been skipped!\n")
                player.skipNextTurn = False

            # now we do the computer's move
            if(not computer.skipNextTurn and 
               not game.thereIsWinner([player, computer])):
                print("\nThe computer will now play.")
                print("The computer has " + str(len(computer.cards)) + " cards.")
                print(game.getTopCardString())
                while(not game.handHasAValidMove(computer)):
                        print("The compueter doesn't have any \
                              valid moves. Adding a card.")
                        game.giveCardToHand(computer)
                cardToPlay = None
                for card in computer.cards:
                    if game.validateCardToPlay(card):
                        indexOfCard = computer.cards.index(card)
                        cardToPlay = computer.takeCardFromHandByPosition(indexOfCard)
                print("The computer is playing " + cardToPlay.getCardString())
                if(isinstance(cardToPlay, WildUnoCard)):
                    colors = ["Red", "Green", "Blue", "Yellow"]
                    color = rchoice(colors)
                    print("The new color is " + color)
                    game.doWildMove(cardToPlay, color, player)
                else:
                    game.doMove(cardToPlay, player)
            else:
                print("The computer's turn has been skipped!\n")
                computer.skipNextTurn = False
    
        print("The game has ended!")
        inputValid = False
        answer = None
        while(not inputValid):
            ins = ["Y", "N"]
            answer = input("Do you want to play again? [Y/N]: ")
            if answer in ins:
                inputValid = True
            else:
                print("Invalid answer, try again.")
        if(answer == "N"):
            wantsToPlay = False
            print("\nGoodbye!\n")
        else:
            print("\nStarting new game!\n")
        

        

if __name__ == "__main__":
    main()