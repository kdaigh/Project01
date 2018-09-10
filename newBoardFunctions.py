from random import randint
from square import Square


class BoardFunctions():
    
    def __init__(self):
        self.mines = 0

    # precondition: no grid has been generated
    # postcondition: grid generated
    # returns: none
    def makeGrid(self, rows, cols):
        rows=int(rows)
        cols=int(cols)
        grid = [[0 for x in range(rows)] for y in range(cols)]

        self.generate_mines(grid, rows, cols)
        self.grid_with_mines(grid, rows, cols)

        self.justPrint(grid, rows, cols)

    def generate_mines(self, grid, rows, cols):
            # in_mines = self.mines
            for i in range(self.mines):
                is_bomb = False
                while not is_bomb:
                    a = randint(0, rows - 1)
                    b = randint(0, cols - 1)
                    if grid[a][b] != 1:
                        grid[a][b] = 1
                        is_bomb = True
            return grid

    def grid_with_mines(self, grid, rows, cols):
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 1:
                    grid[i][j] = Square()
                    grid[i][j].is_mine = True;
                    # to test the change in the status
                    # grid[0][1].is_flagged = True;
                    # grid[0][0].is_revealed = True;
                    # grid[0][0].is_mine = True;
                else:
                    grid[i][j] = Square()



    # precondition: the grid has been generated but not printed
    # postcondition: grid printed ina grid-like manner
    # returns: none
    def justPrint(self, grid, rows, cols):
        for i in range(0, rows):
            for j in range(0, cols):
                # print(grid[i][j].maybe,)
                grid[i][j].print_square()
            print('\n')


    # precondition:grid does not have formatting
    # postcondition: grid is printed to look nice for the user
    # returns: none
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
                    a = grid[i][j]
                    # print(a.maybe0)
                print
