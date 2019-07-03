## @file board.py
#  Source file for the board object
#
#  Project: Minesweeper
#  Author: Clare Meyer
#  Created: 09/06/18

from random import randint
from square import Square


## @class Board
#  @brief Handles board creation and board functionality
class Board:

    ## Constructor
    #  @author: Clare
    def __init__(self):
        ## @var boardSize
        #  stores the size of the board
        self.boardSize = 0
        ## @var mines_num
        #  stores the number of mines
        self.mines_num = 0

    ## Generates a grid object
    #  @author: Clare
    #  @param: size, size of the grid
    #  @returns: grid
    def make_grid(self, size):
            size = int(size)
            grid = [[0 for x in range(size)] for y in range(size)]
            for i in range(0, size):
                for j in range(0, size):
                    grid[i][j] = Square()
            return grid

    ## Randomly places mines on board
    #  @author: Ayah
    #  @pre: a grid has been generated
    #  @param: num_mines, user-selected number of mines
    #  @param: size, size of the grid
    #  @param: grid, grid to be populated
    #  @post: the grid is populated with mines
    def generate_mines(self, mines, size, grid):
        self.mines_num=mines;
        self.boardSize=size;
        for i in range(0, self.mines_num):
            is_bomb = False
            while not is_bomb:
                a = randint(0, self.boardSize - 1)
                b = randint(0, self.boardSize - 1)
                if not grid[a][b].is_mine:
                    grid[a][b].is_mine = True
                    is_bomb = True

    ## Prints the board with minimal formatting
    #  @author:Clare
    #  @pre: the grid has been generated
    #  @param: size, size of the grid
    #  @param: grid, grid to be printed
    #  @post: grid printed in a grid-like manner
    def just_print(self, size, grid):
        for i in range(0, size):
            for j in range(0, size):
                grid[i][j].print_square()
            print('\n', end=' ')

    ## Prints a formatted game board
    #  @author: Clare
    #  @pre: grid does not have formatting
    #  @param: size, size of the grid
    #  @param: main_grid, grid to be printed
    #  @post: grid is printed to look nice for the user
    def print_board(self, size, main_grid):
            size = int(size)
            grid = [[0 for x in range(size + 2)] for y in range(size + 2)]
            for i in range(0, size+2):
                for j in range(0, size+2):
                    if(i == 0 and j == 0 or i == 0 and j == 1 or i == 1 and j == 0
                    or i == 1 and j == 1):
                        grid[i][j] = " "
                    elif j == 0:
                        grid[i][j] = i-2
                    elif i == 0:
                        grid[i][j] = j-2
                    elif j == 1:
                        grid[i][j] = "|"
                    elif i == 1:
                        grid[i][j] = "--"
                    else:
                        grid[i][j] = main_grid[i - 2][j - 2]

            for i in range(0, size+2):
                for j in range(0, size+2):
                    if i == 0 or i == 1 or j == 0 or j == 1:
                        if i == 1 and j == 0:
                            print(grid[i][j], end=' ')
                        elif i == 0 and j == 0 or i == 0 and j == 1 or i == 1 and j == 1:
                            print((str(grid[i][j]).ljust(2)), end=' ')
                        elif i == 0 or j == 0:
                            print((str(grid[i][j]).zfill(2)), end=' ')
                        else:
                            print(str(grid[i][j]).ljust(2), end=' ')
                    else:
                        grid[i][j].print_square()
                print('\n', end=' ')

    ## Counts number of adjacent mines for a given cell
    #  @authors: Kyle, Kristi
    #  @param x, x-coordinate of cell
    #  @param y, y-coordinate of cell
    #  @param: size, size of the grid
    #  @param: grid, grid to be checked
    def count_nearby_mines(self, x, y, size, grid):
        if grid[x][y].is_mine:
            return
        if 0 < x:
            # top left
            if 0 < y:
                if grid[x - 1][y - 1].is_mine:
                    grid[x][y].num_adj_mines += 1

            # top middle
            if grid[x - 1][y].is_mine:
                grid[x][y].num_adj_mines += 1

            # top right
            if y < size:
                if grid[x - 1][y + 1].is_mine:
                    grid[x][y].num_adj_mines += 1

        # left
        if 0 < y:
            if grid[x][y - 1].is_mine:
                grid[x][y].num_adj_mines += 1

        # right
        if y < size:
            if grid[x][y + 1].is_mine:
                grid[x][y].num_adj_mines += 1

        if x < size:
            # bottom left
            if 0 < y:
                if grid[x + 1][y - 1].is_mine:
                    grid[x][y].num_adj_mines += 1

            # bottom middle
            if grid[x + 1][y].is_mine:
                grid[x][y].num_adj_mines += 1

            # bottom right
            if y < size:
                if grid[x + 1][y + 1].is_mine:
                    grid[x][y].num_adj_mines += 1

    ## Counts/labels number of adjacent mines for board
    #  @author: Kyle
    #  @param: size, size of the grid
    #  @param: grid, grid to be checked
    #  @post: each square is labeled with num_adj_mines
    def mine_check(self, size, grid):
        for w in range(size):
            for z in range(size):
                self.count_nearby_mines(w, z, size - 1, grid)
