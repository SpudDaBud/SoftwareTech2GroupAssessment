import pygame
import sys 
import heapq

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

#draws the grid of the application  
def draw_grid(screen, font): 
 
    screen.fill((255, 255, 255))
    infoText1 = FONT.render("Types: 1.obs,2.start,3.end. Please use format number, type", True, (0, 0, 0))
    screen.blit(infoText1, (0, 700))
    infoText2 = FONT.render("and  hit enter to store data. You can", True, (0, 0, 0)) 
    screen.blit(infoText2, (0, 800))
    infoText3 = FONT.render("then use tab to load the path and DEL to clear.", True, (0, 0,0))
    screen.blit(infoText3, (0, 900))

    pygame.draw.rect(screen, (0, 0, 0), inputRect, 2)
    text_surface = FONT.render(userText, True, (0, 0, 0))
    screen.blit(text_surface, (inputRect.x + 5, inputRect.y + 5))



    for r in range(ROWS): 
        for c in range(COLS): 

            color = (200, 200, 200) 
            textColor = (0, 0, 0)

            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            idx = r * COLS + c
            pos = (r, c)

            if pos in obstacles: 
                color = (255, 0, 0)

            elif pos in start: 
                color = (0, 255, 0)

            elif pos in end:
                color = (0, 0, 0)
                textColor = (255, 255, 255)

            if len(path) > 0: 
                if pos in path: 
                    color  = (0, 255, 0) 
                    textColor = (0, 0, 0)


            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

            text = FONT.render(str(idx), True, textColor)
            screen.blit(text, text.get_rect(center=rect.center))

          

    pygame.display.flip()

#creates the path based on the directions, start position, obstacles and end position 

def create_path(start_pos, end_pos): 

    directions = [(1, 0), (-1,0), (0, 1), (0, -1)]

    dist = {} 
    prev = {} 

    for r in range(ROWS):
        for c in range(COLS): 
            dist[(r,c)] = float('inf')

    dist[start_pos] = 0

    pq = [(0, start_pos)]

    while pq: 

        current_dist, current = heapq.heappop(pq) 

        if current == end_pos: 
            break

        for dr, dc in directions: 

            nr, nc = current[0] + dr, current[1] + dc  
            neighbor = (nr, nc) 

            if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS: 
                continue 

            if neighbor in obstacles: 
                continue 

            new_dist = current_dist + 1  

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = current
                heapq.heappush(pq, (new_dist, neighbor))

    path = []
    current = end_pos

    while current in prev:
        path.append(current)
        current = prev[current]

    path.reverse()
    return path


def main(screen, font): 

    global userText
    userText = ''

    running = True 

    while running: 
        #key event listener 
        for event in pygame.event.get(): 

            if event.type == pygame.QUIT: 
                running = False 

            if event.type == pygame.KEYDOWN: 

                if event.key == pygame.K_BACKSPACE: 
                    userText = userText[:-1]

                elif event.key == pygame.K_RETURN: 

                    parts = userText.split(",")

                    idx = int(parts[0])
                    r = idx // COLS
                    c = idx % COLS
                    pos = (r, c)

                    if parts[1] == "obs":
                        obstacles[pos] = "obs"

                    elif parts[1] == "start":
                        start.clear()
                        start[pos] = "start"

                    elif parts[1] == "end":
                        end.clear()
                        end[pos] = "end"

                    userText = ''

                elif event.key == pygame.K_TAB: 

                    start_pos = next(iter(start))
                    end_pos = next(iter(end))

                    print(start_pos)
                    print(end_pos)

                    global path
                    path = create_path(start_pos, end_pos)

                    print(path)
                elif event.key == pygame.K_DELETE: 
                    path.clear() 
                    start.clear() 
                    end.clear() 
                    obstacles.clear()

                else:
                    userText += event.unicode
       
        draw_grid(screen, font) 


if __name__ == "__main__": 
    
    main()
    print(obstacles)
    print(start)
    print(end)
    print(dump)