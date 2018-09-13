## @package main
#  Main file for project
#
#  Project: Minesweeper
#  Author: All
#  Created: 09/06/18
#  Completed:

from menu import Menu
from board import Board
from executive import Executive

playing = Executive()
playing.setup()
playing.play()
