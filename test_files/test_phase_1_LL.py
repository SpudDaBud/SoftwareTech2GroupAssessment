import unittest
from python_files.Phase1_LL import LinkedList


class TestLL(unittest.TestCase):

    def test_insert_at_position(self):

        ll = LinkedList()

        # build inital list

        ll.append(1)
        ll.append(2)
        ll.append(3)

        # insert 10 at pos 2

        ll.insert_at_position(10, 2)

        # 10 shoudl be inseted at pos 2

        self.assertEqual(ll.to_list(), [1, 2, 10, 3])


if __name__ == "__main__":
    unittest.main()
