// public class InsetAtBeginning {
class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }

}

class linkedList {
    Node head;
    Node tail;

    linkedList() {
        head = null;
        tail = null;
    }

    public void insertAtBeginning(int data) {
        Node x = new Node(data);
        x.next = this.head;
        this.head = x;
        if (tail == null) {
            tail = x;
        }

    }

    public void insertAtEnd(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;

        } else {
            tail.next = newNode;
        }
        tail = newNode;
        // Node current = head;
        // while (current.next != null) {
        // current = current.next;
        // }
        // current.next = newNode;
    }

    public void display() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
    }
}

public class InsertAtEnd {

    public static void main(String[] args) {
        linkedList ll = new linkedList();
        ll.insertAtBeginning(5);
        ll.insertAtBeginning(12);
        ll.insertAtBeginning(53);
        ll.insertAtBeginning(50);
        ll.insertAtBeginning(55);
        ll.insertAtBeginning(51992);
        ll.insertAtEnd(23);
        ll.insertAtEnd(2400);
        ll.insertAtEnd(250);

        ll.display();
    }
}
