import math
from Tkinter import *
window=Tk()

class MainWindow():

    rows = raw_input("How many rows?")
    cols = raw_input("How many cols?")

    def makeGrid(rows, cols):
        rows=int(rows)
        cols=int(cols)
        for i in range(0,rows):
            for j in range(0,cols):
                btn1 = Button(window, text=i)
                btn1.grid(column = i, row = j, sticky=NSEW)

    window.title("Welcome to Mine Sweeper")

    window.geometry('1000x2000')

    lbl = Label(window, text="Hello")

    lbl.grid(row=0, column=0)

    makeGrid(rows,cols)

    window.mainloop()
