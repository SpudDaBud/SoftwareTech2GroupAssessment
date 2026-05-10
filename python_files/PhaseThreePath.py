import pygame
import sys

pygame.init()
#defines important variables 
WIDTH, HEIGHT = 600, 800
ROWS, COLS = 6, 6
CELL_SIZE = WIDTH // COLS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

obstacles = {}
path = []
userText  = ''
inputRect = pygame.Rect(150, HEIGHT - 40, 300, 32)
global current_dp
global current_path
current_dp = None 
current_path = None


#draws the application and the grid 
def draw_grid(dp, highlight=None, path=None):
    screen.fill((255, 255, 255))
    text = FONT.render("Use TAB to enter data in format number, obs", True, (0, 0,0))
    screen.blit(text, (100, 700))

    
    pygame.draw.rect(screen, (0, 0, 0), inputRect, 2)
    text_surface = FONT.render(userText, True, (0, 0, 0))
    screen.blit(text_surface, (inputRect.x + 5, inputRect.y + 5))
    #checks if dp is null, and then displays the total paths 
    if current_dp != None:
        fullText = f"Total unique paths: {current_dp[ROWS - 1][COLS - 1]}"
        text = FONT.render(fullText, True, (0, 0, 0))
        screen.blit(text, (100, 650))
    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            textColor = (0, 0, 0)
            color = (200, 200, 200)
            #decides the color by if there in the path or the obstacles 
           

            if path and (r, c) in path:
                color = (100, 255, 100)

            if highlight == (r, c):
                color = (255, 180, 180)
            if (r, c) in obstacles:
                color = (0, 0, 0)
                textColor = (255, 255, 255)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)
            
            val = dp[r][c]
            if val is not None:
                text = FONT.render(str(val), True, textColor)
                screen.blit(text, text.get_rect(center=rect.center))

    pygame.display.flip()
#draws the menu 
def menu(): 
    screen.fill((255, 255, 255))
    text = FONT.render("Use TAB to enter data in format number, obs", True, (0, 0,0))
    screen.blit(text, (0, 700))
    if current_dp != None: 
        fullText =f"Total unique paths: {current_dp[ROWS - 1][COLS - 1]}"
        text = FONT.render(fullText, True, (0, 0, 0))
        screen.blit(text, (100, 650))
    
    pygame.draw.rect(screen, (0, 0, 0), inputRect, 2)
    text_surface = FONT.render(userText, True, (0, 0, 0))
    screen.blit(text_surface, (inputRect.x + 5, inputRect.y + 5))
    i = 0 
    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            textColor = (0, 0, 0)
            color = (200, 200, 200)

            if (r, c) in obstacles:
                color = (0, 0, 0)
                textColor = (255, 255, 255)

     

    

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

            text = FONT.render(str(i), True, textColor)
            screen.blit(text, text.get_rect(center=rect.center))
            i += 1


    
    pygame.display.flip()


#counts the paths 
def count_paths():
    dp = [[0] * COLS for _ in range(ROWS)]
    parent = [[None] * COLS for _ in range(ROWS)]

    for r in range(ROWS):
        for c in range(COLS):

            if (r, c) in obstacles:
                dp[r][c] = 0
                continue

            if r == 0 and c == 0:
                dp[r][c] = 1
                continue

            up = dp[r - 1][c] if r > 0 else 0
            left = dp[r][c - 1] if c > 0 else 0

            dp[r][c] = up + left

            if r > 0 and (r - 1, c) not in obstacles:
                parent[r][c] = "U"
            elif c > 0 and (r, c - 1) not in obstacles:
                parent[r][c] = "L"

            draw_grid(dp, (r, c))


            
    r, c = ROWS - 1, COLS - 1
    path.clear()

    if dp[r][c] == 0:
        return dp, []

    while (r, c) != (0, 0):
        path.append((r, c))

        if parent[r][c] == "U":
            r -= 1
        else:
            c -= 1

    path.append((0, 0))
    path.reverse()

    return dp, path
def main():
    global userText
    global current_dp
    global current_path
    running = True
    while running == True: 
        for event in pygame.event.get():
            #key event listeners 

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_BACKSPACE:
                    userText = userText[:-1]
                

                elif event.key == pygame.K_RETURN:

                    parts = userText.split(",")

                    idx = int(parts[0])

                    r = idx // COLS
                    c = idx % COLS

                    pos = (r, c)

                    if parts[1] == "obs":
                        obstacles[pos] = "obs"

                    userText = ""
                elif event.key == pygame.K_TAB: 
                    current_dp, current_path = count_paths()
          
                    pygame.time.wait(3000)

                else:
                    userText += event.unicode
        if current_dp is None:
            menu()
        else:
            draw_grid(current_dp, path=current_path)

     
  
        clock.tick(60)
    pygame.quit() 

if __name__ == "__main__":

        main()
