import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

BLOCK_WIDTH, BLOCK_HEIGHT = 200, 40
START_X = (WIDTH - BLOCK_WIDTH) // 2
BASE_Y = HEIGHT - BLOCK_HEIGHT - 100


class Queue:
    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self._data:
            self._data.pop(0)

    def is_empty(self):
        return len(self._data) == 0


def queue_visualization(screen, font):
    queue = Queue()
    counter = 1
    running = True

    enqueue_button = pygame.Rect(50, 500, 150, 50)
    dequeue_button = pygame.Rect(350, 500, 150, 50)
    back_button = pygame.Rect(650, 500, 150, 50)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if enqueue_button.collidepoint(event.pos):
                    queue.push(counter)
                    counter += 1

                elif dequeue_button.collidepoint(event.pos) and not queue.is_empty():
                    queue.pop()

                elif back_button.collidepoint(event.pos):
                    running = False

        screen.fill((50, 50, 50))

        pygame.draw.rect(screen, (0, 180, 0), enqueue_button)
        enqueue_txt = font.render("Enqueue", True, (255, 255, 255))
        screen.blit(enqueue_txt, (enqueue_button.centerx - enqueue_txt.get_width() // 2,
                                  enqueue_button.centery - enqueue_txt.get_height() // 2))

        pygame.draw.rect(screen, (0, 180, 0), dequeue_button)
        dequeue_txt = font.render("Dequeue", True, (255, 255, 255))
        screen.blit(dequeue_txt, (dequeue_button.centerx - dequeue_txt.get_width() // 2,
                                  dequeue_button.centery - dequeue_txt.get_height() // 2))

        pygame.draw.rect(screen, (0, 180, 0), back_button)
        back_txt = font.render("Back", True, (255, 255, 255))
        screen.blit(back_txt, (back_button.centerx - back_txt.get_width() // 2,
                               back_button.centery - back_txt.get_height() // 2))

        for i, val in enumerate(queue._data):
            rect = pygame.Rect(
                START_X,
                BASE_Y - i * (BLOCK_HEIGHT + 5),
                BLOCK_WIDTH,
                BLOCK_HEIGHT,
            )
            pygame.draw.rect(screen, (100, 150, 250), rect)

            text = font.render(str(val), True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)

        if queue._data:
            front_rect = pygame.Rect(
                START_X,
                BASE_Y - (len(queue._data) - 1) * (BLOCK_HEIGHT + 5),
                BLOCK_WIDTH,
                BLOCK_HEIGHT,
            )
            rear_rect = pygame.Rect(
                START_X,
                BASE_Y,
                BLOCK_WIDTH,
                BLOCK_HEIGHT,
            )
            head_text = font.render("Front", True, (255, 255, 255))
            tail_text = font.render("Rear", True, (255, 255, 255))
            screen.blit(head_text, (front_rect.right + 10, front_rect.centery - head_text.get_height() // 2))
            screen.blit(tail_text, (rear_rect.right + 10, rear_rect.centery - tail_text.get_height() // 2))

        pygame.display.flip()
        clock.tick(30)


def run_queue():
    queue_visualization(screen, FONT)


if __name__ == "__main__":
    run_queue()
