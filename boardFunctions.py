from Tkinter import *

class BoardFunctions():
    def makeGrid(self,rows,cols):
            rows=int(rows)
            cols=int(cols)
            for i in range(0,rows):
                for j in range(0,cols):
                    btn1 = Button(text=i)
                    btn1.grid(column = i, row = j, sticky=NSEW)

    def checking(self, num):
        num=2
        if()
