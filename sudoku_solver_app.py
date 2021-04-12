import pygame
from button import button
from tile import tile
from solver import find_next_space, is_valid
    
pygame.init()

#Window settings
WINDOW_SIZE = WIDTH, HEIGHT = 901, 1000 #define window size
WINDOW = pygame.display.set_mode (WINDOW_SIZE) #creates window with size
pygame.display.set_caption("Sudoku Puzzle Solver") #renames the window

TEXT_LOCATION = (10, 940)

#RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128,128,128)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#FPS is not accounted, do not need high FPS to use sudoku puzzle solver
#Font of numbers displayed
FONT = pygame.font.SysFont("arial", 16)

#Text Displays
PROMPT = pygame.font.Font.render (FONT, "Enter the numbers in for the Sudoku Puzzle. When done, click solve.", True, BLACK)
IN_PROGRESS = pygame.font.Font.render (FONT, "Solving...", True, BLACK)
WARNING = pygame.font.Font.render (FONT, "Solving. Please wait...", True, BLACK)

#Two conditions, either the puzzle can be solve or not
FINISHED = pygame.font.Font.render (FONT, "Puzzle solved!", True, BLACK)
INVALID = pygame.font.Font.render (FONT, "Puzzle cannot be solved.", True, BLACK)

solve_button = button (WHITE, 675, 910, 150, 80, "Solve")
clear_button = button (WHITE, 500, 910, 150, 80, "Clear")

#Will be called numerous of times to update the window
def draw_window():
    WINDOW.fill(WHITE)
    pygame.draw.line(WINDOW, BLACK, (0, 900), (1000, 900), 1)

#draws rectangles
def draw_grid (grid, outline):
    for x in grid:
        for y in x:
            y.draw(WINDOW, outline)

#creates the grid allowing the user to input values
def create_grid ():
    grid = [[tile (WHITE, x*100, y*100, 100, 100, '1') for x in range (9)] for y in range (9)]
    
    return grid

#creates the sudoku puzzle 2D list
def create_puzzle():
    puzzle = [[0 for x in range (9)] for y in range (9)]
    
    return puzzle

#draws clear and solve buttons
def draw_buttons (clear, solve):
    clear.draw (WINDOW, 2)
    solve.draw (WINDOW, 2)
    
#reusable draw text by passing in text displays
def draw_text(text):
    WINDOW.blit (text, TEXT_LOCATION)

def update_grid (puzzle, grid):
    for x in range(9):
        for y in range(9):
            grid[x][y].setVal (puzzle[x][y])
          
def draw_change (grid, text):
    draw_window()
    draw_grid(grid, 1)
    draw_buttons (solve_button, clear_button)
    draw_text(text)

#Reimplemented with solve logic however added necessary GUI elements in it
def solve(puzzle, grid, text):
    
    #Must add event handler, without it, program crashes due to "inactivity"
    #where window locks up
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            text = WARNING
            
        if event.type == pygame.QUIT:
            return False
                    
    update_grid (puzzle, grid)
    row, col = find_next_space (puzzle, grid, text)

    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col, grid, text):
            #Must update the grid
            grid[row][col].setVal (guess)
            grid[row][col].color = GREEN
            puzzle[row][col] = guess
            update_grid (puzzle, grid)
            draw_change (grid, text)
            pygame.display.update()
            
            
            if solve(puzzle, grid, text):
                return True

            grid[row][col].setVal (None)
            grid[row][col].color = RED
            puzzle[row][col] = None
            update_grid (puzzle, grid)
            draw_change (grid, text)
            pygame.display.update()
        
    return False

#main function
def main():    
    run = True
    solving = False
    text = PROMPT
    sudoku_grid = create_grid()
    sudoku_puzzle = create_puzzle()
    solved = False
    
    while run:
        #Event handler
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if solve_button.isOver(pos):
                    solving = True
                    text = IN_PROGRESS
                    for x in range(9):
                        for y in range(9):
                            sudoku_puzzle[x][y] = sudoku_grid[x][y].getVal()
                    solved = solve (sudoku_puzzle, sudoku_grid, text)
                    
                    if solved:
                        text = FINISHED
                    else:
                        text = INVALID
                                       
                if clear_button.isOver(pos):
                    for x in sudoku_grid:
                        for y in x:
                            y.color = WHITE
                            y.text = ""
                            text = PROMPT
                            solving = False
                
                if solving == False:
                    for x in sudoku_grid:
                        for y in x:
                            if y.isOver(pos):
                                y.color = YELLOW
                            else:
                                y.color = WHITE
                                
            if event.type == pygame.MOUSEBUTTONUP:
                solve_button.color = WHITE
                        
            if event.type == pygame.MOUSEMOTION:
                if solving != True:
                    if solve_button.isOver(pos):
                        solve_button.color = GRAY
                    else:
                        solve_button.color = WHITE
                        
                    if clear_button.isOver(pos):
                        clear_button.color = GRAY
                    else:
                        clear_button.color = WHITE
            
            if event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    for x in sudoku_grid:
                        for y in x:
                            if y.color == YELLOW:
                                y.setVal (event.key - 48)
                                y.color = WHITE
                            else:
                                y.color = WHITE
                                    
            draw_change(sudoku_grid, text)
            pygame.display.update()
        
    pygame.quit ()
    
if __name__ == "__main__":
    main()