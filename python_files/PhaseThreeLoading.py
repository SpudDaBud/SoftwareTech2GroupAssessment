import pygame


from python_files import PhaseThreeGrid

from python_files import PhaseThreePath

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

BLOCK_WIDTH, BLOCK_HEIGHT = 200, 40
START_X = (WIDTH - BLOCK_WIDTH) // 2
BASE_Y = HEIGHT - BLOCK_HEIGHT - 20


def draw_text(text, pos):
    txt = FONT.render(text, True, (0, 0, 0))
    screen.blit(txt, pos)

def main_menu(): 
    screen.fill((200, 200, 250)) 
    draw_text("Puzzle Explorer", (400, 50))

    buttons = {
        "Pathfinding Puzzles": pygame.Rect(400, 150, 270, 50), 
        "Dynamic Puzzles": pygame.Rect(400, 230, 270, 50)
    }
    for text, rect in buttons.items(): 
        pygame.draw.rect(screen, (150, 150, 200), rect)
        draw_text(text, (rect.x + 20, rect.y + 10))

    pygame.display.flip()
    return buttons


def puzzles_module(): 
    PhaseThreeGrid.main() 

def dynamic_module(): 
    PhaseThreePath.main() 
def main():
    running = True
    current_module = None
    buttons = main_menu()
    WIDTH, HEIGHT = 1000, 600
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and current_module is None:
                pos = event.pos

                for name, rect in buttons.items():
                    if rect.collidepoint(pos):
                        current_module = name

        if current_module is None:
            buttons = main_menu()
        else:

            if current_module == "Pathfinding Puzzles":
                w, h = 800, 1000
                screen = pygame.display.set_mode((w, h))
                puzzles_module()
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            elif current_module == "Dynamic Puzzles": 
                w, h = 600, 800
                screen = pygame.display.set_mode((w, h))
                dynamic_module()
                screen = pygame.display.set_mode((WIDTH, HEIGHT))

            current_module = None

        clock.tick(30)





if __name__ == "__main__": 
    main() 
