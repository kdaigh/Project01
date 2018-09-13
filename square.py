## @package square
#  Source file for the square object
#
#  Project: Minesweeper
#  Author: Kristi Daigh
#  Created: 09/07/18
#  Completed:


class Square:

    ## Constructor
    def __init__(self):
        ## @var is_mine
        #  mine status flag
        self.is_mine = False
        ## @var is_flagged
        #  flag status flag
        self.is_flagged = False
        ## @var is_revealed
        #  reveal status flag
        self.is_revealed = False
        ## @var num_adj_mines
        #  tracks number of adjacent mines
        self.num_adj_mines = 0

    ## Prints the square based on properties
    def print_square(self):
        if not self.is_revealed:
            if self.is_flagged:
                print(str("F").ljust(2), end=' ')
            else:
                print(str("#").ljust(2), end=' ')
        else:
            if self.is_mine:
                print(str("*").ljust(2), end=' ')
            elif self.num_adj_mines:
                print(str(self.num_adj_mines).ljust(2), end=' ')
            else:
                print(str(" ").ljust(2), end=' ')
