## @package UserInteraction
#  Source file for the UI class
#
#  Project: Minesweeper
#  Author: Ethan Lefert
#  Created: 09/08/18
#  Completed:

from boardFunctions import BoardFunctions


class UserInteraction:

    ## Constructor; initializes class variables
    #  @author: Ethan
    def __init__(self):
        self.size = 0
        self.mines = 0
        self.num_flags = 0
        self.game_over = False
        self.grid = [0][0]
        self.myBoard = BoardFunctions()

    def reveal(self, x, y):
        if self.grid[x][y].num_adj_mines != 0:
            self.grid[x][y].is_revealed = True
        else:
            if self.grid[x + 1] in range(0, x) and self.grid[y] in range(0,y):
                if self.grid[x + 1][y].is_flagged == False and self.grid[x + 1][y].num_adj_mines != 0:
                    self.grid[x + 1][y].is_revealed = True
                else:
                    self.reveal(x+1, y)
            if self.grid[x - 1] in range(0, x) and self.grid[y] in range(0,y):
                if self.grid[x - 1][y].is_flagged == False and self.grid[x - 1][y].num_adj_mines != 0:
                    self.grid[x - 1][y].is_revealed = True
                else:
                    self.reveal(x-1, y)
            if self.grid[x] in range(0, x) and self.grid[y + 1] in range(0,y):
                if self.grid[x][y + 1].is_flagged == False and self.grid[x][y + 1].num_adj_mines != 0:
                    self.grid[x][y + 1].is_revealed = True
                else:
                    self.reveal(x, y + 1)
            if self.grid[x] in range(0, x) and self.grid[y - 1] in range(0,y):
                if self.grid[x][y - 1].is_flagged == False and self.grid[x][y - 1].num_adj_mines != 0:
                    self.grid[x][y - 1].is_revealed = True
                else:
                    self.reveal(x, y - 1)
            if self.grid[x + 1] in range(0, x) and self.grid[y - 1] in range(0,y):
                if self.grid[x + 1][y - 1].is_flagged == False and self.grid[x + 1][y - 1].num_adj_mines != 0:
                    self.grid[x + 1][y - 1].is_revealed = True
                else:
                    self.reveal(x+1, y - 1)
            if self.grid[x + 1] in range(0, x) and self.grid[y + 1] in range(0,y):
                if self.grid[x + 1][y + 1].is_flagged == False and self.grid[x + 1][y + 1].num_adj_mines != 0:
                    self.grid[x + 1][y + 1].is_revealed = True
                else:
                    self.reveal(x+1, y + 1)
            if self.grid[x - 1] in range(0, x) and self.grid[y + 1] in range(0,y):
                if self.grid[x - 1][y + 1].is_flagged == False and self.grid[x - 1][y + 1].num_adj_mines != 0:
                    self.grid[x - 1][y + 1].is_revealed = True
                else:
                    self.reveal(x-1, y + 1)
            if self.grid[x - 1] in range(0, x) and self.grid[y - 1] in range(0,y):
                if self.grid[x - 1][y - 1].is_flagged == False and self.grid[x - 1][y - 1].num_adj_mines != 0:
                    self.grid[x - 1][y - 1].is_revealed = True
                else:
                    self.reveal(x - 1, y - 1)

    ## Checks if all mines are flagged
    #  @author: Ethan
    def check_win(self):
        flag_on_mine = 0
        for i in range(0, self.size):
            for x in range(0, self.size):
                if self.grid[i][x].is_mine and self.grid[i][x].is_flagged:
                    flag_on_mine += 1
        if flag_on_mine == self.mines:
            print("You Win!")
            self.game_over = True
        else:
            return 0

    ## Generates board with user input for mines and size
    #  @author: Ethan
    def setup(self):

        print("Enter board size, between 2 and 15")
        self.size = int(input())
        max_mines = self.size * self.size - 1
        print("Enter the number of mines, between 1 and " + str(max_mines))
        self.mines = int(input())

        self.num_flags = self.mines

        self.grid = self.myBoard.make_grid(self.size)
        self.myBoard.generate_mines(self.mines, self.size, self.grid)
        self.myBoard.mine_check(self.size, self.grid)


    ## Takes coordinates from user and handles input
    #  @pre: Board has been setup
    #  @author: Ethan
    def play(self):

        while not self.game_over:
            self.myBoard.print_board(self.size, self.grid)
            print("Number of flags: %s" % self.num_flags)
            x = int(input("Enter an Y coordinate: "))
            y = int(input("Enter a X coordinate: "))
            choice = input("Enter an action flag [f], reveal [r], unflag [n]: ")
            if x > self.size or y > self.size:
                print("Invalid try again")
            elif not self.grid[x][y].is_flagged and choice == "n":
                print("Invalid try again")
            elif not self.grid[x][y].is_flagged and self.num_flags == 0 and choice == "f":
                print("Out of flags. Try again.")
            elif not self.grid[x][y].is_flagged and choice == "f":
                self.grid[x][y].is_flagged = True
                self.num_flags -= 1
                self.check_win()
            elif self.grid[x][y].is_flagged and choice == "f":
                print("Space is already flagged. Try again.")
            elif self.grid[x][y].is_revealed and choice == "f":
                print("You can't flag a revealed space. Try again.")
            elif self.grid[x][y].is_revealed and choice == "n":
                print("You can't unflag a revealed space. Try again.")
            elif self.grid[x][y].is_flagged and choice == "n":
                self.grid[x][y].is_flagged = False
                self.num_flags += 1
            #Testing to see if is_revealed is being switched to true
            elif self.grid[x][y].is_revealed and not self.grid[x][y].is_mine and choice == "r":
                print("Space is already revealed. Try again.")
            elif self.grid[x][y].is_flagged and choice == "r":
                print("You can't reveal a flagged space. Unflag before guessing this space or guess a different space.")
            elif self.grid[x][y].is_mine and choice == "r":
                print("Game Over")
                self.game_over = True
            else:
                self.reveal(x, y)
