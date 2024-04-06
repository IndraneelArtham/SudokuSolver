import numpy as np

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

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.rows = sudoku
        self.cols = self.get_cols(sudoku)
        self.grids = self.get_grids(sudoku)
        self.freq = np.zeros(9)

    def mode_sudoku(self):
        
        for row in self.sudoku:
            for cell in row:
                if self.freq[cell] == 8:
                    self.freq[cell] = -1
                else:
                    self.freq[cell] += 1
        
        return str(np.argmax(self.freq))

    def forced_fill(self, num):
        for i, grid in enumerate(self.grids):
            if num not in grid:
                r = self.sudoku[int(3*(i/3)): int(3*(i/3) + 1)]
                c = self.sudoku[int(3*(i%3)): int(3*(i%3) + 1)]

                for i in r:
                    if num in self.rows[r]:
                        r.remove(i)
                
                for j in c:
                    if num in self.cols[c]:
                        c.remove(j)

                if len(r) == 1 and len(c) == 1:
                    self.sudoku[r[0], c[0]] == num

    def can_fill_cell(self, num, row, col):
        # if num not in 
        ...



s = [["", "3", "9", "5", "", "", "", "", ""],
     ["", "", "0", "8", "", "", "", "7", ""],
     ["", "", "", "", "1", "", "9", "", "4"],
     ["1", "", "", "4", "", "", "", "", "3"],
     ["", "", "", "", "", "", "", "", ""],
     ["", "", "7", "", "", "", "8", "6", ""],
     ["", "", "6", "7", "", "8", "2", "", ""],
     ["", "1", "", "", "9", "", "", "", "5"],
     ["", "", "", "", "", "1", "", "", "8"]]

solver = Sudoku(s)
solver.forced_fill("9")
for i in s:
    print(i)