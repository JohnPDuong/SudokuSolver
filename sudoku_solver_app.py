import pygame

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

#Button
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

solve_button = button (GRAY, 675, 910, 150, 80, "Solve")

#Will be called numerous of times to update the window
def draw_window():
    WINDOW.fill(WHITE)
    pygame.draw.line(WINDOW, BLACK, (0, 900), (1000, 900), 1)
    draw_text(PROMPT)
    solve_button.draw (WINDOW, 2)
    draw_grid()

def draw_grid():
    for x in range(9):
        for y in range(9):
            pygame.draw.rect (WINDOW, BLACK, pygame.Rect(x*100, y*100, 100, 100), 2)
    
def draw_text(message_text):
    WINDOW.blit (PROMPT, TEXT_LOCATION)
    
def main():
    clock = pygame.time.Clock()
    run = True;
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if solve_button.isOver(pos):
                    print ("Omg you clicked me!")
                    
            if event.type == pygame.MOUSEMOTION:
                if solve_button.isOver(pos):
                    solve_button.color = GRAY
                else:
                    solve_button.color = WHITE
        
        draw_window()
        
        pygame.display.update()
        
    pygame.quit ()
    
if __name__ == "__main__":
    main()