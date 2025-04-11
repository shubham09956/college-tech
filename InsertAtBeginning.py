class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=" ")
            current=current.next
        print()

linked_list = LinkedList()

linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(20)
linked_list.insert_at_beginning(31)
linked_list.insert_at_beginning(70)
linked_list.insert_at_beginning(30)
linked_list.insert_at_beginning(7000)

linked_list.display()  
    
