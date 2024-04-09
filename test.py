import numpy as np

# Create a 9x9 Sudoku grid
sudoku_grid = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

# Create views for rows, columns, and subgrids
rows = [sudoku_grid[i, :] for i in range(9)]
columns = [sudoku_grid[:, j] for j in range(9)]
subgrids = [sudoku_grid[i:i+3, j:j+3] for i in range(0, 9, 3) for j in range(0, 9, 3)]

# Print the original grid and the views
print("Original Sudoku Grid:")
print(sudoku_grid)

print("\nRows:")
for row in rows:
    print(row)

print("\nColumns:")
for col in columns:
    print(col)

print("\nSubgrids:")
for subgrid in subgrids:
    print(subgrid)

sudoku_grid[4][4] = 9

print("After Change:")
print(sudoku_grid)

print("\nRows:")
for row in rows:
    print(row)

print("\nColumns:")
for col in columns:
    print(col)

print("\nSubgrids:")
for subgrid in subgrids:
    print(subgrid)