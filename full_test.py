import numpy as np
import cv2
from imutils.contours import sort_contours
import matplotlib.pyplot as plt


import create_sudoku as cs
import digit_extract as de
from solver import Sudoku


de.dig_extract("SudokuImages/Sudoku4.jpg")
sudoku = cs.create_sudoku()

# sudoku = [
#     ["5", "3", "",   "", "7", "",   "", "", ""],
#     ["6", "",  "",   "1", "9", "5",  "", "", ""],
#     ["",  "9", "8",  "", "", "",   "", "6", ""],

#     ["8", "",  "",   "", "6", "",   "", "", "3"],
#     ["4", "",  "",   "8", "", "3",   "", "", "1"],
#     ["7", "",  "",   "", "2", "",   "", "", "6"],

#     ["",  "6", "",   "", "", "",   "2", "8", ""],
#     ["",  "",  "",   "4", "1", "9",  "", "", "5"],
#     ["",  "",  "",   "", "8", "",   "", "7", "9"]
# ]


s = Sudoku(sudoku)
s.full_forced()
print(s.sudoku)