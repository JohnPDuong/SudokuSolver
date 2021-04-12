import pygame
from button import button

#Tile implementation and stores number using button implementation

#Inheritance Design
class tile (button):
    def __init__ (self, color, x, y, width, height, text):
        super().__init__ (color, x, y, width, height, text)
        self.text = ''
    
    def draw(self,win,outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '' or self.text != '0':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
            
    def setVal (self, num):
        if (isinstance (num, int)):
            self.text = str (num)
        elif (num == None):
            self.text = ''
        
    def getVal (self):
        if self.text != '':
            return int (self.text)