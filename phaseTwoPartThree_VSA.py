import pygame
import random
import sys
pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()
ARRAY_SIZE = 30
array = [random.randint(10, 450) for _ in range(ARRAY_SIZE)]
bar_width = WIDTH // ARRAY_SIZE

def draw_array(array, color_positions=None):
    screen.fill((30, 30, 30))
    for i, val in enumerate(array):
        color = (100, 200, 250)
        if color_positions:
            if 'compare' in color_positions and i in color_positions['compare']:
                color = (255, 100, 100)
            if 'swap' in color_positions and i in color_positions['swap']:
                color = (100, 255, 100)
            if 'left' in color_positions and i in color_positions['left']:
                color = (200, 100, 200)  # purple for left subarray
            if 'right' in color_positions and i in color_positions['right']:
                color = (100, 200, 100)  # green for right subarray
            if 'merge' in color_positions and i in color_positions['merge']:
                color = (255, 255, 100)  # yellow for merge position
        pygame.draw.rect(screen, color, (i * bar_width,
                                         HEIGHT - val, bar_width - 2, val))
    pygame.display.flip()


def bubble_sort_visualize(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            draw_array(array, {'compare': [j, j + 1], 'swap': []})
            pygame.time.wait(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            draw_array(array, {'compare': [], 'swap': [j, j + 1]})
            pygame.time.wait(50)
    draw_array(array)

def selection_sort_visualize(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            draw_array(array, {'compare': [min_idx, j], 'swap': []})
            pygame.time.wait(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if array[j] < array[min_idx]:
                min_idx = j
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]
            draw_array(array, {'compare': [], 'swap': [i, min_idx]})
            pygame.time.wait(50)
    draw_array(array)

def merge_sort_visualize(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        # Show split
        draw_array(arr, {'left': list(range(left, mid + 1)), 'right': list(range(mid + 1, right + 1))})
        pygame.time.wait(200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        merge_sort_visualize(arr, left, mid)
        merge_sort_visualize(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        draw_array(arr, {'compare': [left + i, mid + 1 + j], 'merge': [k]})
        pygame.time.wait(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    draw_array(arr)

def main():
    running = True
    algorithm = None
    while running:
        screen.fill((30, 30, 30))
        instructions = FONT.render("Press B for Bubble Sort, S for Selection Sort, M for Merge Sort", True, (255, 255, 255))
        screen.blit(instructions, (50, 50))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    algorithm = 'bubble'
                    running = False
                elif event.key == pygame.K_s:
                    algorithm = 'selection'
                    running = False
                elif event.key == pygame.K_m:
                    algorithm = 'merge'
                    running = False
    if algorithm:
        draw_array(array)
        pygame.time.wait(1000)
        if algorithm == 'bubble':
            bubble_sort_visualize(array)
        elif algorithm == 'selection':
            selection_sort_visualize(array)
        elif algorithm == 'merge':
            merge_sort_visualize(array, 0, len(array) - 1)
        pygame.time.wait(2000)
    pygame.quit()


if __name__ == "__main__":
    main()