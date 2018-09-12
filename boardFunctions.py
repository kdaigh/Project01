
#boardFunctions class
#project: mineSweeper
#author: Clare Meyer

from random import randint
from square import Square


class BoardFunctions():

    def __init__(self):
        self.boardSize = 0
        self.mines_num = 0


    #@precondition: no grid has been generated
    #@postcondition: grid generated
    #@returns: grid
    #@author: Clare
    def make_grid(self,size):
            size=int(size)
            grid = [[0 for x in range(size)] for y in range(size)]
            for i in range(0,size):
                for j in range(0,size):
                    grid[i][j] = Square()
            return(grid)

    def generate_mines(self,size,grid):
        for i in range(0, self.mines_num):
            is_bomb = False
            while is_bomb==False:
                a = randint(0, size - 1)
                b = randint(0, size - 1)
                if grid[a][b].is_mine == False:
                    grid[a][b].is_mine = True
                    is_bomb = True

    #@precondition: the grid has been generated but not printed
    #@postcondition: grid printed ina grid-like manner
    #@returns: none
    #@author:Clare
    def just_print(self, size, grid):
        for i in range(0, size):
            for j in range(0, size):
                # print(grid[i][j].maybe,)
                grid[i][j].print_square()
            print('\n', end=' ')


    #@precondition:grid does not have formatting
    #@postcondition: grid is printed to look nice for the user
    #@returns: none
    #@author: Clare
    def print_board(self,size,main_grid):
            size=int(size)
            grid = [[0 for x in range(size+2)] for y in range(size+2)]
            for i in range(0,size+2):
                for j in range(0,size+2):
                    if(i==0 and j==0 or i==0 and j==1 or i==1 and j==0
                    or i==1 and j==1):
                        grid[i][j]=" "
                    elif(j == 0):
                        grid[i][j]=i-2
                    elif(i == 0):
                        grid[i][j]=j-2
                    elif(j == 1):
                        grid[i][j]="|"
                    elif(i==1):
                        grid[i][j]="--"
                    else:
                        grid[i][j] = main_grid[i-2][j-2]

            for i in range(0, size+2):
                for j in range(0, size+2):
                    if(i==0 or i==1 or j==0 or j==1):
                        if((i==1 and j==0)):
                            print(grid[i][j], end=' ')
                        elif((i==0 and j==0) or (i==0 and j==1)or (i==1 and j==1)):
                            print((str(grid[i][j]).ljust(2)),end=' ')
                        elif(i==0 or j==0):
                            print((str(grid[i][j]).zfill(2)),end=' ')
                        else:
                            print(str(grid[i][j]).ljust(2), end=' ')
                    else:
                        grid[i][j].print_square()
                print('\n', end=' ')
p
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
