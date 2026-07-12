class Queue:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.array = [None] * capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.size == self.capacity:
            self._resize()

        rear = (self.front + self.size) % self.capacity
        self.array[rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        item = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.array[self.front]

    def _resize(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity

        for i in range(self.size):
            new_array[i] = self.array[(self.front + i) % self.capacity]

        self.array = new_array
        self.capacity = new_capacity
        self.front = 0