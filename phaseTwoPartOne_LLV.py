import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 900, 260
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()
NODE_RADIUS = 25

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

    def insert(self, value, position):
        new_node = Node(value)
        if not self.head or position <= 0:
            new_node.next = self.head
            self.head = new_node
            return 0
        current = self.head
        idx = 0
        while current.next and idx < position - 1:
            current = current.next
            idx += 1
        new_node.next = current.next
        current.next = new_node
        return idx + 1

    def delete(self, value):
        current = self.head
        prev = None
        idx = 0
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return idx
            prev = current
            current = current.next
            idx += 1
        return -1

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def to_list(self):
        elems = []
        current = self.head
        while current:
            elems.append(current.value)
            current = current.next
        return elems

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


def draw_text(text, x, y, color=(0, 0, 0)):
    rendered = FONT.render(text, True, color)
    screen.blit(rendered, (x, y))


def draw_node(x, y, value, highlight=False):
    color = (255, 150, 120) if highlight else (100, 200, 250)
    pygame.draw.circle(screen, color, (int(x), int(y)), NODE_RADIUS)
    text = FONT.render(str(value), True, (0, 0, 0))
    text_rect = text.get_rect(center=(int(x), int(y)))
    screen.blit(text, text_rect)


def draw_arrow(start_pos, end_pos):
    start = (int(start_pos[0]), int(start_pos[1]))
    end = (int(end_pos[0]), int(end_pos[1]))
    pygame.draw.line(screen, (0, 0, 0), start, end, 3)
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    length = max(1, (dx * dx + dy * dy) ** 0.5)
    ux = dx / length
    uy = dy / length
    left = (end[0] - 10 * ux + 5 * uy, end[1] - 10 * uy - 5 * ux)
    right = (end[0] - 10 * ux - 5 * uy, end[1] - 10 * uy + 5 * ux)
    pygame.draw.polygon(screen, (0, 0, 0), [left, end, right])


def draw_linked_list(linked_list, highlight_index=None):
    screen.fill((240, 240, 240))
    nodes = []
    current = linked_list.head
    x, y = 200, 180
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


def animate_transition(values, start_positions, end_positions, steps=20):
    for step in range(1, steps + 1):
        t = step / steps
        screen.fill((240, 240, 240))
        interp = []
        for (x0, y0), (x1, y1), val in zip(start_positions, end_positions, values):
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            interp.append((x, y, val))
        for i, (x, y, val) in enumerate(interp):
            draw_node(x, y, val)
            if i < len(interp) - 1:
                next_x, next_y = interp[i + 1][0], interp[i + 1][1]
                draw_arrow((x + NODE_RADIUS, y), (next_x - NODE_RADIUS, next_y))
        pygame.display.flip()
        clock.tick(60)


def animate_reverse(linked_list):
    values = linked_list.to_list()
    if len(values) <= 1:
        return
    start_positions = [(200 + i * 150, 180) for i in range(len(values))]
    end_positions = list(reversed(start_positions))
    animate_transition(values, start_positions, end_positions)
    linked_list.reverse()
    draw_linked_list(linked_list)
    pygame.time.wait(300)


def main():
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    ll.append(15)

    mode = None
    input_text = ''
    prompt_text = ''
    status_text = 'Ready'
    insert_value = None
    last_highlight = None

    running = True
    while running:
        draw_linked_list(ll, highlight_index=last_highlight)
        draw_text('Commands: I=Insert, D=Delete, R=Reverse, Q=Quit', 10, 10)
        draw_text('Insert: enter value then position (0-based).', 10, 40)
        draw_text('Delete: enter a value to remove.', 10, 70)
        if mode:
            draw_text(f'{prompt_text} {input_text}', 10, 100, (50, 50, 150))
        draw_text(status_text, 10, 130, (50, 120, 50))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if mode is None:
                    if event.key == pygame.K_i:
                        mode = 'insert_value'
                        input_text = ''
                        prompt_text = 'Insert value:'
                        status_text = 'Type the node value and press Enter.'
                    elif event.key == pygame.K_d:
                        mode = 'delete'
                        input_text = ''
                        prompt_text = 'Delete value:'
                        status_text = 'Type the node value and press Enter.'
                    elif event.key == pygame.K_r:
                        animate_reverse(ll)
                        status_text = 'Reversed the list.'
                        last_highlight = None
                    elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                        running = False
                else:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        if mode == 'insert_value':
                            try:
                                insert_value = int(input_text)
                                mode = 'insert_pos'
                                input_text = ''
                                prompt_text = 'Insert position:'
                                status_text = 'Enter insertion position (0-based).'
                            except ValueError:
                                status_text = 'Invalid value. Please type digits only.'
                                mode = None
                                input_text = ''
                        elif mode == 'insert_pos':
                            try:
                                position = int(input_text)
                                inserted_index = ll.insert(insert_value, position)
                                status_text = f'Inserted {insert_value} at position {inserted_index}.'
                                last_highlight = inserted_index
                            except ValueError:
                                status_text = 'Invalid position. Enter an integer.'
                            mode = None
                            input_text = ''
                        elif mode == 'delete':
                            try:
                                delete_value = int(input_text)
                                deleted_index = ll.delete(delete_value)
                                if deleted_index >= 0:
                                    status_text = f'Deleted {delete_value} from position {deleted_index}.'
                                    last_highlight = min(deleted_index, len(ll) - 1) if len(ll) > 0 else None
                                else:
                                    status_text = f'Value {delete_value} not found.'
                                    last_highlight = None
                            except ValueError:
                                status_text = 'Invalid delete value. Enter digits only.'
                            mode = None
                            input_text = ''
                    else:
                        if event.unicode.isdigit() or (event.unicode == '-' and input_text == ''):
                            input_text += event.unicode
        clock.tick(60)

    pygame.quit()

def run_linked_list():
    main()

if __name__ == "__main__":
    run_linked_list()
