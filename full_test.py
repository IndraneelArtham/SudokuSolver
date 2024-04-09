import numpy as np
import cv2
from imutils.contours import sort_contours
import matplotlib.pyplot as plt


import create_sudoku as cs
import digit_extract as de
from solver import Sudoku


de.dig_extract("SudokuImages/Sudoku2.jpg")
sudoku = cs.create_sudoku()

s = Sudoku(sudoku)
s.full_forced()
print(s.sudoku)