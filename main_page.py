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
    draw_text ("Algorithm Explorer", (WIDTH // 3, 50))

    buttons = {
        "Data Structures": pygame.Rect(300, 150, 200, 50), 
        "Sorting": pygame.Rect(300, 230, 200, 50),
        "Graphs": pygame.Rect(300, 310, 200, 50),
        "Heap": pygame.Rect(300, 390, 200, 50),
        'Puzzles': pygame.Rect(300, 470, 200, 50)
    }

    for text, rect in buttons.items():
        pygame.draw.rect(screen, (150, 150, 200), rect)
        draw_text(text, (rect.x + 20, rect.y + 10))
    
    pygame.display.flip()
    return buttons

# Placeholder functions for different modules
def data_structures_module():
    # stack, queue, linked list, BST visualization here - completed by u3285413

    # LINKED LIST FUNTION     
    def linked_list_visualization():
        pygame.init()

        WIDTH, HEIGHT = 1100, 600
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        FONT = pygame.font.SysFont(None, 30)
        clock = pygame.time.Clock()

        # LL CLASSES:
        class Node:
            def __init__(self, value):
                self.value = value
                self.next = None
        
        class LinkedList:
            def __init__(self):
                self.head = None
            
            def append(self, value):
                if not self.head:
                    self.head = Node(value)
                    return
                
                current = self.head
                while current.next:
                    current = current.next
                current.next = Node(value)
        
            def delete(self, value):
                current = self.head
                prev = None
                while current:
                    if current.value == value:
                        if prev:
                            prev.next = current.next
                        else:
                            self.head = current.next
                        return True
                    prev = current
                    current = current.next
                return False
        
            def to_list(self):
                elems = []
                current = self.head
                while current:
                    elems.append(current.value)
                    current = current.next
                return elems
        
            def reverse(self): # new funtion for reversing the LL
                prev = None                         # sets the value to ALWAYS be one step behind current
                current = self.head                 # this is the value of the currnt node 

                while current:
                    next_node = current.next        # next_node is a temp value which stores the next node so we dont lose the list when reversing
                    current.next = prev             # this reverses the link
                    prev = current                  # prev moves forward by 1 spot the where 'current' was before
                    current = next_node             # moves current indicator to the next node
            
                self.head = prev
        
            def insert_at_position(self, value, position): # new funtion for inserting at a custom position 
                new_node = Node(value)

                if position == 0:
                    new_node.next = self.head           # if the position = 0, change the next node inserted to be 'first' actual node
                    self.head = new_node                # now the 'first' node becomes the new node
                    return 
                
                current = self.head
                index = 0

                while current and index < position -1:          # this while loop moves the 'current' node forward by 1
                    current = current.next
                    index += 1

                if current:                                     # this code makes the inserted node point what was there before
                    new_node.next = current.next
                    current.next = new_node
                    
        NODE_RADIUS = 25

        def draw_node(x, y, value, highlight=False):
            color = (255, 100, 100) if highlight else (100, 200, 250)
            pygame.draw.circle(screen, color, (x, y), NODE_RADIUS)
            text = FONT.render(str(value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x, y))
            screen.blit(text, text_rect)
        
        def draw_arrow(start_pos, end_pos):
            pygame.draw.line(screen, (0, 0, 0), start_pos, end_pos, 3)
        
            # Draw a simple arrow head
            dx = end_pos[0] - start_pos[0]
            dy = end_pos[1] - start_pos[1]
            angle = pygame.math.Vector2(dx, dy).angle_to(pygame.math.Vector2(1, 0))
            arrow_head = [
                (end_pos[0] - 10, end_pos[1] - 5), 
                end_pos,
                (end_pos[0] - 10, end_pos[1] + 5),
            ]
            pygame.draw.polygon(screen, (0, 0, 0), arrow_head)
        
        def draw_linked_list(linked_list, custom_value, custom_position, highlight_index=None):
            screen.fill((240, 240, 240))
            nodes = []
            current = linked_list.head
            x, y = 80, HEIGHT // 2
            idx = 0
            while current:
                nodes.append((x, y, current.value, idx == highlight_index))
                x += 150
                current = current.next
                idx += 1
            
            for i, (x, y, val, highlight) in enumerate(nodes):
                draw_node(x, y, val, highlight)
                if i < len(nodes) - 1:
                    draw_arrow((x + NODE_RADIUS, y), (x + 150 - NODE_RADIUS, y))

            info = FONT.render(                                                     # displays the value of the current value of the node, adn the current position
            f"Value: {custom_value}        Position: {custom_position}",    
            True,                                                       # makes the edges look smoother
            (0, 0, 0)                                                   # black colour
            )
            screen.blit(info, (20, 20)) 

            controls = FONT.render(
            "Up/Down = Value    Left/Right = Position   A = Insert  D = Delete  R = Reverse \n\n Press ESC to go Back", 
            True, 
            (0, 0, 0)
            )
            screen.blit(controls, (20, 50))     

        

        def main():
            ll = LinkedList()

            ll.append(5)
            
            custom_value = 10
            custom_position = 0

            running = True

            while running:
                draw_linked_list(ll, custom_value, custom_position)

                pygame.display.flip()  
            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        
                        if event.key == pygame.K_UP: # chaneges the insert value up by 5
                            custom_value +=5
                        
                        elif event.key == pygame.K_DOWN: # chaneges the insert value down by 5
                            custom_value -= 5
                        
                        elif event.key == pygame.K_RIGHT: # pressing right changes the position by 1
                            custom_position += 1
                        
                        elif event.key == pygame.K_LEFT: # pressing left changes the position by 1
                            custom_position -= 1

                        # press a to add to LL

                        elif event.key == pygame.K_a:
                            ll.insert_at_position(custom_value, custom_position)

                        # press d to remove last node

                        elif event.key == pygame.K_d:
                            value = ll.to_list()
                            if value:
                                ll.delete(value[-1])

                        # press r to reverse LL 

                        elif event.key == pygame.K_r:
                            ll.reverse()

                        elif event.key == pygame.K_ESCAPE:
                            running = False

        main()

    


    # stack vis code here:

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
                    BLOCK_HEIGHT
                )   
                pygame.draw.rect(screen, (100, 150, 250), rect) 
                  
                text = font.render(str(val), True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

            pygame.display.flip()
            clock.tick(30)

    def queue_visualization(screen, font):
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
            enqueue_txt = font.render("Enqueue", True, (255, 255, 255))
            screen.blit(enqueue_txt, (enqueue_button.centerx - enqueue_txt.get_width()//2, enqueue_button.centery - enqueue_txt.get_height()//2))

            #draw dequeue button
            pygame.draw.rect(screen, (0, 180, 0), dequeue_button)
            dequeue_txt = font.render("Dequeue", True, (255, 255, 255))
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
                    BLOCK_HEIGHT
                )   
                pygame.draw.rect(screen, (100, 150, 250), rect) 
                  
                text = font.render(str(val), True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

            pygame.display.flip()
            clock.tick(30)

    
        
        

        

    

    # CODE FOR RUNNIGN THE MENU INSIDE THE DATA_STRUCTRES MODULE:
    font = pygame.font.SysFont(None, 28)

    menu_items = [
        "Stack Visualization (press enter)",
        "Queue Visualization (press enter)",
        "Linked List Visualization (press enter)",
        "BST Visualization (not implemented)",
        "Back"
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
                    
                    elif choice == "Linked List Visualization (press enter)":
                        linked_list_visualization()


                    



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
            if event.type== pygame.QUIT:
                running= False
            
            elif event.type== pygame.MOUSEBUTTONDOWN and current_module is None:
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
            elif current_module == "Heaps":
                heap_module()
            elif current_module == "Puzzle":
                puzzles_module()

            current_module= None

        clock.tick(30)
    
    pygame.quit()

if __name__ == "__main__":
    main()

