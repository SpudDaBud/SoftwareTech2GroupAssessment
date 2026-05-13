import unittest
from python_files.phaseTwoPartThree_VSA import bubble_sort_visualize
import pygame
pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()
ARRAY_SIZE = 30

class TestBS(unittest.TestCase):

    def test_insert_at_position(self):

        testArray = [5,3,8,1,2]
        #test array is unsorted, should be sorted after bubble sort
        bs = bubble_sort_visualize(testArray)
        #test array should be sorted after bubble sort
        self.assertEqual(testArray, [1,2,3,5,8])
        #this should be true as the array is sorted


if __name__ == "__main__":
    unittest.main()
