class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return -1
        val = self.top.data
        self.top = self.top.next
        self.size -= 1
        return val

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return -1
        return self.top.data

    def get_size(self):
        return self.size

    def display(self):
        temp = self.top
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    s = Stack()
    s.push(12)
    s.push(13)
    s.push(14)
    s.push(15)
    s.push(16)
    s.push(17)

    print("Stack elements:")
    s.display()
    print("Top element:", s.peek())
    print("Popped element:", s.pop())
    print("Stack elements after pop:")
    s.display()
    print("Current size of stack:", s.get_size())