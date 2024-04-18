document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById("container");

    // Sample puzzle data (modify this with your Sudoku puzzle data)
    let puzzle = JSON.parse(solution);
    const original = JSON.parse(solution);
    // Function to create the Sudoku puzzle grid
    function createSudokuGrid(puzzle) {
        container.innerHTML = '';
        puzzle.forEach((row, rowIndex) => {
            const rowElement = document.createElement('div');
            rowElement.classList.add('row');
            row.forEach((cell, columnIndex) => {
                const cellElement = document.createElement('input');
                cellElement.classList.add('cell');
                cellElement.classList.add((Math.floor(rowIndex / 3) + Math.floor(columnIndex / 3)) % 2 === 0 ? 'darkBackground' : 'lightBackground');
                cellElement.type = 'text';
                cellElement.maxLength = 1;
                cellElement.value = cell !== 0 ? cell : '';
                cellElement.addEventListener('input', () => {
                    // Ensure that the input is a single digit
                    const value = cellElement.value.replace(/\D/g, '');
                    cellElement.value = value;
                });
                rowElement.appendChild(cellElement);
            });
            container.appendChild(rowElement);
        });
    }

    // Function to solve the Sudoku puzzle
    function solveSudoku(board) {
        // Placeholder function for solving Sudoku puzzle
        const solvedPuzzle = JSON.parse(JSON.stringify(board));
        solveHelper(solvedPuzzle);
        return solvedPuzzle;
    }

    // Helper function for solving Sudoku recursively
    function solveHelper(board) {
        const emptyCell = findEmptyCell(board);
        if (!emptyCell) {
            return true; // Puzzle solved
        }

        const [row, col] = emptyCell;
        for (let num = 1; num <= 9; num++) {
            if (isValidMove(board, row, col, num)) {
                board[row][col] = num;
                if (solveHelper(board)) {
                    return true;
                }
                board[row][col] = 0; // Backtrack
            }
        }
        return false; // No valid number found for this cell
    }

    // Function to find an empty cell in the Sudoku puzzle
    function findEmptyCell(board) {
        for (let row = 0; row < 9; row++) {
            for (let col = 0; col < 9; col++) {
                if (board[row][col] === 0) {
                    return [row, col];
                }
            }
        }
        return null; // No empty cell found
    }

    // Function to check if a move is valid
    function isValidMove(board, row, col, num) {
        // Check row
        for (let i = 0; i < 9; i++) {
            if (board[row][i] === num) {
                return false;
            }
        }
        // Check column
        for (let i = 0; i < 9; i++) {
            if (board[i][col] === num) {
                return false;
            }
        }
        // Check 3x3 grid
        const startRow = Math.floor(row / 3) * 3;
        const startCol = Math.floor(col / 3) * 3;
        for (let i = startRow; i < startRow + 3; i++) {
            for (let j = startCol; j < startCol + 3; j++) {
                if (board[i][j] === num) {
                    return false;
                }
            }
        }
        return true; // Move is valid
    }

    // Function to solve the puzzle
    function solvePuzzle() {
        const board = getCurrentBoard();
        const solvedBoard = solveSudoku(board);
        setCurrentBoard(solvedBoard);
    }

    // Function to reset the puzzle
    function resetPuzzle() {
        createSudokuGrid(original);
    }

    // Function to get the current state of the puzzle board
    function getCurrentBoard() {
        const currentBoard = [];
        const rows = container.getElementsByClassName('row');
        for (let rowElement of rows) {
            const cells = rowElement.getElementsByClassName('cell');
            const row = [];
            for (let cellElement of cells) {
                const value = cellElement.value.trim();
                row.push(value !== '' ? parseInt(value) : 0);
            }
            currentBoard.push(row);
        }
        return currentBoard;
    }

    // Function to set the puzzle board to a new state
    function setCurrentBoard(board) {
        puzzle = JSON.parse(JSON.stringify(board));
        createSudokuGrid(puzzle);
    }

    // Initialize puzzle
    createSudokuGrid(puzzle);

    // Attach event listeners to buttons
    document.getElementById("solveButton").addEventListener("click", solvePuzzle);
    document.getElementById("resetButton").addEventListener("click", resetPuzzle);
});