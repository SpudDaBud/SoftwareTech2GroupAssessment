import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()
NODE_RADIUS = 20

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if not node:
                return BSTNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            return node
        self.root = _insert(self.root, value)

    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node)
                _inorder(node.right)
        _inorder(self.root)
        return result

    def preorder(self):
        result = []
        def _preorder(node):
            if node:
                result.append(node)
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        return result

    def postorder(self):
        result = []
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node)
        _postorder(self.root)
        return result

    def search_path(self, value):
        path = []
        def _search(node):
            if not node:
                return False
            path.append(node)
            if value == node.value:
                return True
            elif value < node.value:
                return _search(node.left)
            else:
                return _search(node.right)
        _search(self.root)
        return path if path and path[-1].value == value else []

    def delete(self, value):
        def _delete(node, value):
            if not node:
                return node
            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                # Two children
                temp = self._min_value_node(node.right)
                node.value = temp.value
                node.right = _delete(node.right, temp.value)
            return node
        self.root = _delete(self.root, value)

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    

def draw_node(x, y, value, highlight=False):
    color = (255, 150, 150) if highlight else (100, 200, 250)
    pygame.draw.circle(screen, color, (x, y), NODE_RADIUS)
    text = FONT.render(str(value), True, (0, 0, 0))
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

def draw_edge(start_pos, end_pos):
    pygame.draw.line(screen, (0, 0, 0), start_pos, end_pos, 3)

def draw_text(text, x, y, color=(0, 0, 0)):
    rendered = FONT.render(text, True, color)
    screen.blit(rendered, (x, y))

def draw_tree(node, x, y, x_offset, nodes_pos, highlight_nodes=None, highlight_node=None, parent_pos=None):
    if highlight_nodes is None:
        highlight_nodes = []
    if node:
        nodes_pos[node] = (x, y)
        if parent_pos:
            draw_edge(parent_pos, (x, y))
        # Draw left subtree
        draw_tree(node.left, x - x_offset, y + 80, x_offset // 2, nodes_pos, highlight_nodes, highlight_node, (x, y))
        # Draw right subtree
        draw_tree(node.right, x + x_offset, y + 80, x_offset // 2, nodes_pos, highlight_nodes, highlight_node, (x, y))
        highlight = node in highlight_nodes or node == highlight_node
        draw_node(x, y, node.value, highlight)

def main():
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)
    running = True
    mode = 'inorder'
    traversal_idx = 0
    traversal_active = False
    traversal_delay = 0
    search_value = None
    delete_value = None
    input_text = ''
    prompt_text = ''
    status_text = 'Ready'
    path = []
    search_timer = 0
    nodes = bst.inorder()
    while running:
        screen.fill((240, 240, 240))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    mode = 'inorder'
                    traversal_idx = 0
                    traversal_active = True
                    traversal_delay = 1
                    status_text = 'Inorder traversal'
                elif event.key == pygame.K_p:
                    mode = 'preorder'
                    traversal_idx = 0
                    traversal_active = True
                    traversal_delay = 1
                    status_text = 'Preorder traversal'
                elif event.key == pygame.K_o:
                    mode = 'postorder'
                    traversal_idx = 0
                    traversal_active = True
                    traversal_delay = 1
                    status_text = 'Postorder traversal'
                elif event.key == pygame.K_s:
                    mode = 'search'
                    input_text = ''
                    prompt_text = 'Search value:'
                    status_text = 'Enter value to search'
                    search_value = None
                    path = []
                    search_timer = 0
                elif mode in ['search', 'delete']:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        try:
                            val = int(input_text)
                            if mode == 'search':
                                search_value = val
                                path = bst.search_path(val)
                                if path:
                                    status_text = f'Found {val}, path highlighted'
                                    search_timer = 5  # Show for 5 seconds
                                else:
                                    status_text = f'{val} not found'
                                    search_timer = 2  # Show message for 2 seconds
                            elif mode == 'delete':
                                bst.delete(val)
                                status_text = f'Deleted {val}'
                                mode = 'inorder'
                                traversal_idx = 0
                                traversal_active = True
                        except ValueError:
                            status_text = 'Invalid input'
                        input_text = ''
                    else:
                        if event.unicode.isdigit() or (event.unicode == '-' and not input_text):
                            input_text += event.unicode
        if mode == 'inorder':
            nodes = bst.inorder()
        elif mode == 'preorder':
            nodes = bst.preorder()
        elif mode == 'postorder':
            nodes = bst.postorder()
        else:
            nodes = []
        highlight_node = None
        highlight_nodes = []
        if mode in ['inorder', 'preorder', 'postorder'] and traversal_active:
            if traversal_idx < len(nodes):
                highlight_node = nodes[traversal_idx]
        elif mode == 'search' and search_timer > 0:
            highlight_nodes = path
        nodes_pos = {}
        draw_tree(bst.root, WIDTH // 2, 50, 150, nodes_pos, highlight_nodes, highlight_node)
        draw_text('Modes: I=Inorder, P=Preorder, O=Postorder, S=Search, D=Delete', 10, 10)
        if mode in ['search', 'delete'] and input_text:
            draw_text(f'{prompt_text} {input_text}', 10, 40, (50, 50, 150))
        draw_text(status_text, 10, 70, (50, 120, 50))
        pygame.display.flip()
        if traversal_delay > 0:
            traversal_delay -= 1
        if mode in ['inorder', 'preorder', 'postorder'] and traversal_active and traversal_delay == 0:
            traversal_idx += 1
            if traversal_idx >= len(nodes):
                traversal_active = False
        if search_timer > 0:
            search_timer -= 1
            if search_timer == 0:
                mode = 'inorder'
                traversal_idx = 0
                traversal_active = False
                traversal_delay = 0
                status_text = 'Ready'
                path = []
        clock.tick(1)
    pygame.quit()

if __name__ == "__main__":
    main()