# Square Object
# Project: Minesweeper
# Author: Kristi Daigh
# Created: 09/07/18 09:00AM

class Square:
    maybe = 5

    def __init__(self):
        self.x = 0
        self.y = 0
        self.is_mine = False
        self.is_flagged = False
        self.is_revealed = False
        self.num_adj_mines = 0

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
