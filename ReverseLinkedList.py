class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = new_node

    def print_list(self):
        current = self.head
        while current != None:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse(self):
        prev = None
        current = self.head
        next_node = None

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)
    linked_list.insert_at_end(50)

    print("Original Linked List:")
    linked_list.print_list()

    linked_list.reverse()

    print("Reversed Linked List:")
    linked_list.print_list()