import pygame
import sys
import math
from datetime import timedelta

pygame.init()
#defines global and importnat varibles 
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

heap = []

inputRect = pygame.Rect(350, 560, 300, 32)
exitButton = pygame.Rect(50, 560, 100, 32)
userText = ''
errorMsg = ''
finalTime = ''
errorState = False 
#draws the menu of the program 
def draw_menu(): 

    title_text = FONT.render("Welcome to the program", True, (0, 0,0))
    screen.blit(title_text, (400, 100) )
    menu_text = FONT.render("Use TAB to load the insertions,  RCTRL to show the highest priority item and", True, (0, 0, 0))
    screen.blit(menu_text, (200, 200))
    if errorState != True and len(errorMsg) != 0:
        errorText = FONT.render(errorMsg, True, (0, 0, 0)) 
        screen.blit(errorText, (250, 400))
    else: 
        pass 
    extra_text = FONT.render("LCTRL to delete a specific items. Format is (1, 8.00, wake up)", True, (0, 0,0))
    screen.blit(extra_text, (275, 250))
    pygame.draw.rect(screen, (0, 0, 0), inputRect, 2)
    text_surface = FONT.render(userText, True, (0, 0, 0))
    screen.blit(text_surface, (inputRect.x + 5, inputRect.y + 5))

    exitText = FONT.render("Exit", True, (0, 0, 0))
   
    pygame.draw.rect(screen, (0, 0, 0), exitButton,  2)
    
    textRect = exitText.get_rect(center=exitButton.center)
    screen.blit(exitText, textRect)
    pygame.display.flip()
#draws the heap 
def draw_heap(heap, highlight_indices=None):
    global errorMsg

    if highlight_indices is None:
        highlight_indices = []

    screen.fill((255, 255, 255))
    #if heap is empty display a message on screen 
    if not heap:
        text = FONT.render("Heap is empty", True, (0, 0, 0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

    else:
        node_positions = []
        #draws the nodes and lines 
        for i in range(len(heap)):
            level = int(math.log2(i + 1))
            index_in_level = i - (2 ** level - 1)
            gap = WIDTH // (2 ** level + 1)
            x = gap * (index_in_level + 1)
            y = 60 + level * 70
            node_positions.append((x, y))

        for i in range(len(heap)):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(heap):
                pygame.draw.line(screen, (0, 0, 0), node_positions[i], node_positions[left], 2)

            if right < len(heap):
                pygame.draw.line(screen, (0, 0, 0), node_positions[i], node_positions[right], 2)

        for i, val in enumerate(heap):
            priority, time, desc = val

            color = (100, 200, 250)
            if i in highlight_indices:
                color = (255, 100, 100)

            pygame.draw.circle(screen, color, node_positions[i], 40)

            t1 = FONT.render(str(priority), True, (0, 0, 0))
            screen.blit(t1, t1.get_rect(center=(node_positions[i][0], node_positions[i][1] - 8)))

            t2 = FONT.render(desc, True, (0, 0, 0))
            screen.blit(t2, t2.get_rect(center=(node_positions[i][0], node_positions[i][1] + 10)))
            t3 = FONT.render(str(time), True, (0, 0, 0))
            screen.blit(t3, t3.get_rect(center=(node_positions[i][0], node_positions[i][1] + 30)) )

    pygame.draw.rect(screen, (0, 0, 0), inputRect, 2)
    text_surface = FONT.render(userText, True, (0, 0, 0))
    screen.blit(text_surface, (inputRect.x + 5, inputRect.y + 5))

   
    pygame.display.flip()

#orders the heap 
def heapify_up(heap, index):
    while index > 0:
        parent = (index - 1) // 2

        if heap[parent][0] > heap[index][0]:
            heap[parent], heap[index] = heap[index], heap[parent]
            index = parent
        if heap[parent][1] > heap[index][1] and heap[parent][0] == heap[index][0]: 
            heap[parent], heap[index] = heap[index], heap[parent]
            index = parent
        else:
            break


def heapify_down(heap, index):
    n = len(heap)

    while True:
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < n and heap[left][0] < heap[smallest][0]:
            smallest = left

        if right < n and heap[right][0] < heap[smallest][0]:
            smallest = right

        if smallest != index:
            heap[index], heap[smallest] = heap[smallest], heap[index]
            index = smallest
        else:
            break

#inserts values into the heap and then draws them 
def insert(heap, val):
    heap.append(val)
    draw_heap(heap, [len(heap) - 1])
    pygame.time.wait(300) 
 
    heapify_up(heap, len(heap) - 1)

#extracts the earliest object in the heap
def extract_min(heap):
    if not heap:
        return None

    root = heap[0]
    heap[0] = heap[-1]
  
    heap.pop()
    heapify_down(heap, 0)
    return root 
#displays the earliest object in the heap 
def showMin(heap): 
    if not heap:
        return

    screen.fill((255, 255, 255))
   
    priority, time,  desc = heap[0]

    fullText = str(priority) + " " + str(time) + " " + desc
    text = FONT.render(fullText, True, (0, 0, 0))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

    pygame.time.wait(1000)


def main():
    global userText, errorMsg
    global insertions
    insertions = []
    running = True
    inserted = False

    while running:
        global idx 
        idx = 0

    
      
       
       #key event listener 
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN: 
                pos = event.pos 
                if exitButton.collidepoint(pos): 
                    running = False 
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:
                    userText = userText[:-1]
       
                elif event.key == pygame.K_RETURN:
                    parts = userText.split(",")

                    if len(parts) != 3:
                        errorState = True
                        errorMsg = "Error please use format: priority description eg (1, 8.00, wake up)"
                        pygame.time.wait(1000)
                    else:
                       
                        priority = int(parts[0])
                        try: 
                            global finalTime
                            
                            time = float(parts[1])
                            finalTime = timedelta(hours=time)
                        except: 
                            
                            errorState = True 
                            errorMsg =  "Error please use format: priority description eg (1, 8.00, wake up)"
                        desc = parts[2]
                        insertions.append((priority, finalTime, desc))
                        userText = ""
                     

                

                elif event.key == pygame.K_LCTRL: 
                    parts = userText.split(",")
                
                    for i in range(len(heap)): 
                        try: 
                            
                            
                            if(int(parts[0]) == (heap[i][0])): 
                                print("success")
                                heap.pop(i)
                            else: 
                                errorState = True 
                                errorMsg = 'Incorrect order please use format e.g  (1, 8.00, wake up)'
                        except: 
                            break 

                elif event.key == pygame.K_TAB: 
                    if idx < len(insertions):
                        for idx in range(len(insertions)): 
                            insert(heap, insertions[idx])
                            idx += 1
                            pygame.time.wait(600)
                    draw_heap(heap)
                    insertions = []
                    inserted = True
                    errorMsg = '' 
                    errorState = False 
                elif event.key == pygame.K_RCTRL: 
                    showMin(heap)
                    earliest = extract_min(heap)
                    print(earliest)
                    
                    
                    
                        
               


                else:
                    userText += event.unicode
        if inserted == False: 
            screen.fill((255, 255,255))

            draw_menu()
        else: 
            if len(heap) != 0: 
                screen.fill((255, 255, 255))
                draw_heap(heap) 
            else: 
                draw_heap(heap) 
                pygame.time.wait(1000)
                screen.fill((255, 255, 255))
                inserted = False

    
        clock.tick(30)

  


if __name__ == "__main__":
    main()
