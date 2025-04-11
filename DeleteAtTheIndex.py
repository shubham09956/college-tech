class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    size = 0
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_at(self, index):
        if index < 0 or index >= self.size:
            print("Index out of bounds")
            return
        
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            if temp.next is not None:
                temp.next = temp.next.next
        self.size -= 1

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()



linked_list = LinkedList()

linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(20)
linked_list.insert_at_beginning(31)
linked_list.insert_at_beginning(70)
linked_list.insert_at_beginning(30)
linked_list.insert_at_beginning(7000)

linked_list.print_list()  

linked_list.delete_at(4) 
linked_list.print_list()  