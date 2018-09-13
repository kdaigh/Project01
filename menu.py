## @package menu
#  Source file for the menu object
#
#  Project: Minesweeper
#  Author: Ayah Alkhatib
#  Created: 09/08/18
#  Completed:

class Menu:

    def __init__(self):
        self.choice = 2
        self.mines_num = 0
        self.board_size = 0
        #self.game_over = game_over
        self.is_loser = False


#    def game_menu(self):
#       print("Welcome to Minesweeper!")
#       print("Please, chose from the menu:")
        print("""1. Play the Game
2. Quit""")
#        self.choice = int(input())
#        if self.choice == 1:
#            print("Please Enter the board size, it should be at least 2, and maximum 15")
#           self.board_size = int(input())
#           print("Awesome! Let the fun begin!")
#           max_mines = self.board_size ** 2 - 1
#           print("Enter the number of mines, it should be between 1 and " + str(max_mines))
#           self.mines_num = int(input())

#       else:
#           return


    def play_again(self):
        if self.is_winner:
            print("YOU WON!!")
            self.game_menu()
            self.is_winner = False
        elif self.is_loser:
            print("GAME OVER!")
            self.game_menu()
            self.is_loser = False

    def play_game(self):
        while not self.is_winner or not self.is_loser:
            # some interactive between the game and the user
            print("still playing")
        self.play_again()
