import unittest
from doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    # ---------- Insert ----------

    def test_insert_beginning(self):
        dll = DoublyLinkedList()
        dll.insert_beginning(10)
        dll.insert_beginning(20)

        self.assertEqual(dll.to_list_forward(), [20, 10])
        self.assertEqual(dll.to_list_backward(), [10, 20])

    def test_insert_end(self):
        dll = DoublyLinkedList()
        dll.insert_end(10)
        dll.insert_end(20)
        dll.insert_end(30)

        self.assertEqual(dll.to_list_forward(), [10, 20, 30])
        self.assertEqual(dll.to_list_backward(), [30, 20, 10])

    def test_insert_position_beginning(self):
        dll = DoublyLinkedList()
        dll.insert_end(20)
        dll.insert_position(0, 10)

        self.assertEqual(dll.to_list_forward(), [10, 20])

    def test_insert_position_middle(self):
        dll = DoublyLinkedList()
        dll.insert_end(10)
        dll.insert_end(30)

        dll.insert_position(1, 20)

        self.assertEqual(dll.to_list_forward(), [10, 20, 30])

    def test_insert_position_end(self):
        dll = DoublyLinkedList()
        dll.insert_end(10)
        dll.insert_end(20)

        dll.insert_position(2, 30)

        self.assertEqual(dll.to_list_forward(), [10, 20, 30])

    def test_insert_invalid_position(self):
        dll = DoublyLinkedList()
        dll.insert_end(10)

        dll.insert_position(5, 50)

        self.assertEqual(dll.to_list_forward(), [10])

    # ---------- Delete ----------

    def test_delete_beginning_empty(self):
        dll = DoublyLinkedList()

        dll.delete_beginning()

        self.assertEqual(dll.to_list_forward(), [])

    def test_delete_beginning(self):
        dll = DoublyLinkedList()

        dll.insert_end(10)
        dll.insert_end(20)

        dll.delete_beginning()

        self.assertEqual(dll.to_list_forward(), [20])

    def test_delete_end_empty(self):
        dll = DoublyLinkedList()

        dll.delete_end()

        self.assertEqual(dll.to_list_forward(), [])

    def test_delete_end_single(self):
        dll = DoublyLinkedList()

        dll.insert_end(10)

        dll.delete_end()

        self.assertEqual(dll.to_list_forward(), [])

    def test_delete_end_multiple(self):
        dll = DoublyLinkedList()

        dll.insert_end(10)
        dll.insert_end(20)
        dll.insert_end(30)

        dll.delete_end()

        self.assertEqual(dll.to_list_forward(), [10, 20])

    def test_delete_value_middle(self):
        dll = DoublyLinkedList()

        dll.insert_end(10)
        dll.insert_end(20)
        dll.insert_end(30)

        dll.delete_value(20)

        self.assertEqual(dll.to_list_forward(), [10, 30])
        self.assertEqual(dll.to_list_backward(), [30, 10])

    def test_delete_value_head(self):
        dll = DoublyLinkedList()

        dll.insert_end(10)
        dll.insert_end(20)

        dll.delete_value(10)

        self.assertEqual(dll.to_list_forward(), [20])

    def test_delete_value_not_found(self):
        dll = DoublyLinkedList()

        dll.insert_end(10)
        dll.insert_end(20)

        dll.delete_value(99)

        self.assertEqual(dll.to_list_forward(), [10, 20])

    # ---------- Search ----------

    def test_search_found(self):
        dll = DoublyLinkedList()

        dll.insert_end(10)
        dll.insert_end(20)
        dll.insert_end(30)

        self.assertEqual(dll.search(20), 1)

    def test_search_not_found(self):
        dll = DoublyLinkedList()

        self.assertEqual(dll.search(50), -1)

    # ---------- Length ----------

    def test_length_empty(self):
        dll = DoublyLinkedList()

        self.assertEqual(dll.length(), 0)

    def test_length_multiple(self):
        dll = DoublyLinkedList()

        dll.insert_end(1)
        dll.insert_end(2)
        dll.insert_end(3)

        self.assertEqual(dll.length(), 3)

    # ---------- Traversal ----------

    def test_forward_traversal(self):
        dll = DoublyLinkedList()

        dll.insert_end(1)
        dll.insert_end(2)
        dll.insert_end(3)

        self.assertEqual(dll.to_list_forward(), [1, 2, 3])

    def test_backward_traversal(self):
        dll = DoublyLinkedList()

        dll.insert_end(1)
        dll.insert_end(2)
        dll.insert_end(3)

        self.assertEqual(dll.to_list_backward(), [3, 2, 1])


if __name__ == "__main__":
    unittest.main()