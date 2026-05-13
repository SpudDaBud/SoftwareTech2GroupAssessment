

import pygame
import sys
import math
from datetime import timedelta
from python_files import PhaseThreeHeap

pygame.init()
#defines global and importnat varibles 
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

heap = []

inputRect = pygame.Rect(150, HEIGHT - 40, 300, 32)
userText = ''
errorMsg = ''
finalTime = 0.0
errorState = False 
#draws the menu of the program 





#shows what happens when priority and time are alll different, expected result: (1, 11.0, brush teeth), (2, 12.0, have breakfast),  (3, 10.0, wake up) 
def basicInsertion(): 

    
    newHeap = [(3, 10.0, 'wake up'), (1, 11.0, 'brush teeth'), (2, 12.0, 'have breakfast')]
    for i in range(len(newHeap)): 
        PhaseThreeHeap.insert(heap, newHeap[i])
    PhaseThreeHeap.draw_heap(heap)
#shows what happens when priority is the same  but time is different, expected result:  (1,9.0, brush teeth), (1, 11.0, wake up), (1, 14.0, have breakfast)  
def timeInsertion(): 
    heap = [] 
    newHeap = [(1, 11.0, 'wake up'), (1, 9.0, 'brush teeth'), (1, 14.0, 'have breakfast')]
    
    for i in range(len(newHeap)): 
        PhaseThreeHeap.insert(heap, newHeap[i])
    PhaseThreeHeap.draw_heap(heap)
#shows what happens when everything is the same, expected result:  (1, 10.0, wake up), (1, 10.0, brush teeth), 1, 10.0, have breakfast) 
def sameInsertion(): 
    heap = [] 
    newHeap = [(1, 10.0, 'wake up'), (1, 10.0, 'brush teeth'), (1, 10.0, 'have breakfast')]
    
    for i in range(len(newHeap)): 
        PhaseThreeHeap.insert(heap, newHeap[i])
    PhaseThreeHeap.draw_heap(heap)



if __name__ == "__main__":
    basicInsertion() 
    pygame.time.wait(3000)
    timeInsertion()
    pygame.time.wait(3000)
    sameInsertion() 
    pygame.time.wait(3000)
