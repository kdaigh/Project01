## @package menu
#  Source file for the menu object
#
#  Project: Minesweeper
#  Author: Ayah Alkhatib
#  Created: 09/08/18
#  Completed:


from executive import Executive


class Menu :


    def __init__(self):

        self.choice = 0
        self.myGame = Executive ()

    
    def game_menu(self):

        play_again = "p"
        while (self.myGame.game_over == False):
            print("Please, chose from the menu:")
            print("""1. Play the Game
2. Quit""")
            self.choice = int(input())
            if self.choice == 1:
                self.myGame.setup()
                self.myGame.play()
            else:
                print("Goodbye! See you later!")
                return
            while play_again != "q":
                play_again = input ("Play again (p), otherwise (q): ")
                if play_again == "p":
                    self.myGame = Executive ()
                    self.myGame.setup()
                    self.myGame.play()
                elif play_again !='q':
                    print ("Please enter a valid choice")
            print ("Goodbye! See you later!")
            return


    def game_rules (self):
        print ("""Welcome to Minesweepers!

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
