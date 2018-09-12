from boardFunctions import BoardFunctions
from square import Square


class UserInteraction():
    ##variable to check when the game ends

    def __init__(self):
        self.size=0
        self.mines=0
        self.num_flags=0
        self.game_over = False
        self.grid=[][]
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

    def check_win(self):
        flag_on_mine = 0
        for i in range(0, self.size):
            for x in range(0, self.size):
                if self.grid[i][x].is_mine == True and self.grid[i][x].is_flagged == True:
                    flag_on_mine += 1
        if flag_on_mine == self.mines:
            print("You Win!")
            self.game_over = True
        else:
            return 0

    def play(self):

        print("Enter board size, between 2 and 15")
        self.size = int(input())
        max_mines = self.board_size ** 2 - 1
        print("Enter the number of mines, between 1 and " + str(max_mines))
        self.mines = int(input())

        numFlags = self.mines

        self.grid = self.myBoard.make_grid(self.size)
        self.myBoard.generate_mines(self.size,self.grid)

        while(self.game_over != True):
            ##SEEING IF REVEAL WAS SET TO TRUE
            print(self.grid[0][0].is_revealed)
            ##END OF THIS CHECK
            self.myBoard.print_board(self.size, self.grid)
            print("Number of flags: %s" % numFlags)
            userX = int(input("Enter an Y coordinate: "))
            userY = int(input("Enter a X coordinate: "))
            userChoice = input("Enter an action flag [f], reveal [r], unflag [n]: ")
            if userX > self.size or userY > self.size:
                print("Invalid Try again")
            elif self.grid[userX][userY].is_flagged == False and userChoice == "n":
                print("Invalid try again")
            elif self.grid[userX][userY].is_flagged == False and userChoice == "f":
                self.grid[userX][userY].is_flagged = True
                numFlags -= 1
                self.check_win()
            elif self.grid[userX][userY].is_flagged == True and userChoice == "n":
                self.grid[userX][userY].is_flagged = False
                numFlags += 1
            elif self.grid[userX][userY].is_mine == True and userChoice == "r":
                print("Game Over")
                self.game_over = True
            else:
                self.reveal(userX, userY)
