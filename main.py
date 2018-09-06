import math
from Tkinter import *
from boardFunctions import BoardFunctions

window=Tk()

class MainWindow():

    theBoard = BoardFunctions()

    rows = raw_input("How many rows?")
    cols = raw_input("How many cols?")

    theBoard.makeGrid(rows, cols)

    window.title("Welcome to Mine Sweeper")

    window.geometry('1000x2000')

    lbl = Label(window, text="Hello")

    lbl.grid(row=0, column=0)

    window.mainloop()
