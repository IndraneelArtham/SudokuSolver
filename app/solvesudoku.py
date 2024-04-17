"""
Module containing class to solve a sudoku
"""
import create_sudoku as cs
import digit_extract as de

class Sudoku:

    def __init__(self, path):
        de.dig_extract(path)
        self.sudoku = cs.create_sudoku()

    DIGITS = set([str(i) for i in range(1, 10)])
    EMPTY = ''

    def get_rows(self, sudoku):
        return sudoku
    
    def get_cols(self, sudoku):
        cols = [[sudoku[i][j] for i in range(len(sudoku[0]))] for j in range(len(sudoku))]
        return cols
    
    def get_grids(self, sudoku):
        grids = []

        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                grid = []
                for i in range(x, x+3):
                    for j in range(y, y+3):
                        grid.append(sudoku[i][j])
                grids.append(grid)

        return grids

    def is_valid_state(self, sudoku):
        for row in self.get_rows(sudoku):
            if set(row) != self.DIGITS:
                return False
            
        for col in self.get_cols(sudoku):
            if set(col) != self.DIGITS:
                return False
            
        for grid in self.get_grids(sudoku):
            if set(grid) != self.DIGITS:
                return False
        
        return True
    
    def get_candidates(self, sudoku, row, col):
        candidates = self.DIGITS.copy()

        candidates -= set(self.get_rows(sudoku)[row])

        candidates -= set(self.get_cols(sudoku)[col])

        candidates -= set(self.get_grids(sudoku)[((row//3)*3 + col//3)])

        return list(candidates)
    
    def solve_sudoku(self):
        if self.is_valid_state(self.sudoku):
            return True
        for row in range(9):
            for col in range(9):
                if self.sudoku[row][col] == self.EMPTY:
                    for candidate in self.get_candidates(self.sudoku, row, col):
                        self.sudoku[row][col] = candidate
                        solved = self.solve_sudoku()
                        if solved:
                            return True
                        else:
                            self.sudoku[row][col] = self.EMPTY
                    return False
        return True