let selectedCell = null;

function createGrid() {
  const grid = document.getElementById('sudokuGrid');
  for (let i = 0; i < 9; i++) {
    const row = grid.insertRow(i);
    for (let j = 0; j < 9; j++) {
      const cell = row.insertCell(j);
      const input = document.createElement('input');
      input.setAttribute('maxlength', '1');
      input.addEventListener('click', () => selectCell(input));
      cell.appendChild(input);
    }
  }
}


function selectCell(cell) {
  if (selectedCell) {
    selectedCell.style.backgroundColor = ''; 
  }
  selectedCell = cell;
  selectedCell.style.backgroundColor = '#e0e0e0'; 
}


function insertNumber(num) {
  if (selectedCell) {
    selectedCell.value = num;
  }
}


function resetGrid() {
  const inputs = document.querySelectorAll('input');
  inputs.forEach(input => input.value = '');
}


function solveSudoku() {
  const grid = getGridValues();
  if (solve(grid)) {
    fillGrid(grid);
  } else {
    alert("No solution found.");
  }
}


function getGridValues() {
  const grid = [];
  const inputs = document.querySelectorAll('input');
  let index = 0;

  for (let i = 0; i < 9; i++) {
    const row = [];
    for (let j = 0; j < 9; j++) {
      const value = parseInt(inputs[index].value) || 0;
      row.push(value);
      index++;
    }
    grid.push(row);
  }

  return grid;
}


function fillGrid(grid) {
  const inputs = document.querySelectorAll('input');
  let index = 0;

  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      inputs[index].value = grid[i][j] === 0 ? '' : grid[i][j];
      index++;
    }
  }
}


function solve(board) {
  for (let row = 0; row < 9; row++) {
    for (let col = 0; col < 9; col++) {
      if (board[row][col] === 0) {
        for (let num = 1; num <= 9; num++) {
          if (isValid(board, row, col, num)) {
            board[row][col] = num;
            if (solve(board)) {
              return true;
            }
            board[row][col] = 0; 
          }
        }
        return false;
      }
    }
  }
  return true;
}


function isValid(board, row, col, num) {
  for (let i = 0; i < 9; i++) {
    if (board[row][i] === num || board[i][col] === num) {
      return false;
    }
  }

  const startRow = Math.floor(row / 3) * 3;
  const startCol = Math.floor(col / 3) * 3;

  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      if (board[startRow + i][startCol + j] === num) {
        return false;
      }
    }
  }

  return true;
}


createGrid();
