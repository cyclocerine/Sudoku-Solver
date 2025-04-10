def is_valid(board, row, col, num):
    
    # Cek baris
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Cek kolom
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Cek subgrid 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def find_empty(board):
    min_remaining_values = float('inf')
    best_cell = None
    
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                remaining_values = sum(1 for num in range(1, 10) if is_valid(board, row, col, num))
                if remaining_values < min_remaining_values:
                    min_remaining_values = remaining_values
                    best_cell = (row, col)
                    
    return best_cell

def sudoku_solver(board):
    empty_cell = find_empty(board)
    
    if not empty_cell:
        return True  
    
    row, col = empty_cell
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            if sudoku_solver(board):
                return True
            
            board[row][col] = 0  
            
    return False  

def input_sudoku():
    print("Masukkan papan Sudoku Anda (gunakan 0 untuk posisi kosong):")
    board = []
    for i in range(9):
        row = list(map(int, input(f"Baris {i+1} (pisahkan angka dengan spasi): ").split()))
        board.append(row)
    return board

board = input_sudoku()

if sudoku_solver(board):
    print("\nSudoku yang diselesaikan:")
    for row in board:
        print(row)
else:
    print("Tidak ada solusi yang ditemukan.")
