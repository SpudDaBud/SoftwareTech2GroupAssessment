import unittest
from python_files.Phase1_QUEUE import Queue


class TestQueue(unittest.TestCase):

    def test_enqueue_dequeue(self):

        queue = Queue()

        # enqueue 4 items

        queue.push(1)
        queue.push(2)
        queue.push(3)
        queue.push(4)

        # dequeue 3 items

        queue.pop()
        queue.pop()
        queue.pop()

        # queue should have 1 item left: [4]

        self.assertEqual(queue.size(), 1)


if __name__ == "__main__":
    unittest.main()
