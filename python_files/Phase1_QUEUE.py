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


class Queue:
    def __init__(self):
        self._data = []

    def push(self, val):
        self._data.append(val)

    def pop(self):
        if not self.is_empty():
            return self._data.pop(0)
        raise IndexError("pop from empty queue")

    def peek(self):
        if not self.is_empty():
            return self._data[0]
        raise IndexError("peek from empty queue")

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):
        return f"Queue({self._data})"


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
                if enqueue_button.collidepoint(event.pos):  # MOUSE BTN FOR PUSH
                    queue.push(counter)
                    counter += 1

                elif (
                    dequeue_button.collidepoint(event.pos) and not queue.is_empty()
                ):  # MOUSE BTN FOR POP
                    queue.pop()

                elif back_button.collidepoint(event.pos):
                    running = False

        screen.fill((50, 50, 50))

        # draw enqueue button
        pygame.draw.rect(screen, (0, 180, 0), enqueue_button)
        enqueue_txt = font.render("Enqueue", True, (255, 255, 255))
        screen.blit(
            enqueue_txt,
            (
                enqueue_button.centerx - enqueue_txt.get_width() // 2,
                enqueue_button.centery - enqueue_txt.get_height() // 2,
            ),
        )

        # draw dequeue button
        pygame.draw.rect(screen, (0, 180, 0), dequeue_button)
        dequeue_txt = font.render("Dequeue", True, (255, 255, 255))
        screen.blit(
            dequeue_txt,
            (
                dequeue_button.centerx - dequeue_txt.get_width() // 2,
                dequeue_button.centery - dequeue_txt.get_height() // 2,
            ),
        )

        # back button
        pygame.draw.rect(screen, (0, 180, 0), back_button)
        back_txt = font.render("Back", True, (255, 255, 255))
        screen.blit(
            back_txt,
            (
                back_button.centerx - back_txt.get_width() // 2,
                back_button.centery - back_txt.get_height() // 2,
            ),
        )

        for i, val in enumerate(queue._data):
            rect = pygame.Rect(
                START_X, BASE_Y - i * (BLOCK_HEIGHT + 5), BLOCK_WIDTH, BLOCK_HEIGHT
            )
            pygame.draw.rect(screen, (100, 150, 250), rect)

            text = font.render(str(val), True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)
