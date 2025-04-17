class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return -1
        val = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return val

    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return -1
        return self.front.data

    def get_size(self):
        return self.size

    def display(self):
        temp = self.front
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)

  
    q.display()
    print("Front element:", q.peek())
    print("Dequeued element:", q.dequeue())
    print("Queue elements after dequeue:")
    q.display()
    print("Current size of queue:", q.get_size())