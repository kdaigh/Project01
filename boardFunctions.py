#boardFunctions class
#project: mineSweeper
#author: Clare Meyer

from square import Square
import square

class BoardFunctions():

    #precondition: no grid has been generated
    #postcondition: grid generated
    #returns: none
    def makeGrid(self,rows,cols):
            rows=int(rows)
            cols=int(cols)
            grid = [[0 for x in range(cols)] for y in range(rows)]
            for i in range(0,rows):
                for j in range(0,cols):
                        grid[i][j] = Square()

            ##self.justPrint(rows, cols, grid)

            ##grid[0][0].is_flagged = True;

            ##self.justPrint(rows,cols,grid)

            return(grid)
            
    #precondition: the grid has been generated but not printed
    #postcondition: grid printed ina grid-like manner
    #returns: none
    def justPrint(self, rows, cols, grid):
        for i in range(0, rows):
            for j in range(0, cols):
                #print grid[i][j].maybe,
                grid[i][j].print_square()
            print('\n')

    #precondition:grid does not have formatting
    #postcondition: grid is printed to look nice for the user
    #returns: none
    def printBoard(self,rows,cols):
            rows=int(rows)
            cols=int(cols)
            grid = [[0 for x in range(cols+2)] for y in range(rows+2)]
            for i in range(0,rows+2):
                for j in range(0,cols+2):
                    if(i==0 and j==0 or i==0 and j==1 or i==1 and j==0
                    or i==1 and j==1):
                        grid[i][j]=" "
                    elif(j == 0):
                        grid[i][j]= i-1
                    elif(i == 0):
                        grid[i][j]=j-1
                    elif(j == 1):
                        grid[i][j]="|"
                    elif(i==1):
                        grid[i][j]="~"
                    else:
                        grid[i][j] = 0


            for i in range(0, rows+2):
                for j in range(0, cols+2):
                    grid[i][j].print_square()
                print('\n')


    def generate_mines(self, size, mines):
            # , and maybe board para. depnds on how we want to access square
            minesNum = 0
            while minesNum != mines:
                for i in range(size):
                    for j in range(size):
                        isMine = random.randint(0, 1)
                        if isMine == 1:
                            # update square flags
                            minesNum += 1
                        else:
                            break
                    isMine = random.randint(0, 1)
                    if isMine == 1:
                        # udate square flags
                        minesNum += 1
                    else:
                        break

    def game_menu(self):
        print("Welcome to Minesweeper!")
        print("Please, chose from the menu:")
        print("""1. Play the Game
    2. Quit""")
        choice = int(input())
        if choice == 1:
            print("Please Enter the board size, it should be at least 2, and maximum 15")
            self.boardSize = int(input())
            print("Awsome! Let the fun begin!")
            min_mines = 1
            max_mines = self.boardSize ** 2 - 1
            print("Enter the number of mines, it should be between 1 and " + str(max_mines))
            self.mines_num = int(input())
            return self.boardSize, self.mines_num
        else:
            return

        #def num_adj_mines(self, rows, cols):
         #   adj_mines = 0
            #for (adj_rows, adj_cols) in self.get_adj_squares(rows, cols):
               # if self.adjacent(adj_rows, adj_cols) and self[adj_rows][adj_cols].is_mine:
                    #adj_mines += 1
            #return adj_mines

        #def get_adj_squares(self, rows, cols):
            #near = [(0, -1), (0, 1), (-1, 1), (-1, -1), (0,1), (0, -1), (1, 1), (1, -1)]
            #for (adj_rows, adj_cols) in near:
                #return (rows + adj_rows, cols + adj_cols)

        #def adjacent(self, rows, cols):
            #return 0 <= rows < len(self) and 0 <= cols < len(self)

    def count_nearby_mines(self, x, y):
        adj_mine_counter = 0
        if Square(x + 1, y).is_mine == True:
            adj_mine_counter += 1
        if Square(x + 1, y + 1).is_mine == True:
            adj_mine_counter += 1
        if Square(x + 1, y - 1).is_mine == True:
            adj_mine_counter += 1
        if Square(x, y + 1).is_mine == True:
            adj_mine_counter += 1
        if Square(x, y - 1).is_mine == True:
            adj_mine_counter += 1
        if Square(x - 1, y).is_mine == True:
            adj_mine_counter += 1
        if Square(x - 1, y + 1).is_mine == True:
            adj_mine_counter += 1
        if Square(x - 1, y - 1).is_mine == True:
            adj_mine_counter += 1
        Square(x, y).num_adj_mines = adj_mine_counter


    def mine_check(self):
        for w in range(0, boardSize):
            for z in range(0, boardSize):
                count_nearby_mines(Square.x, Square.y)
