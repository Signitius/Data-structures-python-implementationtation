import unittest
from binary_search_tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()

    def populate_tree(self):
        for value in [50, 30, 70, 20, 40, 60, 80]:
            self.bst.insert(value)

    # ---------- Constructor ----------

    def test_new_tree_is_empty(self):
        self.assertIsNone(self.bst.root)

    # ---------- Insert ----------

    def test_insert_single_value(self):
        self.bst.insert(10)

        self.assertIsNotNone(self.bst.root)
        self.assertEqual(self.bst.root.value, 10)

    def test_insert_multiple_values(self):
        self.populate_tree()

        self.assertEqual(
            self.bst.inorder(),
            [20, 30, 40, 50, 60, 70, 80]
        )

    def test_insert_duplicate_value(self):
        self.populate_tree()
        self.bst.insert(30)

        self.assertEqual(
            self.bst.inorder(),
            [20, 30, 40, 50, 60, 70, 80]
        )

    # ---------- Search ----------

    def test_search_existing_value(self):
        self.populate_tree()

        self.assertTrue(self.bst.search(60))

    def test_search_nonexistent_value(self):
        self.populate_tree()

        self.assertFalse(self.bst.search(100))

    def test_search_empty_tree(self):
        self.assertFalse(self.bst.search(10))

    # ---------- Traversals ----------

    def test_inorder_empty_tree(self):
        self.assertEqual(self.bst.inorder(), [])

    def test_inorder_traversal(self):
        self.populate_tree()

        self.assertEqual(
            self.bst.inorder(),
            [20, 30, 40, 50, 60, 70, 80]
        )

    def test_preorder_traversal(self):
        self.populate_tree()

        self.assertEqual(
            self.bst.preorder(),
            [50, 30, 20, 40, 70, 60, 80]
        )

    def test_postorder_traversal(self):
        self.populate_tree()

        self.assertEqual(
            self.bst.postorder(),
            [20, 40, 30, 60, 80, 70, 50]
        )

    # ---------- Find Min / Max ----------

    def test_find_min(self):
        self.populate_tree()

        self.assertEqual(self.bst.find_min(), 20)

    def test_find_max(self):
        self.populate_tree()

        self.assertEqual(self.bst.find_max(), 80)

    def test_find_min_empty_tree(self):
        self.assertIsNone(self.bst.find_min())

    def test_find_max_empty_tree(self):
        self.assertIsNone(self.bst.find_max())

    # ---------- Delete ----------

    def test_delete_leaf_node(self):
        self.populate_tree()

        self.bst.delete(20)

        self.assertEqual(
            self.bst.inorder(),
            [30, 40, 50, 60, 70, 80]
        )

    def test_delete_node_with_left_child(self):
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(20)

        self.bst.delete(30)

        self.assertEqual(
            self.bst.inorder(),
            [20, 50]
        )

    def test_delete_node_with_right_child(self):
        self.bst.insert(50)
        self.bst.insert(70)
        self.bst.insert(80)

        self.bst.delete(70)

        self.assertEqual(
            self.bst.inorder(),
            [50, 80]
        )

    def test_delete_node_with_two_children(self):
        self.populate_tree()

        self.bst.delete(70)

        self.assertEqual(
            self.bst.inorder(),
            [20, 30, 40, 50, 60, 80]
        )

    def test_delete_root_only_node(self):
        self.bst.insert(50)

        self.bst.delete(50)

        self.assertIsNone(self.bst.root)

    def test_delete_root_with_one_child(self):
        self.bst.insert(50)
        self.bst.insert(30)

        self.bst.delete(50)

        self.assertEqual(self.bst.root.value, 30)

    def test_delete_root_with_two_children(self):
        self.populate_tree()

        self.bst.delete(50)

        self.assertEqual(
            self.bst.inorder(),
            [20, 30, 40, 60, 70, 80]
        )

    def test_delete_nonexistent_value(self):
        self.populate_tree()

        self.bst.delete(100)

        self.assertEqual(
            self.bst.inorder(),
            [20, 30, 40, 50, 60, 70, 80]
        )

    def test_delete_from_empty_tree(self):
        self.bst.delete(10)

        self.assertIsNone(self.bst.root)


if __name__ == "__main__":
    unittest.main()