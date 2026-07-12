import unittest
from queue import Queue


class TestQueue(unittest.TestCase):

    def test_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        self.assertEqual(q.size, 0)

    def test_enqueue_dequeue_fifo(self):
        q = Queue()

        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.size, 0)

    def test_peek(self):
        q = Queue()

        q.enqueue(10)
        q.enqueue(20)

        self.assertEqual(q.peek(), 10)
        self.assertEqual(q.size, 2)

    def test_peek_does_not_remove(self):
        q = Queue()

        q.enqueue(5)
        self.assertEqual(q.peek(), 5)
        self.assertEqual(q.size, 1)

    def test_dequeue_empty_raises(self):
        q = Queue()

        with self.assertRaises(IndexError):
            q.dequeue()

    def test_peek_empty_raises(self):
        q = Queue()

        with self.assertRaises(IndexError):
            q.peek()

    def test_dynamic_resize(self):
        q = Queue()
        initial_capacity = q.capacity

        for i in range(20):
            q.enqueue(i)

        self.assertGreater(q.capacity, initial_capacity)
        self.assertEqual(q.size, 20)


if __name__ == "__main__":
    unittest.main()