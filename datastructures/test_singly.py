import unittest
from singly import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    # ---------- Insert ----------

    def test_insert_beginning_empty(self):
        sll = SinglyLinkedList()
        sll.insert_beginning(10)
        self.assertEqual(sll.to_list(), [10])

    def test_insert_beginning_multiple(self):
        sll = SinglyLinkedList()
        sll.insert_beginning(10)
        sll.insert_beginning(20)
        sll.insert_beginning(30)
        self.assertEqual(sll.to_list(), [30, 20, 10])

    def test_insert_end_empty(self):
        sll = SinglyLinkedList()
        sll.insert_end(10)
        self.assertEqual(sll.to_list(), [10])

    def test_insert_end_multiple(self):
        sll = SinglyLinkedList()
        sll.insert_end(10)
        sll.insert_end(20)
        sll.insert_end(30)
        self.assertEqual(sll.to_list(), [10, 20, 30])

    def test_insert_position_beginning(self):
        sll = SinglyLinkedList()
        sll.insert_end(20)
        sll.insert_position(0, 10)
        self.assertEqual(sll.to_list(), [10, 20])

    def test_insert_position_middle(self):
        sll = SinglyLinkedList()
        sll.insert_end(10)
        sll.insert_end(30)
        sll.insert_position(1, 20)
        self.assertEqual(sll.to_list(), [10, 20, 30])

    def test_insert_position_end(self):
        sll = SinglyLinkedList()
        sll.insert_end(10)
        sll.insert_end(20)
        sll.insert_position(2, 30)
        self.assertEqual(sll.to_list(), [10, 20, 30])

    def test_insert_position_invalid(self):
        sll = SinglyLinkedList()
        sll.insert_end(10)
        sll.insert_position(5, 50)
        self.assertEqual(sll.to_list(), [10])

    # ---------- Delete ----------

    def test_delete_beginning_empty(self):
        sll = SinglyLinkedList()
        sll.delete_beginning()
        self.assertEqual(sll.to_list(), [])

    def test_delete_beginning(self):
        sll = SinglyLinkedList()
        sll.insert_end(10)
        sll.insert_end(20)
        sll.delete_beginning()
        self.assertEqual(sll.to_list(), [20])

    def test_delete_end_empty(self):
        sll = SinglyLinkedList()
        sll.delete_end()
        self.assertEqual(sll.to_list(), [])

    def test_delete_end_single(self):
        sll = SinglyLinkedList()
        sll.insert_end(10)
        sll.delete_end()
        self.assertEqual(sll.to_list(), [])

    def test_delete_end_multiple(self):
        sll = SinglyLinkedList()
        sll.insert_end(10)
        sll.insert_end(20)
        sll.insert_end(30)
        sll.delete_end()
        self.assertEqual(sll.to_list(), [10, 20])

    def test_delete_value_middle(self):
        sll = SinglyLinkedList()
        sll.insert_end(10)
        sll.insert_end(20)
        sll.insert_end(30)
        sll.delete_value(20)
        self.assertEqual(sll.to_list(), [10, 30])

    def test_delete_value_head(self):
        sll = SinglyLinkedList()
        sll.insert_end(10)
        sll.insert_end(20)
        sll.delete_value(10)
        self.assertEqual(sll.to_list(), [20])

    def test_delete_value_not_found(self):
        sll = SinglyLinkedList()
        sll.insert_end(10)
        sll.insert_end(20)
        sll.delete_value(100)
        self.assertEqual(sll.to_list(), [10, 20])

    # ---------- Search ----------

    def test_search_found(self):
        sll = SinglyLinkedList()
        sll.insert_end(10)
        sll.insert_end(20)
        sll.insert_end(30)
        self.assertEqual(sll.search(20), 1)

    def test_search_not_found(self):
        sll = SinglyLinkedList()
        self.assertEqual(sll.search(100), -1)

    # ---------- Length ----------

    def test_length_empty(self):
        sll = SinglyLinkedList()
        self.assertEqual(sll.length(), 0)

    def test_length_multiple(self):
        sll = SinglyLinkedList()
        sll.insert_end(1)
        sll.insert_end(2)
        sll.insert_end(3)
        self.assertEqual(sll.length(), 3)

    # ---------- Reverse ----------

    def test_reverse_empty(self):
        sll = SinglyLinkedList()
        sll.reverse()
        self.assertEqual(sll.to_list(), [])

    def test_reverse_single(self):
        sll = SinglyLinkedList()
        sll.insert_end(10)
        sll.reverse()
        self.assertEqual(sll.to_list(), [10])

    def test_reverse_multiple(self):
        sll = SinglyLinkedList()
        sll.insert_end(1)
        sll.insert_end(2)
        sll.insert_end(3)
        sll.reverse()
        self.assertEqual(sll.to_list(), [3, 2, 1])


if __name__ == "__main__":
    unittest.main()