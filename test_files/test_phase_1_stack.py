import unittest
from python_files.Phase1_STACK import Stack


class TestStack(unittest.TestCase):

    def test_push_pop(self):

        stack = Stack()

        # push 3 items

        stack.push(1)
        stack.push(2)
        stack.push(3)

        # pop 2 items

        stack.pop()
        stack.pop()

        self.assertEqual(stack.size(), 1)


if __name__ == "__main__":
    unittest.main()
