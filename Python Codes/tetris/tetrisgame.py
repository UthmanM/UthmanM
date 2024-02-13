import pygame 
import sys 
from Tetris_class import *
from Big_block import *

pygame.init()
dark_blue=(44,44,127)

screen=pygame.display.set_mode((300,600))
pygame.display.set_caption("Attahs Version of Tetris")

clock=pygame.time.Clock()
game_grid= Grid()
block=L_block
game_grid.print_grid()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    
    #Display
    screen.fill(dark_blue)
    game_grid.draw (screen) 
    block.draw  ()
    
    
    pygame.display.update()
    clock.tick(60)
    
    