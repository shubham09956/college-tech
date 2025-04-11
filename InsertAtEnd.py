class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print() 


ll = LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(12)
ll.insert_at_beginning(53)
ll.insert_at_beginning(50)
ll.insert_at_beginning(55)
ll.insert_at_beginning(51992)
ll.insert_at_end(23)
ll.insert_at_end(2400)
ll.insert_at_end(250)
ll.insert_at_end(252)
ll.display() 