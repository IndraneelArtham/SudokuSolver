"""
Module containing class to solve a sudoku
"""

def p(grid):
    print(grid[0:3])
    print(grid[3:6])
    print(grid[6:9])
    print("\n")


class Sudoku:

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
    
    def solve_sudoku(self, sudoku):
        if self.is_valid_state(sudoku):
            return True
        for row in range(9):
            for col in range(9):
                if sudoku[row][col] == self.EMPTY:
                    for candidate in self.get_candidates(sudoku, row, col):
                        sudoku[row][col] = candidate
                        solved = self.solve_sudoku(sudoku)
                        if solved:
                            return True
                        else:
                            sudoku[row][col] = self.EMPTY
                    return False
        return True

s = [["", "5", "", "", "", "", "", "9", ""],
     ["", "", "8", "4", "", "9", "3", "", ""],
     ["", "6", "", "", "7", "", "", "1", ""],
     ["9", "", "", "6", "4", "8", "", "", "5"],
     ["", "", "", "", "", "", "", "7", ""],
     ["6", "", "", "1", "3", "7", "", "", "9"],
     ["", "9", "", "", "1", "", "", "4", ""],
     ["", "", "6", "7", "", "5", "2", "", ""],
     ["", "2", "", "", "", "", "", "6", ""]]

solver = Sudoku()
solver.solve_sudoku(s)
for i in s:
    print(i)