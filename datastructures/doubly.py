class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def insert_position(self, position, data):
        if position < 0:
            return

        if position == 0:
            self.insert_beginning(data)
            return

        new_node = Node(data)
        current = self.head

        for _ in range(position - 1):
            if current is None:
                return
            current = current.next

        if current is None:
            return

        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node

        current.next = new_node

    def delete_beginning(self):
        if self.head is None:
            return

        self.head = self.head.next

        if self.head:
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head

        while current.next:
            current = current.next

        current.prev.next = None

    def delete_value(self, value):
        current = self.head

        while current and current.data != value:
            current = current.next

        if current is None:
            return

        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next:
            current.next.prev = current.prev

    def search(self, value):
        current = self.head
        index = 0

        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1

        return -1

    def length(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    def to_list_forward(self):
        result = []
        current = self.head

        while current:
            result.append(current.data)
            current = current.next

        return result

    def to_list_backward(self):
        result = []

        current = self.head

        if current is None:
            return result

        while current.next:
            current = current.next

        while current:
            result.append(current.data)
            current = current.prev

        return result