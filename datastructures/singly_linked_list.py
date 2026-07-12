class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
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
        current.next = new_node

    def delete_beginning(self):
        if self.head:
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None

    def delete_value(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        if current.next:
            current.next = current.next.next

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

    def reverse(self):
        prev = None
        current = self.head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        self.head = prev

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
