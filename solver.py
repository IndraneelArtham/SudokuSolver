import numpy as np


def p(grid):
    """Print the Sudoku"""
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
        cols = [[sudoku[i][j]
                 for i in range(len(sudoku[0]))] for j in range(len(sudoku))]
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
        self.sudoku = np.array(sudoku)
        self.rows = [self.sudoku[i, :] for i in range(9)]
        self.cols = [self.sudoku[:, j] for j in range(9)]
        self.grids = self.sudoku.reshape(
            3, 3, 3, 3).swapaxes(1, 2).reshape(9, 9)

    def mode_sudoku(self):
        """Element which occurs the most in the Sudoku"""
        freq = np.zeros(9)
        for row in self.rows:
            for cell in row:
                if cell:
                    # print(cell)
                    if freq[int(cell)-1] == 8:
                        freq[int(cell)-1] = -1
                    else:
                        freq[int(cell)-1] += 1

        # print("freq", freq)
        return np.argsort(freq)[::-1]

    def forced_fill(self, num):
        """Fill Cells which can be done without assumptions"""
        changed = False
        for grid_num, grid in enumerate(self.grids):
            if num not in grid:

                indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8]

                for cell in range(9):
                    if grid[cell] != "":
                        indexes.remove(cell)

                # print("Grid_num", grid_num)
                rows = self.rows[int(3*(grid_num//3))                                 : int(3*(grid_num//3) + 3)]
                cols = self.cols[int(3*(grid_num % 3)): int(3*(grid_num % 3) + 3)]

                # print("rows", rows)
                # print("cols", cols)

                for r_num, r in enumerate(rows):
                    if num in r:
                        for k in range(3*r_num, 3*r_num+3):
                            if k in indexes:
                                indexes.remove(k)

                # print("After rows", indexes)
                for c_num, c in enumerate(cols):
                    if num in c:
                        for k in range(c_num, 9, 3):
                            if k in indexes:
                                indexes.remove(k)

                # print("After Cols", indexes)

                if len(indexes) == 1:
                    row = (grid_num // 3) * 3 + (indexes[0] // 3)
                    col = (grid_num % 3) * 3 + (indexes[0] % 3)
                    self.sudoku[row][col] = num
                    changed = True
                    print(f"Filled {num}")

        return changed

    def full_forced(self):
        changed = True
        while changed:
            for i in self.mode_sudoku():
                changed = self.forced_fill(str(i+1))


# s = [["", "3", "9", "5", "", "", "", "", ""],
#      ["", "", "", "8", "", "", "", "7", ""],
#      ["", "", "", "", "1", "", "9", "", "4"],
#      ["1", "", "", "4", "", "", "", "", "3"],
#      ["", "", "", "", "", "", "", "", ""],
#      ["", "", "7", "", "", "", "8", "6", ""],
#      ["", "", "6", "7", "", "8", "2", "", ""],
#      ["", "1", "", "", "9", "", "", "", "5"],
#      ["", "", "", "", "", "1", "", "", "8"]]

# s = [['4', '5', '3', '8', '2', '1', '7', '9', '6'],
#      ['7', '1', '8', '4', '6', '9', '3', '5', '2'],
#      ['2', '6', '9', '5', '7', '3', '8', '1', '4'],
#      ['9', '7', '2', '6', '4', '8', '1', '3', '5'],
#      ['1', '3', '4', '9', '5', '2', '6', '7', '8'],
#      ['6', '8', '5', '1', '3', '7', '4', '2', '9'],
#      ['8', '9', '7', '2', '1', '6', '5', '4', '3'],
#      ['3', '4', '6', '7', '9', '5', '2', '8', '1'],
#      ['5', '2', '1', '3', '8', '4', '9', '6', '7']]

# solver = Sudoku(s)
# solver.full_forced()
# print(solver.sudoku)
