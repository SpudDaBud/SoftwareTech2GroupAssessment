import unittest
from python_files.Phase1_BST import BST


class TestBST(unittest.TestCase):

    def test_insert_at_position(self):

        bst = BST()

        # insert values

        bst.insert(50)
        bst.insert(30)
        bst.insert(70)

        result = bst.inorder()

        result_values = [node.value for node in result]

        self.assertEqual(result_values, [30, 50, 70])


if __name__ == "__main__":
    unittest.main()
