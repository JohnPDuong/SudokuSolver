import pygame
import button

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

#FPS - Each PC is different, regulates the frequency of program updates
FPS = 60

#Font of numbers displayed
FONT = pygame.font.SysFont("arial", 16)

#Text Displays
PROMPT = pygame.font.Font.render (FONT, "Enter the numbers in for the Sudoku Puzzle. When done, click solve.", True, BLACK)
IN_PROGRESS = pygame.font.Font.render (FONT, "Solving...", True, BLACK)
FINISHED = pygame.font.Font.render (FONT, "Puzzle solved!", True, BLACK)
INVALID = pygame.font.Font.render (FONT, "Puzzle cannot be solved.", True, BLACK)

solve_button = button (GRAY, 675, 910, 150, 80, "Solve")

#Will be called numerous of times to update the window
def draw_window():
    WINDOW.fill(WHITE)
    pygame.draw.line(WINDOW, BLACK, (0, 900), (1000, 900), 1)

#draws rectangles
def draw_grid():
    for x in range(9):
        for y in range(9):
            pygame.draw.rect (WINDOW, BLACK, pygame.Rect(x*100, y*100, 100, 100), 2)

#reusable draw text by passing in text displays
def draw_text(text):
    WINDOW.blit (text, TEXT_LOCATION)
    
def main():
    #updates every 1/60th of a second
    clock = pygame.time.Clock(FPS)
    
    run = True;
    solving = False;
    text = PROMPT
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if solve_button.isOver(pos):
                    solving = True
                    
            if event.type == pygame.MOUSEMOTION:
                if solve_button.isOver(pos):
                    solve_button.color = GRAY
                else:
                    solve_button.color = WHITE
        
        draw_window()
        draw_grid()
        
        if (solving):
            text = IN_PROGRESS
            
        draw_text(text)
        solve_button.draw(WINDOW, 2)
        pygame.display.update()
        
    pygame.quit ()
    
if __name__ == "__main__":
    main()