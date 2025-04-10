class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_last_transaction(self):
        current = self.head
        if current is None:
            print("No withdraws/deposits found.")
        else:
            print(current.data)
            current = current.next

    def print_all_transactions(self):
        current = self.head
        if current is None:
            print("No withdraws/deposits found.")
        while current:
            print(current.data)
            current = current.next