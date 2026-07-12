class Stack:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        if self.size == self.capacity:
            self._resize()

        self.array[self.size] = item
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        self.size -= 1
        item = self.array[self.size]
        self.array[self.size] = None
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.array[self.size - 1]

    def _resize(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity