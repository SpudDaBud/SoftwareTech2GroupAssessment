"""This program uses pygame to showcase a visualisation of a Linked List"""

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

BLOCK_WIDTH, BLOCK_HEIGHT = 200, 40
START_X = (WIDTH - BLOCK_WIDTH) // 2
BASE_Y = HEIGHT - BLOCK_HEIGHT - 20


# LL CLASSES:
class Node:
    """represents a single node in a LL"""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """a singly Linked List implemeted with common operations"""

    def __init__(self):
        self.head = None

    def append(self, value):
        """used to add a new node with a given value to the end of the LL"""
        if not self.head:
            self.head = Node(value)
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def delete(self, value):
        """used to delete the last value from the LL"""
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

    def reverse(self):  
        """
        This funtion uses iteration to reverse the LL

        uses 3 pointers:
        -prev: keeps track of the previous node (the one behind current node)
        -current: tracks the current node being processed
        -next_node: this is a temp value to the rest of the LL so it isn't lost

        the funtion goes theough the list and reverses each nodes link until 
        the enteire LL is reversed
        """

        prev = None  
        current = self.head  

        while current:
            next_node = current.next 
            current.next = prev  
            prev = current  
            current = next_node  

        self.head = prev

    def insert_at_position(self, value, position):
        """
        This is a special funtion used to insert a node at a specific position in the LL

        Variables:
        -new_node: this is the value of the node the user has inserted
        -self.head: refers to the 'head' of the LL
        -current: current is a temp value assinged to the next node as you travel in the LL 
        -index: this is used to keep track of current's value in the LL

        the funtion begins with an 'if' statement checking if the new_node's position is at 0.
        if the pos is 0, it takes the next node inserted by the user and makes that the 'head'
        of the LL. 

        The 'while' loop forces the current node and index values to change by 1

        the 'if current' statement checks if you reached a valid node in the LL, and is responsibel for the actual insertion.
        If you reaches a valid node, make the new_node point to the node infront, and maek the node behind new_node 
        point to new_node
        """
    
        new_node = Node(value)

        if position == 0:
            new_node.next = self.head 
            self.head = new_node  
            return

        current = self.head
        index = 0

        while current and index < position - 1:  
            current = current.next
            index += 1

        if current:  
            new_node.next = current.next
            current.next = new_node


def linked_list_visualization():
    pygame.init()

    WIDTH, HEIGHT = 1100, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    FONT = pygame.font.SysFont(None, 30)
    clock = pygame.time.Clock()

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
        arrow_head = [(end_pos[0] - 10, end_pos[1] - 5), end_pos, (end_pos[0] - 10, end_pos[1] + 5)]
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

        info = FONT.render(  # displays the value of the current value of the node, adn the current position
            f"Value: {custom_value}        Position: {custom_position}",
            True,  # makes the edges look smoother
            (0, 0, 0))  # black colour
        
        screen.blit(info, (20, 20))

        controls = FONT.render(
            "Up/Down = Value    Left/Right = Position   A = Insert  D = Delete  R = Reverse \n\n Press ESC to go Back",
            True,
            (0, 0, 0))
        
        screen.blit(controls, (20, 50))

    def main():
        """
        This is the main funtion responsible for handling inputs and custom value sform the user
        """
        ll = LinkedList()

        ll.append(1)

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

                    if event.key == pygame.K_UP:  # chaneges the insert value up by 5
                        custom_value += 1

                    elif event.key == pygame.K_DOWN:  # chaneges the insert value down by 5
                        custom_value -= 1

                    elif event.key == pygame.K_RIGHT:  # pressing right changes the position by 1
                        custom_position += 1

                    elif event.key == pygame.K_LEFT:  # pressing left changes the position by 1
                        custom_position -= 1

                    elif event.key == pygame.K_a:   # press a to add to LL
                        ll.insert_at_position(custom_value, custom_position)

                    elif event.key == pygame.K_d:   # press d to remove last node
                        value = ll.to_list()
                        if value:
                            ll.delete(value[-1])

                    elif event.key == pygame.K_r:   # press r to reverse LL
                        ll.reverse()

                    elif event.key == pygame.K_ESCAPE:
                        running = False

    main()
