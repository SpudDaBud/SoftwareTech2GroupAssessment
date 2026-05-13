import pygame
import sys
import collections
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()
# Graph nodes positioned manually
nodes_pos = {
    'A': (100, 100),
    'B': (250, 60),
    'C': (250, 200),
    'D': (400, 50),
    'E': (500, 150),
    'F': (400, 300)
}   

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'E'],
    'D': ['B'],
    'E': ['B', 'F', 'C'],
    'F': ['C', 'E']
}

def draw_graph(visited=set(), frontier=set(), current=None, traversal_order=None):
    screen.fill((240, 240, 240))
    # Draw edges
    for node, neighbors in graph.items():
        x1, y1 = nodes_pos[node]
        for n in neighbors:
            x2, y2 = nodes_pos[n]
            pygame.draw.line(screen, (0, 0, 0), (x1, y1), (x2, y2), 2)
    # Draw nodes
    for node, (x, y) in nodes_pos.items():
        color = (200, 200, 200)
        if node in visited:
            color = (100, 200, 100)
        if node in frontier:
            color = (255, 200, 100)
        if node == current:
            color = (255, 100, 100)
        pygame.draw.circle(screen, color, (x, y), 25)
        text = FONT.render(node, True, (0, 0, 0))
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)
    
    # Draw traversal order text
    if traversal_order is not None:
        order_text = "Traversal Order: " + " -> ".join(traversal_order)
        text = FONT.render(order_text, True, (0, 0, 0))
        screen.blit(text, (10, 10))
    
    pygame.display.flip()

def bfs(start):
    visited = set()
    queue = collections.deque([start])
    traversal_order = []
    while queue:
        current = queue.popleft()
        visited.add(current)
        traversal_order.append(current)
        draw_graph(visited=visited, frontier=set(queue), current=current, traversal_order=traversal_order)
        pygame.time.wait(700)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

def dfs(start):
    visited = set()
    stack = [start]
    traversal_order = []
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            traversal_order.append(current)
            draw_graph(visited=visited, frontier=set(stack), current=current, traversal_order=traversal_order)
            pygame.time.wait(700)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # Add neighbors in reverse order to maintain left-to-right traversal
            for neighbor in reversed(graph[current]):
                if neighbor not in visited:
                    stack.append(neighbor)

def get_clicked_node(pos):
    """Check if a click position is on a node and return the node name."""
    for node, (x, y) in nodes_pos.items():
        distance = ((pos[0] - x)**2 + (pos[1] - y)**2)**0.5
        if distance <= 25:
            return node
    return None

def wait_to_return():
    waiting = True
    while waiting:
        screen.fill((240, 240, 240))
        message = FONT.render("Traversal complete. Press ESC to return to menu.", True, (0, 0, 0))
        screen.blit(message, (80, 20))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False


def main():
    pygame.time.wait(1000)
    
    # Wait for user to choose between BFS and DFS
    algorithm = None
    font_large = pygame.font.SysFont(None, 32)
    bfs_button = pygame.Rect(100, 150, 150, 60)
    dfs_button = pygame.Rect(350, 150, 150, 60)
    draw_graph()
    
    choosing_algorithm = True
    while choosing_algorithm:
        screen.fill((240, 240, 240))
        instruction = font_large.render("Choose an Algorithm", True, (0, 0, 0))
        screen.blit(instruction, (150, 50))
        
        # Draw BFS button
        pygame.draw.rect(screen, (150, 150, 255), bfs_button)
        bfs_text = font_large.render("BFS", True, (0, 0, 0))
        screen.blit(bfs_text, (140, 165))
        
        # Draw DFS button
        pygame.draw.rect(screen, (150, 150, 255), dfs_button)
        dfs_text = font_large.render("DFS", True, (0, 0, 0))
        screen.blit(dfs_text, (390, 165))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if bfs_button.collidepoint(event.pos):
                    algorithm = "bfs"
                    choosing_algorithm = False
                elif dfs_button.collidepoint(event.pos):
                    algorithm = "dfs"
                    choosing_algorithm = False
    
    # Wait for user to click on a node to start traversal
    waiting = True
    selected_node = None
    
    while waiting:
        screen.fill((240, 240, 240))
        instruction = font_large.render("Click on a node to start", True, (0, 0, 0))
        screen.blit(instruction, (80, 20))
        
        # Draw edges
        for node, neighbors in graph.items():
            x1, y1 = nodes_pos[node]
            for n in neighbors:
                x2, y2 = nodes_pos[n]
                pygame.draw.line(screen, (0, 0, 0), (x1, y1), (x2, y2), 2)
        
        # Draw nodes
        for node, (x, y) in nodes_pos.items():
            pygame.draw.circle(screen, (200, 200, 200), (x, y), 25)
            text = FONT.render(node, True, (0, 0, 0))
            text_rect = text.get_rect(center=(x, y))
            screen.blit(text, text_rect)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicked_node = get_clicked_node(event.pos)
                if clicked_node:
                    selected_node = clicked_node
                    waiting = False
    
    # Run selected algorithm from selected node
    if algorithm == "bfs":
        bfs(selected_node)
    else:
        dfs(selected_node)
    
    wait_to_return()


if __name__ == "__main__":
    main()
