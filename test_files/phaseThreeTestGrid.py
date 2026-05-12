import pygame
import sys 
import heapq
from python_files import PhaseThreeGrid

pygame.init() 
#defines some important and global variables 
WIDTH, HEIGHT = 600, 1000
ROWS, COLS = 4, 4
CELL_SIZE = WIDTH // COLS 

screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
FONT = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock() 

obstacles = {} 
start = {} 
end = {} 
path = [] 
dump = []

inputRect = pygame.Rect(150, HEIGHT - 40, 300, 32)

userText = ''
failedPath = False 


#basic insertion, normal start, end and obstacles 
def basicPath(): 
   
    PhaseThreeGrid.start.clear()
    PhaseThreeGrid.end.clear()
    PhaseThreeGrid.obstacles.clear()
    PhaseThreeGrid.path.clear()

    PhaseThreeGrid.start[(0, 0)] = "start"
    PhaseThreeGrid.end[(3, 3)] = "end"

    PhaseThreeGrid.obstacles[(0, 1)] = "obs"
    PhaseThreeGrid.obstacles[(1, 1)] = "obs"

    PhaseThreeGrid.start_pos = next(iter(PhaseThreeGrid.start))
    PhaseThreeGrid.end_pos = next(iter(PhaseThreeGrid.end))

    PhaseThreeGrid.fullPath = PhaseThreeGrid.create_path(PhaseThreeGrid.start_pos, PhaseThreeGrid.end_pos)

    PhaseThreeGrid.path.clear()

    if len(PhaseThreeGrid.fullPath) == 0:
        print("Path cannot be accessed")
        PhaseThreeGrid.failedPath = True
    else:
        PhaseThreeGrid.failedPath = False

    for cell in PhaseThreeGrid.fullPath:
        PhaseThreeGrid.path.append(cell)
        PhaseThreeGrid.draw_grid()
        pygame.time.wait(250)
    pygame.time.wait(1000)
    print("Final path:", PhaseThreeGrid.path)


#inaccessible or impossible path, blocked end 
def blockedEnd():

    PhaseThreeGrid.start.clear()
    PhaseThreeGrid.end.clear()
    PhaseThreeGrid.obstacles.clear()
    PhaseThreeGrid.path.clear()

    PhaseThreeGrid.start[(0, 0)] = "start"
    PhaseThreeGrid.end[(3, 3)] = "end"

    PhaseThreeGrid.obstacles[(2, 3)] = "obs"
    PhaseThreeGrid.obstacles[(3, 2)] = "obs"

    PhaseThreeGrid.start_pos = next(iter(PhaseThreeGrid.start))
    PhaseThreeGrid.end_pos = next(iter(PhaseThreeGrid.end))

    PhaseThreeGrid.fullPath = PhaseThreeGrid.create_path(PhaseThreeGrid.start_pos, PhaseThreeGrid.end_pos)

    PhaseThreeGrid.path.clear()

    if len(PhaseThreeGrid.fullPath) == 0:
        print("Path cannot be accessed")
        PhaseThreeGrid.failedPath = True
    else:
        PhaseThreeGrid.failedPath = False
    PhaseThreeGrid.draw_grid()

    pygame.time.wait(3000)
    print("Final path:", PhaseThreeGrid.path)


if __name__ == "__main__": 
    basicPath()
    pygame.time.wait(1000)
    blockedEnd() 
