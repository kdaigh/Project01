from square import Square
import square

class BoardFunctions():
    def makeGrid(self,rows,cols):
            rows=int(rows)
            cols=int(cols)
            grid = [[0 for x in range(cols)] for y in range(rows)]
            for i in range(0,rows):
                for j in range(0,cols):
                        grid[i][j] = Square()

            for i in range(0, rows):
                for j in range(0, cols):
                    #print grid[i][j].maybe,
                    grid[i][j].print_square()
                print('\n')


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
                    print(a.maybe0)
                print
