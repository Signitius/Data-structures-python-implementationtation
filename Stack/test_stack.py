import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        self.assertEqual(s.size, 0)

    def test_push_and_peek(self):
        s = Stack()
        s.push(10)
        self.assertEqual(s.peek(), 10)
        self.assertEqual(s.size, 1)

        s.push(20)
        self.assertEqual(s.peek(), 20)
        self.assertEqual(s.size, 2)

    def test_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)

        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.size, 0)

    def test_lifo_order(self):
        s = Stack()
        for i in range(4):
            s.push(i)

        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.pop(), 0)

    def test_peek_does_not_remove(self):
        s = Stack()
        s.push(5)
        self.assertEqual(s.peek(), 5)
        self.assertEqual(s.size, 1)

    def test_pop_empty_raises(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()

    def test_peek_empty_raises(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.peek()

    def test_dynamic_resize(self):
        s = Stack()
        initial_capacity = s.capacity

        for i in range(20):
            s.push(i)

        self.assertGreater(s.capacity, initial_capacity)
        self.assertEqual(s.size, 20)


if __name__ == "__main__":
    unittest.main()