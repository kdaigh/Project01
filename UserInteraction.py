from boardFunctions import BoardFunctions
from square import Square


class UserInteraction:
    ##variable to check when the game ends

    def __init__(self, size, mines):
        self.size = size
        self.mines = mines
        self.game_over = False
        self.myBoard = BoardFunctions()
        self.myBoard.mines_num = mines
        self.grid = self.myBoard.make_grid(self.size)
        self.myBoard.generate_mines(self.size, self.grid)

    def count_nearby_mines(self, x, y):
        adj_mine_counter = 0
        if self.grid[x + 1][y].is_mine:
            adj_mine_counter += 1
        if self.grid[x + 1][y + 1].is_mine:
            adj_mine_counter += 1
        if self.grid[x + 1][y - 1].is_mine:
            adj_mine_counter += 1
        if self.grid[x][y + 1].is_mine:
            adj_mine_counter += 1
        if self.grid[x][y - 1].is_mine:
            adj_mine_counter += 1
        if self.grid[x - 1][y].is_mine:
            adj_mine_counter += 1
        if self.grid[x - 1][y + 1].is_mine:
            adj_mine_counter += 1
        if self.grid[x - 1][y - 1].is_mine:
            adj_mine_counter += 1
        self.grid.num_adj_mines = adj_mine_counter

    def mine_check(self):
        for w in range(0, self.size):
            for z in range(0, self.size):
                self.count_nearby_mines(self.grid.x, self.grid.y)

    def reveal(self, x, y):
        if self.grid[x][y].num_adj_mines != 0:
            self.grid[x][y].is_revealed = True
        else:
            if self.grid[x + 1] in range(0, x) and self.grid[y] in range(0, y):
                if self.grid[x + 1][y].is_flagged == True and self.grid[x + 1][y].num_adj_mines != 0:
                    self.grid[x + 1][y].is_revealed = True
                else:
                    self.reveal(x + 1, y)
            if self.grid[x - 1] in range(0, x) and self.grid[y] in range(0, y):
                if self.grid[x - 1][y].is_flagged == True and self.grid[x - 1][y].num_adj_mines != 0:
                    self.grid[x - 1][y].is_revealed = True
                else:
                    self.reveal(x-1, y)
            if self.grid[x] in range(0, x) and self.grid[y + 1] in range(0, y):
                if self.grid[x][y + 1].is_flagged == True and self.grid[x][y + 1].num_adj_mines != 0:
                    self.grid[x][y + 1].is_revealed = True
                else:
                    self.reveal(x, y + 1)
            if self.grid[x] in range(0, x) and self.grid[y - 1] in range(0, y):
                if self.grid[x][y - 1].is_flagged == True and self.grid[x][y - 1].num_adj_mines != 0:
                    self.grid[x][y - 1].is_revealed = True
                else:
                    self.reveal(x, y - 1)
            if self.grid[x + 1] in range(0, x) and self.grid[y - 1] in range(0, y):
                if self.grid[x + 1][y - 1].is_flagged == True and self.grid[x + 1][y - 1].num_adj_mines != 0:
                    self.grid[x + 1][y - 1].is_revealed = True
                else:
                    self.reveal(x+1, y - 1)
            if self.grid[x + 1] in range(0, x) and self.grid[y + 1] in range(0, y):
                if self.grid[x + 1][y + 1].is_flagged == True and self.grid[x + 1][y + 1].num_adj_mines != 0:
                    self.grid[x + 1][y + 1].is_revealed = True
                else:
                    self.reveal(x+1, y + 1)
            if self.grid[x - 1] in range(0, x) and self.grid[y + 1] in range(0, y):
                if self.grid[x - 1][y + 1].is_flagged == True and self.grid[x - 1][y + 1].num_adj_mines != 0:
                    self.grid[x - 1][y + 1].is_revealed = True
                else:
                    self.reveal(x-1, y + 1)
            if self.grid[x - 1] in range(0, x) and self.grid[y - 1] in range(0, y):
                if self.grid[x - 1][y - 1].is_flagged == True and self.grid[x - 1][y - 1].num_adj_mines != 0:
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
        numFlags = self.mines
        while(self.game_over == False):
            self.myBoard.print_board(self.size, self.grid)
            print("Number of flags: %s" % numFlags)
            user_x = int(input("Enter an Y coordinate: "))
            user_y = int(input("Enter a X coordinate: "))
            user_choice = input("Enter an action flag [f], reveal [r], unflag [n]: ")
            if user_x > self.size or user_y > self.size:
                print("Invalid try again")
            elif self.grid[user_x][user_y].is_flagged == False and user_choice == "n":
                print("Invalid try again")
            elif self.grid[user_x][user_y].is_flagged == False and user_choice == "f":
                self.grid[user_x][user_y].is_flagged = True
                numFlags -= 1
                self.check_win()
            elif self.grid[user_x][user_y].is_flagged == True and user_choice == "f":
                print("Space is already flagged. Try again.")
            elif self.grid[user_x][user_y].is_revealed == True and user_choice == "f":
                print("You can't flag a revealed space. Try again.")
            elif self.grid[user_x][user_y].is_revealed == True and user_choice == "n":
                print("You can't unflag a revealed space. Try again.")
            elif self.grid[user_x][user_y].is_flagged == True and user_choice == "n":
                self.grid[user_x][user_y].is_flagged = False
                numFlags += 1
            #Testing to see if is_revealed is being switched to true
            elif self.grid[user_x][user_y].is_revealed == True and self.grid[user_x][user_y].is_mine == False and user_choice == "r":
                print("Space is already revealed. Try again.")
            elif self.grid[user_x][user_y].is_flagged == True and user_choice == "r":
                print("You can't reveal a flagged space. Unflag before guessing this space or guess a different space.")
            elif self.grid[user_x][user_y].is_mine == True and user_choice == "r":
                print("Game Over")
                self.game_over = True
            else:
                self.reveal(user_x, user_y)
