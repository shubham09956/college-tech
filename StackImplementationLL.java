class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class Stack {
    Node top;
    private int size = 0;

    Stack() {
        this.top = null;
    }

    public void push(int data) {
        Node x = new Node(data);
        x.next = top;
        top = x;
        size++;
    }

    public int pop() {
        if (top == null) {
            System.out.println("Stack is empty");
            return -1;
        }
        int val = top.data;
        top = top.next;
        size--;
        return val;
    }

    public int peek() {
        if (top == null) {
            System.out.println("Stack is empty");
            return -1;
        }
        return top.data;
    }

    public int size() {
        return size;
    }

    public void display() {
        Node temp = top;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }
}

public class StackImplementationLL {
    public static void main(String[] args) {
        Stack s = new Stack();
        s.push(12);
        s.push(13);
        s.push(14);
        s.push(15);
        s.push(16);
        s.push(17);
        
        System.out.println("Stack elements:");
        s.display();
        System.out.println("Top element: " + s.peek());
        System.out.println("Popped element: " + s.pop());
        System.out.println("Stack elements after pop:");
        s.display();
        System.out.println("Current size of stack: " + s.size());
    }
}