import tkinter as tk
from tkinter import messagebox

class SudokuSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.root.geometry("600x700")
        self.root.config(bg="#f0f4f8")
        
        self.entry_vars = [[None for _ in range(9)] for _ in range(9)]
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        
        self.create_widgets()
        
    def create_widgets(self):
        frame_grid = tk.Frame(self.root, bg="#f0f4f8")
        frame_grid.grid(row=0, column=0, padx=20, pady=20)
        
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(frame_grid, width=5, font=('Arial', 18), borderwidth=2, relief="solid", justify='center', 
                                 fg="#333", bg="#e8f0f2", highlightbackground="#0066cc", highlightthickness=2)
                entry.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
                self.entry_vars[i][j] = entry
                self.root.grid_rowconfigure(i, weight=1)
                self.root.grid_columnconfigure(j, weight=1)
        
        for i in range(1, 9):
            if i % 3 == 0:
                for j in range(9):
                    self.entry_vars[i][j].config(bd=3, relief="solid", highlightbackground="black")
        
        panel_buttons = tk.Frame(self.root, bg="#f0f4f8")
        panel_buttons.grid(row=0, column=1, padx=20, pady=20)

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i, num in enumerate(numbers):
            button = tk.Button(panel_buttons, text=str(num), font=('Arial', 18), width=4, height=2, 
                               bg="#e8f0f2", fg="#333", command=lambda num=num: self.on_number_button_click(num))
            button.grid(row=i//3, column=i%3, padx=5, pady=5)
        
        self.solve_button = tk.Button(panel_buttons, text="Solve Sudoku", font=('Arial', 14), bg="#4CAF50", fg="white", 
                                      activebackground="#45a049", activeforeground="white", relief="solid", command=self.solve)
        self.solve_button.grid(row=3, column=0, columnspan=3, pady=10, ipadx=10, ipady=10)

        self.reset_button = tk.Button(panel_buttons, text="Reset", font=('Arial', 14), bg="#f44336", fg="white", 
                                      activebackground="#e53935", activeforeground="white", relief="solid", command=self.reset)
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=10, ipadx=10, ipady=10)

    def on_number_button_click(self, num):
        for i in range(9):
            for j in range(9):
                if self.entry_vars[i][j].get() == '':
                    self.entry_vars[i][j].insert(tk.END, str(num))
                    return
    
    def solve(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                value = self.entry_vars[row][col].get()
                if value != '':
                    self.board[row][col] = int(value)
        
        # Coba menyelesaikan Sudoku
        if self.sudoku_solver(self.board):
            for row in range(9):
                for col in range(9):
                    self.entry_vars[row][col].delete(0, tk.END)
                    self.entry_vars[row][col].insert(tk.END, str(self.board[row][col]))
        else:
            messagebox.showinfo("Hasil", "Tidak ada solusi yang ditemukan.")
    
    def sudoku_solver(self, board):
        empty_cell = self.find_empty(board)
        
        if not empty_cell:
            return True
        
        row, col = empty_cell
        
        for num in range(1, 10):
            if self.is_valid(board, row, col, num):
                board[row][col] = num
                
                if self.sudoku_solver(board):
                    return True
                
                board[row][col] = 0  # Backtrack
                
        return False
    
    def find_empty(self, board):
        min_remaining_values = float('inf')
        best_cell = None
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    remaining_values = sum(1 for num in range(1, 10) if self.is_valid(board, row, col, num))
                    if remaining_values < min_remaining_values:
                        min_remaining_values = remaining_values
                        best_cell = (row, col)
                        
        return best_cell
    
    def is_valid(self, board, row, col, num):
        
        for i in range(9):
            if board[row][i] == num:
                return False
        
        for i in range(9):
            if board[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def reset(self):
        for row in range(9):
            for col in range(9):
                self.entry_vars[row][col].delete(0, tk.END)


root = tk.Tk()
app = SudokuSolverApp(root)
root.mainloop()
