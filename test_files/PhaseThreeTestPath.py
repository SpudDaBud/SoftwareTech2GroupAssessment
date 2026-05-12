
import pygame
import sys
from python_files import PhaseThreePath
pygame.init()
#defines important variables 
WIDTH, HEIGHT = 600, 800
ROWS, COLS = 6, 6
CELL_SIZE = WIDTH // COLS

screen = pygame.display.set_mode((WIDTH, HEIGHT))


path = []
userText  = ''
global current_dp
global current_path
current_dp = None 
current_path = None




#basic path
def basicPath(): 

    PhaseThreePath.obstacles.clear()
    PhaseThreePath.obstacles = {(0,1), (1, 1)}
    PhaseThreePath.current_dp, PhaseThreePath.current_path = PhaseThreePath.count_paths(PhaseThreePath.obstacles)
    for i in range(len(PhaseThreePath.current_path)):
                        screen.fill((255, 255, 255))
                        
                        # draw grid with partial path
                        PhaseThreePath.draw_grid(PhaseThreePath.current_dp, path=PhaseThreePath.current_path[:i+1])
                        
                        pygame.time.wait(200)
    pygame.time.wait(1000)
#blocked path
def blockedPath(): 
    
    PhaseThreePath.obstacles.clear()
    PhaseThreePath.obstacles = {(5,4), (4, 5)}
    PhaseThreePath.current_dp.clear()
    PhaseThreePath.current_path.clear()
    PhaseThreePath.current_dp, PhaseThreePath.current_path = PhaseThreePath.count_paths(PhaseThreePath.obstacles)
    for i in range(len(PhaseThreePath.current_path)):
                        screen.fill((255, 255, 255))
                        
                        # draw grid with partial path
                        PhaseThreePath.draw_grid(PhaseThreePath.current_dp, path=PhaseThreePath.current_path[:i+1])
                        
                        pygame.time.wait(200)
    pygame.time.wait(1000)

if __name__ == "__main__":
    basicPath()
    blockedPath()
       
