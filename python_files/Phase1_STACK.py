"""This program uses pygame to showcase a visualisation of a stack"""

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


class Stack:
    """Simple stack class"""

    def __init__(self):
        self._data = []

    def push(self, val):
        """Add item to top of stack"""
        self._data.append(val)

    def pop(self):
        """remove item from top of stack"""
        if not self.is_empty():
            return self._data.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """Returns the top value without removing it"""
        if not self.is_empty():
            return self._data[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        """checks if the stack is empty"""
        return len(self._data) == 0

    def size(self):
        """gets the size of the stack"""
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data})"


def stack_visualization(screen, font):
    """runs the interactive stack visualisation program using pygame"""

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
                if push_button.collidepoint(event.pos):  # MOUSE BTN FOR PUSH
                    stack.push(counter)
                    counter += 1

                elif (
                    pop_button.collidepoint(event.pos) and not stack.is_empty()
                ):  # MOUSE BTN FOR POP
                    stack.pop()

                elif back_button.collidepoint(event.pos):
                    running = False

        screen.fill((50, 50, 50))

        # draw push button
        pygame.draw.rect(screen, (0, 180, 0), push_button)
        push_txt = font.render("Push", True, (255, 255, 255))
        screen.blit(
            push_txt,
            (
                push_button.centerx - push_txt.get_width() // 2,
                push_button.centery - push_txt.get_height() // 2,
            ),
        )

        # draw pop button
        pygame.draw.rect(screen, (0, 180, 0), pop_button)
        pop_txt = font.render("Pop", True, (255, 255, 255))
        screen.blit(
            pop_txt,
            (
                pop_button.centerx - pop_txt.get_width() // 2,
                pop_button.centery - pop_txt.get_height() // 2,
            ),
        )

        # back button
        pygame.draw.rect(screen, (0, 180, 0), back_button)
        back_txt = font.render("Back", True, (255, 255, 255))
        screen.blit(back_txt,(back_button.centerx - back_txt.get_width() // 2, back_button.centery - back_txt.get_height() // 2))

        for i, val in enumerate(stack._data):
            rect = pygame.Rect(
                START_X, BASE_Y - i * (BLOCK_HEIGHT + 5), BLOCK_WIDTH, BLOCK_HEIGHT
            )
            pygame.draw.rect(screen, (100, 150, 250), rect)

            text = font.render(str(val), True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)
