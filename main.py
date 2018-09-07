import math
import random
from boardFunctions import BoardFunctions

print ("Welcome to Minesweeper!")
print ("Please, chose from the menu:")

theBoard=BoardFunctions()

rows = input("How many rows?")
cols = input("How many cols?")

theBoard.makeGrid(rows, cols)
