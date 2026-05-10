import pygame
import sys
import math

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
#draws the menu of the program 
def draw_menu(): 

    title_text = FONT.render("Welcome to the program", True, (0, 0,0))
    screen.blit(title_text, (200, 0) )
    menu_text = FONT.render("Use TAB to load the insertions,  RCTRL to show the highest priority item and", True, (0, 0, 0))

    screen.blit(menu_text, (0, 200))
    extra_text = FONT.render("LCTRL to delete a specific items", True, (0, 0,0))
    screen.blit(extra_text, (175, 250))
    pygame.draw.rect(screen, (0, 0, 0), inputRect, 2)
    text_surface = FONT.render(userText, True, (0, 0, 0))
    screen.blit(text_surface, (inputRect.x + 5, inputRect.y + 5))
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
            priority, desc = val

            color = (100, 200, 250)
            if i in highlight_indices:
                color = (255, 100, 100)

            pygame.draw.circle(screen, color, node_positions[i], 20)

            t1 = FONT.render(str(priority), True, (0, 0, 0))
            screen.blit(t1, t1.get_rect(center=(node_positions[i][0], node_positions[i][1] - 8)))

            t2 = FONT.render(desc, True, (0, 0, 0))
            screen.blit(t2, t2.get_rect(center=(node_positions[i][0], node_positions[i][1] + 10)))

    pygame.draw.rect(screen, (0, 0, 0), inputRect, 2)
    text_surface = FONT.render(userText, True, (0, 0, 0))
    screen.blit(text_surface, (inputRect.x + 5, inputRect.y + 5))

    if errorMsg:
        err = FONT.render(errorMsg, True, (200, 0, 0))
        screen.blit(err, (10, HEIGHT - 80))

    pygame.display.flip()

#orders the heap 
def heapify_up(heap, index):
    while index > 0:
        parent = (index - 1) // 2

        if heap[parent][0] > heap[index][0]:
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
    priority, desc = heap[0]

    fullText = str(priority) + " " + desc
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

        errorMsg = ""
      
       
       #key event listener 
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:
                    userText = userText[:-1]

                elif event.key == pygame.K_RETURN:
                    parts = userText.split(",")

                    if len(parts) != 2:
                        errorMsg = "Format: priority description (e.g. 1 wake up)"
                        pygame.time.wait(1000)
                    else:
                       
                        priority = int(parts[0])
                        desc = parts[1]
                        insertions.append((priority, desc))
                        userText = ""
                     

                elif event.key == pygame.K_0:
                    extracted = extract_min(heap)
                    if extracted:
                        print("Processing:", extracted)

                elif event.key == pygame.K_LCTRL: 
                    parts = userText.split(",")
                
                    for i in range(len(heap)): 
                        try: 
                            if(int(parts[0]) == (heap[i][0])): 
                                print("success")
                                heap.pop(i)
                            else: 
                                pass 
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

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()