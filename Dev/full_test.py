import create_sudoku as cs
import digit_extract as de
from solvesudoku import Sudoku


de.dig_extract("SudokuImages/Sudoku5.jpg")
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


solver = Sudoku()
solver.solve_sudoku(sudoku)
print(sudoku)