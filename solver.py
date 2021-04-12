#returns the row, col for the next empty space in grid
#returns None, None if there are no empty spaces
def find_next_space (puzzle, grid, text):
    for row in range(9): #0 to 8
        for col in range(9):
            if puzzle[row][col] == None:
                return row, col
    
    return None, None

#determines validity of guess in sudoku puzzle
#returns True if valid, otherwise False
def is_valid(puzzle, guess, row, col, grid, text):
    row_vals = puzzle[row] #row_vals is vector of given puzzle row
    
    if guess in row_vals: #checks if guess is in row_vals
        return False
    
    col_vals = [puzzle[i][col] for i in range(9)] #col_vals is vector of given puzzle row

    if guess in col_vals: #checks if guess is in col_vals
        return False
        
        
    #starting pos will be on the top left of the specified grid
    row_start = (row // 3) * 3 #determines which row to start in
    col_start = (col // 3) * 3 #determines which column to start in

    #checks for group validation
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
             
    return True



#primary function that solves the problem
def solve(puzzle):
    row, col = find_next_space (puzzle)

    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if solve(puzzle):
                return True

        puzzle[row][col] = None
    return False