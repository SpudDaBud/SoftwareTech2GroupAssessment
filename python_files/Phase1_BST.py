import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 600
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
    
    def search(self, root, target, path_list):
        
        if root is None:
            return []
        
        if root.value == target:
            path_list.append(root)
            return path_list
 
        elif target < root.value:
            path_list.append(root)
            return self.search(root.left, target, path_list)
            

        else:
            path_list.append(root)
            return self.search(root.right, target, path_list)
    
    def delete(self, root, key):

        if root is None:
            return 
        
        if root.value > key:
            root.left = self.delete(root.left, key)
        
        elif root.value < key:
            root.right = self.delete(root.right, key)
        
        else: 

            #1st case: No Children
            if not root.right and not root.left:
                return None
            
            #2nd case: One Child
            
            if not root.right and root.left:
                return root.left
            
            if root.right and not root.left:
                return root.right
            
            #3rd case: Both Chrildren

            successor = root.right

            while successor.left:
                successor = successor.left

            root.value = successor.value

            root.right = self.delete(root.right, successor.value)

        return root

            


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


def draw_node(x, y, value, highlight=False):
    color = (255, 150, 150) if highlight else (100, 200, 250)
    pygame.draw.circle(screen, color, (x, y), NODE_RADIUS)
    text = FONT.render(str(value), True, (0, 0, 0))
    text_rect = text.get_rect(center=(x, y))

    screen.blit(text, text_rect)




def draw_edge(start_pos, end_pos):
    pygame.draw.line(screen, (0, 0, 0), start_pos, end_pos, 3)


def draw_tree(node, x, y, x_offset, nodes_pos, parent_pos=None):
    if node:
        nodes_pos[node] = (x, y)
        if parent_pos:
            draw_edge(parent_pos, (x, y))

        # Draw left subtree
        draw_tree(node.left, x - x_offset, y + 80, x_offset // 2, nodes_pos, (x, y))

        # Draw Right subtree
        draw_tree(node.right, x + x_offset, y + 80, x_offset // 2, nodes_pos, (x, y))
        draw_node(x, y, node.value)

        


def bst_visulaisation(font):
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)
    
    back_button = pygame.Rect(10, 500, 150, 50)

    running = True
    highlight_idx = 0
    traversal_nodes = []
    mode_selected = False
    

    traversal_timer = 0
    traversal_delay = 700

    current_mode = False

    search_found = ""
    user_txt = ""
    
    



    while running:
        screen.fill((240, 240, 240))

        pygame.draw.rect(screen, (0, 180, 0), back_button)
        back_txt = font.render("Back To Menu", True, (255, 255, 255))
        screen.blit(back_txt,(back_button.centerx - back_txt.get_width() // 2, back_button.centery - back_txt.get_height() // 2))

        controls = FONT.render("P = Preorder   I = Inorder  O = Postorder  L = Insert  D = Delete  S = Search", True, (0, 0, 0))
        screen.blit(controls, (20, 50))

        controls2 = FONT.render("Press ESC to exit current mode", True, (0, 0, 0))
        screen.blit(controls2, (20, 80))

        if current_mode == "search":
            search_text1 = FONT.render("Search Mode is ACTIVE!", True, (0, 0, 0))
            search_text2 = FONT.render("Press BACKSPACE to delete text", True, (250, 0, 0))
            search_text3 = FONT.render("Press ENTER when ready", True, (50, 153, 50))
            search_text4 = FONT.render("Search: " + user_txt, True, (0, 0, 0))                       
            screen.blit(search_text1, (20, 130))
            screen.blit(search_text2, (20, 180))
            screen.blit(search_text3, (20, 230))
            screen.blit(search_text4, (20, 280))
        
        if current_mode == "delete":
            del_text1 = FONT.render("Delete Mode is ACTIVE!", True, (0, 0, 0))
            del_text2 = FONT.render("Press BACKSPACE to delete text", True, (250, 0, 0))
            del_text3 = FONT.render("Press ENTER when ready", True, (50, 153, 50))
            del_text4 = FONT.render("Delete: " + user_txt, True, (0, 0, 0))                       
            screen.blit(del_text1, (20, 130))
            screen.blit(del_text2, (20, 180))
            screen.blit(del_text3, (20, 230))
            screen.blit(del_text4, (20, 280))
        
        if current_mode == "insert":
            ins_text1 = FONT.render("Insert Mode is ACTIVE!", True, (0, 0, 0))
            ins_text2 = FONT.render("Press BACKSPACE to delete text", True, (250, 0, 0))
            ins_text3 = FONT.render("Press ENTER when ready", True, (50, 153, 50))
            ins_text4 = FONT.render("Insert: " + user_txt, True, (0, 0, 0))                       
            screen.blit(ins_text1, (20, 130))
            screen.blit(ins_text2, (20, 180))
            screen.blit(ins_text3, (20, 230))
            screen.blit(ins_text4, (20, 280))
        
        if current_mode == "pre":
            pre_text = FONT.render("Currently showing Preorder: ", True, (50, 153, 50))                
            screen.blit(pre_text, (20, 100))
        
        if current_mode == "post":
            post_text = FONT.render("Currently showing Postorder: ", True, (50, 153, 50))                
            screen.blit(post_text, (20, 100))
        
        if current_mode == "inor":
            inor_text = FONT.render("Currently showing Inorder: ", True, (50, 153, 50))                
            screen.blit(inor_text, (20, 100))
        
        if search_found == "no":
            no_search = FONT.render("Node " + user_txt + " Not Found", True, (250, 0, 0))
            screen.blit(no_search, (20, 330))

        if search_found == "yes":
            no_search = FONT.render("Node " + user_txt + " Found!", True, (50, 153, 50))
            screen.blit(no_search, (20, 330))
            


        
        nodes_pos = {}

        draw_tree(bst.root, WIDTH // 2, 200, 150, nodes_pos)
        # Highlight current node in in-order traversal
        if highlight_idx < len(traversal_nodes):
            node = traversal_nodes[highlight_idx]
            x, y = WIDTH // 2, 50

            # We need to find node position (roughly)
            # For simplicity, redraw tree and highlight the node:

            

            def store_positions(node, x, y, x_offset, parent_pos=None):
                if node:
                    nodes_pos[node] = (x, y)
                    store_positions(
                        node.left, x - x_offset, y + 80, x_offset // 2, (x, y)
                    )
                    store_positions(
                        node.right, x + x_offset, y + 80, x_offset // 2, (x, y)
                    )

            store_positions(bst.root, WIDTH // 2, 200, 150)
            if node in nodes_pos:
                draw_node(*nodes_pos[node], node.value, highlight=True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    current_mode = False
                    user_txt = ""
                    search_found = ""

                if current_mode == "search":

                    if event.key == pygame.K_RETURN:
                        if user_txt != "": # only continue if the text box is not empty 
                            target = int(user_txt)
                            traversal_nodes = bst.search(bst.root, target, [])
                            highlight_idx = 0
                            mode_selected = True
                            traversal_timer = pygame.time.get_ticks()

                            if traversal_nodes and traversal_nodes[-1].value == target:
                                search_found = "yes"
                            else:
                                search_found = "no"

                            
                            
                    elif event.key == pygame.K_BACKSPACE:
                        user_txt = user_txt[:-1]

                    else:
                        user_txt += event.unicode
                
                elif current_mode == "delete":

                    if event.key == pygame.K_RETURN:
                        if user_txt != "": # only continue if the text box is not empty 
                            target = int(user_txt)
                            bst.root = bst.delete(bst.root, target)
                            highlight_idx = 0
                            mode_selected = True
                            traversal_timer = pygame.time.get_ticks()

                    elif event.key == pygame.K_BACKSPACE:
                        user_txt = user_txt[:-1]

                    else:
                        user_txt += event.unicode

                elif current_mode == "insert":
                    if event.key == pygame.K_RETURN:
                        if user_txt != "": # only continue if the text box is not empty 
                            target = int(user_txt)
                            bst.insert(target)
                            highlight_idx = 0
                            mode_selected = True
                            traversal_timer = pygame.time.get_ticks()
                            
                    elif event.key == pygame.K_BACKSPACE:
                        user_txt = user_txt[:-1]

                    else:
                        user_txt += event.unicode
                        
                else:

                    if event.key == pygame.K_i:
                        traversal_nodes = bst.inorder()
                        highlight_idx = 0
                        mode_selected = True
                        current_mode = "inor"
                        traversal_timer = pygame.time.get_ticks()
                
                    elif event.key == pygame.K_p:
                        traversal_nodes = bst.preorder()
                        highlight_idx = 0 
                        mode_selected = True
                        current_mode = "pre"
                        traversal_timer = pygame.time.get_ticks()
                
                    elif event.key == pygame.K_o:
                        traversal_nodes = bst.postorder()
                        highlight_idx = 0
                        mode_selected = True
                        current_mode = "post"
                        traversal_timer = pygame.time.get_ticks()
                    
                    elif event.key == pygame.K_s:
                        current_mode = "search"
                    
                    elif event.key == pygame.K_d:
                        current_mode = "delete"
                    
                    elif event.key == pygame.K_l:
                        current_mode = "insert"
                    
                        


        pygame.display.flip()
        clock.tick(60) 

        if mode_selected and traversal_nodes:

            current_time = pygame.time.get_ticks()

            if current_time - traversal_timer > traversal_delay:

                traversal_timer = current_time

            
                if highlight_idx < len(traversal_nodes) - 1:            
                    highlight_idx += 1
                else:
                    mode_selected = False

    


    
