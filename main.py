"""
This script uses pygame to showcase visualisations of DSA through modular prorgamming 
"""

import pygame
import sys

from python_files.Phase1_STACK import stack_visualization
from python_files.Phase1_QUEUE import queue_visualization
from python_files.Phase1_LL import linked_list_visualization
from python_files.Phase1_BST import bst_visulaisation

from python_files import PhaseThreeLoading, phaseTwoPartThree_VSA

from python_files import PhaseThreeGrid # Pathfinding Puzzle
from python_files import PhaseThreeHeap
from python_files import PhaseThreePath # Dynamic Programming Puzzle
from python_files import phaseThreeGraph # Graph Traversal Visualization



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
    draw_text("Algorithm Explorer", (400, 50))

    buttons = {
        "Data Structures": pygame.Rect(400, 150, 200, 50),
        "Sorting": pygame.Rect(400, 230, 200, 50),
        "Graphs": pygame.Rect(400, 310, 200, 50),
        "Heap": pygame.Rect(400, 390, 200, 50),
        "Puzzles": pygame.Rect(400, 460, 200, 50)
    }

    for text, rect in buttons.items():
        pygame.draw.rect(screen, (150, 150, 200), rect)
        draw_text(text, (rect.x + 20, rect.y + 10))

    pygame.display.flip()
    return buttons

def data_structures_module():
    """
    This module showcases visualisations for a Stack, 
    Queue, Linked List, and a BST
    """
    # completed by u3285413

    # code for running the menu inside data_structures_module:
    font = pygame.font.SysFont(None, 28)

    menu_items = [
        "Stack Visualization (press enter)",
        "Queue Visualization (press enter)",
        "Linked List Visualization (press enter)",
        "BST Visualization (press enter)",
        "Back (press enter)",
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
                    
                    elif choice == "BST Visualization (press enter)":
                        bst_visulaisation(font)

                    elif choice == "Back (press enter)":
                        running = False

        clock.tick(30)


def sorting_module():
    # Bubble sort, selection sort, merge sort visualizations
    phaseTwoPartThree_VSA.main()


def graphs_module():
    # BFS, DFS visualization with interactive graph
    phaseThreeGraph.main()


def heap_module():
    # Heap insertion and extraction visualization
    PhaseThreeHeap.main() 


def puzzles_module():
    PhaseThreeLoading.main()

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
            elif current_module == "Heap":
                heap_module()
            elif current_module == "Graphs":
                graphs_module()
            elif current_module == "Puzzles":
                puzzles_module()
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
         

            current_module = None

        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
