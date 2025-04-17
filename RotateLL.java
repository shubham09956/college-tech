class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    Node head;

    LinkedList() {
        head = null;
    }

    public void insertAtEnd(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
        }
    }

    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }
    public void rotate(int k) {
        if (head == null || head.next == null || k == 0) {
            return;
        }

        Node current = head;
        int length = 1;
        while (current.next != null) {
            current = current.next;
            length++;
        }

        k = k % length;
        if (k == 0) {
            return;
        }

        current = head;
        for (int i = 1; i < length - k; i++) {
            current = current.next;
        }

        Node newHead = current.next;
        current.next = null;

        Node temp = newHead;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = head;

        head = newHead;
    }
}
public class RotateLL {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();

        list.insertAtEnd(10);
        list.insertAtEnd(20);
        list.insertAtEnd(30);
        list.insertAtEnd(40);
        list.insertAtEnd(50);

        System.out.println("Original Linked List:");
        list.printList();

        list.rotate(2);
        list.printList();

        
    }
    
}
