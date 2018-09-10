from boardFunctions import BoardFunctions
from square import Square


class UserInteraction:

    game_over = False

    def reveal(self, x, y):
        if Square(x,y).num_adj_mines != 0:
            Square(x,y).is_revealed = True
        else:
            if Square(x + 1, y).is_flagged != False and Square.num_adj_mines != 0:
                Square(x + 1,y).is_revealed = True
            else:
                self.reveal(x+1, y)
            if Square(x - 1, y).is_flagged != False and Square.num_adj_mines != 0:
                Square(x - 1,y).is_revealed = True
            else:
                self.reveal(x-1, y)
            if Square(x, y + 1).is_flagged != False and Square.num_adj_mines != 0:
                Square(x,y + 1).is_revealed = True
            else:
                self.reveal(x, y + 1)
            if Square(x, y - 1).is_flagged != False and Square.num_adj_mines != 0:
                Square(x,y - 1).is_revealed = True
            else:
                self.reveal(x, y - 1)
            if Square(x + 1, y - 1).is_flagged != False and Square.num_adj_mines != 0:
                Square(x + 1,y - 1).is_revealed = True
            else:
                self.reveal(x+1, y - 1)
            if Square(x + 1, y + 1).is_flagged != False and Square.num_adj_mines != 0:
                Square(x + 1,y + 1).is_revealed = True
            else:
                self.reveal(x+1, y + 1)
            if Square(x - 1, y + 1).is_flagged != False and Square.num_adj_mines != 0:
                Square(x - 1,y + 1).is_revealed = True
            else:
                self.reveal(x-1, y + 1)
            if Square(x - 1, y - 1).is_flagged != False and Square.num_adj_mines != 0:
                Square(x - 1,y - 1).is_revealed = True
            else:
                self.reveal(x - 1, y - 1)

    def check_win(self):
        flag_on_mine = 0
        for i in range(0, BoardFunctions.boardSize):
            for x in range(0, BoardFunctions.boardSize):
                if Square(i,x).is_mine == True and Square(i,x).is_flagged == True:
                    flag_on_mine += 1
        if flag_on_mine == BoardFunctions.mines_num:
            print("You Win!")
            gameOver = True
        else:
            return 0
    while(game_over != True):
        numFlags = BoardFunctions.mines_num
        print("Number of flags: %s" % numFlags)
        userX = input("Enter an X coordinate: ")
        userY = input("Enter a Y coordinate: ")
        userChoice = input("Enter an action flag [f], reveal [r], unflag [n]: ")
        if userX > BoardFunctions.boardSize or userY > BoardFunctions.boardSize:
            print("Invalid Try again")
        #elif square at user input x or y is flagged == false and userChoice == N:
            print("Invalid try again")
        #elif #square at user input x and y isflagged == false and userChoice == f:
            #set square(x,y) isFlagged = true
            # numFlags -= check_win
        #elif# square(x,y) isFlagged == true and userChoice == n:
            #set square(x,y) isFlagged == false and numFlags +=
        #elif #square(x,y) isMine == true and userChoice == r:
            print("Game Over")
            game_over == True
        #else:
            reveal(userX, userY)