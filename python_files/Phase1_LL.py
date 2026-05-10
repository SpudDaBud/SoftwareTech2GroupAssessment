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

        def reverse(self):  # new funtion for reversing the LL
            prev = None  # sets the value to ALWAYS be one step behind current
            current = self.head  # this is the value of the currnt node

            while current:
                next_node = (
                    current.next
                )  # next_node is a temp value which stores the next node so we dont lose the list when reversing
                current.next = prev  # this reverses the link
                prev = current  # prev moves forward by 1 spot the where 'current' was before
                current = next_node  # moves current indicator to the next node

            self.head = prev

        def insert_at_position(
            self, value, position
        ):  # new funtion for inserting at a custom position
            new_node = Node(value)

            if position == 0:
                new_node.next = (
                    self.head
                )  # if the position = 0, change the next node inserted to be 'first' actual node
                self.head = new_node  # now the 'first' node becomes the new node
                return

            current = self.head
            index = 0

            while (
                current and index < position - 1
            ):  # this while loop moves the 'current' node forward by 1
                current = current.next
                index += 1

            if current:  # this code makes the inserted node point what was there before
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

    def draw_linked_list(
        linked_list, custom_value, custom_position, highlight_index=None
    ):
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
            (0, 0, 0),  # black colour
        )
        screen.blit(info, (20, 20))

        controls = FONT.render(
            "Up/Down = Value    Left/Right = Position   A = Insert  D = Delete  R = Reverse \n\n Press ESC to go Back",
            True,
            (0, 0, 0),
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

                    if event.key == pygame.K_UP:  # chaneges the insert value up by 5
                        custom_value += 5

                    elif (
                        event.key == pygame.K_DOWN
                    ):  # chaneges the insert value down by 5
                        custom_value -= 5

                    elif (
                        event.key == pygame.K_RIGHT
                    ):  # pressing right changes the position by 1
                        custom_position += 1

                    elif (
                        event.key == pygame.K_LEFT
                    ):  # pressing left changes the position by 1
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
