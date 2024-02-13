from color_p import coo
import pygame
class Grid:
    def __init__(self) :
        self.num_rows=20
        self.num_cols=10
        self.cell_size=30
        self.colors= coo
        self.grid = [ [0 for j in range(self.num_rows)]  for i in range(self.num_cols)]  
       
        
    def print_grid (self):
        for row in range (self.num_rows):
            for column in range (self.num_cols):
             print(self.grid[row][column], end ="")
        print ()
        
   
    
    
    def draw(self,screen):
        for row in range (self.num_rows):
            for column in range (self.num_cols):
                cell_value=self.grid[row][column]
                cell_rect=pygame.Rect(column*self.cell_size+1,row*self.cell_size+1,self.cell_size-1,self.cell_size-1)
                pygame.draw.rect(screen,coo,cell_rect)