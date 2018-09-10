## @package square
#  Source file for the square object
#
#  Project: Minesweeper
#  Author: Kristi Daigh
#  Created: 09/07/18
#  Completed:


class Square:
    maybe = 5

    ## Constructor
    def __init__(self):
        self.x = 0
        self.y = 0
        ## @var is_mine
        #  mine status flag
        self.is_mine = False
        ## @var is_flagged
        #  flag status flag
        self.is_flagged = False
        ## @var is_revealed
        #  reveal status flag
        self.is_revealed = True
        ## @var num_adj_mines
        #  tracks number of adjacent mines
        self.num_adj_mines = 0

    ## Prints the square based on properties
    def print_square(self):
        if not self.is_revealed:
            if self.is_flagged:
                print("F", end=' ')
            else:
                print("O", end=' ')
        else:
            if self.is_mine:
                print("*", end=' ')
            elif self.num_adj_mines:
                print(" ", end=' ')
            else:
                print("%d" % self.num_adj_mines)