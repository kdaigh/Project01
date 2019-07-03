## @file menu.py
#  Source file for the menu object
#
#  Project: Minesweeper
#  Author: Ayah Alkhatib
#  Created: 09/08/18

from executive import Executive


## @class Menu
#  @brief Prints menu and rules; Manages Executive instance
class Menu:

    ## Constructor; initializes class variables
    #  @author: Ayah
    def __init__(self):
        ## @var choice
        #  flag for replay choice
        self.choice = 0
        ## @var myGame
        #  instance of the executive class
        self.myGame = Executive()

    ## Handles any type error in users input
    #  @author: Ayah
    #  @returns user input when entered correctly
    def type_error_handler(self):
        while True:
            try:
                check = int (input())
                break
            except:
                print ("Please enter a valid choice: ")
                print ("Play[1], Quit[2]")
        return check

    ## Keep the game running until user chose to quit
    #  @authors: Ayah
    def game_menu(self):

        play_again = 1
        while not self.myGame.game_over:
            print("Please, chose from the menu:")
            print("""1. Play the Game
2. Quit""")
            self.choice = self.type_error_handler()
            if self.choice == 1:
                self.myGame.setup()
                self.myGame.play()
            elif self.choice == 2:
                print("Goodbye! See you later!")
                break
            else:
                print("Please enter a valid choice:")
            while play_again != 2:
                print("Play[1], Quit [2]")
                play_again = self.type_error_handler()
                if play_again == 1:
                    self.myGame = Executive ()
                    self.myGame.setup()
                    self.myGame.play()
                elif play_again != 2:
                    print("Please enter a valid choice")
            print("Goodbye! See you later!")
            return

    
    ## Prints the game instructions
    #  @author: Ayah
    def game_rules(self):
        print("""Welcome to Minesweepers!

Here are the game instructions:

The game will provid players a square board with a number of hidden mines and similar number of flags.

Player has three choices of action:

    - Flag: to flag squares that might have mines.

    - Unflag: to unflag if player changed mind.

    - Reveal: to see what squares have underneath.

When player chose to reveal:

    - If the square has a mine -> Gameover!

    - If not a mine, it will show spaces and numbers to tell player the number of mines around the chosen square.

The goal is to flag all mines until the counter of flags equals to zero without revealing any mine.

Good Luck!

""")
