import pygame
import sys
from modules.stack import Stack, Queue

pygame.init()

WIDTH, HEIGHT = 800, 600
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
    draw_text("Algorithm Explorer", (WIDTH // 3, 50))

    buttons = {
        "Data Structures": pygame.Rect(300, 150, 200, 50),
        "Sorting": pygame.Rect(300, 230, 200, 50),
        "Graphs": pygame.Rect(300, 310, 200, 50),
        "Heap": pygame.Rect(300, 390, 200, 50),
        "Puzzles": pygame.Rect(300, 470, 200, 50),
    }

    for text, rect in buttons.items():
        pygame.draw.rect(screen, (150, 150, 200), rect)
        draw_text(text, (rect.x + 20, rect.y + 10))

    pygame.display.flip()
    return buttons


# Placeholder functions for different modules
def data_structures_module():
    # Implement stack, queue, linked list, BST visualization here

    # STACK VIS CODE HERE:
    def stack_visualization(screen, font):
        stack = Stack()
        counter = 1
        running = True

        push_button = pygame.Rect(0, 500, 150, 50)
        pop_button = pygame.Rect(650, 500, 150, 50)
        back_button = pygame.Rect(10, 10, 150, 50)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN: 

                    if push_button.collidepoint(event.pos): #MOUSE BTN FOR PUSH
                        stack.push(counter)
                        counter += 1

                    elif pop_button.collidepoint(event.pos) and not stack.is_empty(): #MOUSE BTN FOR POP
                        stack.pop()

                    elif back_button.collidepoint(event.pos):
                        running = False

            screen.fill((50, 50, 50))
            
            #draw push button
            pygame.draw.rect(screen, (0, 180, 0), push_button)
            push_txt = font.render("Push", True, (255, 255, 255))
            screen.blit(push_txt, (push_button.centerx - push_txt.get_width()//2, push_button.centery - push_txt.get_height()//2))

            #draw pop button
            pygame.draw.rect(screen, (0, 180, 0), pop_button)
            pop_txt = font.render("Pop", True, (255, 255, 255))
            screen.blit(pop_txt, (pop_button.centerx - pop_txt.get_width()//2, pop_button.centery - pop_txt.get_height()//2))

            #back button    
            pygame.draw.rect(screen, (0, 180, 0), back_button)
            back_txt = font.render("Back", True, (255, 255, 255))
            screen.blit(back_txt, (back_button.centerx - back_txt.get_width()//2, back_button.centery - back_txt.get_height()//2))


            for i, val in enumerate(stack._data):
                rect = pygame.Rect(
                    START_X,
                    BASE_Y - i * (BLOCK_HEIGHT + 5),
                    BLOCK_WIDTH,
                    BLOCK_HEIGHT,
                )
                pygame.draw.rect(screen, (100, 150, 250), rect)

                text = font.render(str(val), True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

            pygame.display.flip()
            clock.tick(30)

    # QUEUE VIS CODE HERE:
    def queue_visualization(screen, font):  # queue vis
        queue = Queue()
        counter = 1
        running = True

        enqueue_button = pygame.Rect(0, 500, 150, 50)
        dequeue_button = pygame.Rect(650, 500, 150, 50)
        back_button = pygame.Rect(10, 10, 150, 50)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN: 

                    if enqueue_button.collidepoint(event.pos): #MOUSE BTN FOR PUSH
                        queue.push(counter)
                        counter += 1

                    elif dequeue_button.collidepoint(event.pos) and not queue.is_empty(): #MOUSE BTN FOR POP
                        queue.pop()

                    elif back_button.collidepoint(event.pos):
                        running = False

            screen.fill((50, 50, 50))

            #draw enqueue button
            pygame.draw.rect(screen, (0, 180, 0), enqueue_button)
            enqueue_txt = font.render("Push", True, (255, 255, 255))
            screen.blit(enqueue_txt, (enqueue_button.centerx - enqueue_txt.get_width()//2, enqueue_button.centery - enqueue_txt.get_height()//2))

            #draw dequeue button
            pygame.draw.rect(screen, (0, 180, 0), dequeue_button)
            dequeue_txt = font.render("Pop", True, (255, 255, 255))
            screen.blit(dequeue_txt, (dequeue_button.centerx - dequeue_txt.get_width()//2, dequeue_button.centery - dequeue_txt.get_height()//2))

            #back button    
            pygame.draw.rect(screen, (0, 180, 0), back_button)
            back_txt = font.render("Back", True, (255, 255, 255))
            screen.blit(back_txt, (back_button.centerx - back_txt.get_width()//2, back_button.centery - back_txt.get_height()//2))

            for i, val in enumerate(queue._data):
                rect = pygame.Rect(
                    START_X,
                    BASE_Y - i * (BLOCK_HEIGHT + 5),
                    BLOCK_WIDTH,
                    BLOCK_HEIGHT,
                )
                pygame.draw.rect(screen, (100, 150, 250), rect)

                text = font.render(str(val), True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

            pygame.display.flip()
            clock.tick(30)

    # CODE FOR RUNNING THE MENU INSIDE THE DATA_STUCTRES MODULE:
    font = pygame.font.SysFont(None, 28)

    menu_items = [
        "Stack Visualization (press enter)",
        "Queue Visualization (press enter)",
        "Linked List Visualization (not implemented)",
        "BST Visualization (not implemented)",
        "Back",
    ]

    selected = 0
    running = True

    while running:
        screen.fill((220, 220, 220))

        for i, item in enumerate(menu_items):
            color = (255, 0, 0) if i == selected else (0, 0, 0)
            text = font.render(item, True, color)
            screen.blit(text, (100, 100 + i * 40))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(menu_items)

                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(menu_items)

                elif event.key == pygame.K_RETURN:
                    choice = menu_items[selected]

                    if choice == "Stack Visualization (press enter)":
                        stack_visualization(screen, font)

                    elif choice == "Queue Visualization (press enter)":
                        queue_visualization(screen, font)

                    elif choice == "Back":
                        running = False

        clock.tick(30)


def sorting_module():
    # Bubble sort, selection sort, merge sort visualizations
    pass


def graphs_module():
    # BFS, DFS visualization with interactive graph
    pass


def heap_module():
    # Heap insertion and extraction visualization
    pass


def puzzles_module():
    # Pathfinding, event simulation, DP puzzles
    pass


def main():
    running = True
    current_module = None
    buttons = main_menu()

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
            if current_module == "Data Structures":
                data_structures_module()
            elif current_module == "Sorting":
                sorting_module()
            elif current_module == "Graphs":
                graphs_module()
            elif current_module == "Heap":
                heap_module()
            elif current_module == "Puzzles":
                puzzles_module()

            current_module = None

        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
