#returns the row, col for the next empty space in grid
#returns None, None if there are no empty spaces
def find_next_space (puzzle):
    for row in range(9): #0 to 8
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, col
    
    return None, None

#primary function
def solve(puzzle):
    row, col = find_next_space (puzzle)