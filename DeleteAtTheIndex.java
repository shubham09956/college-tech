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
    int size=0;
    public void insertAtBeginning(int data) {
        Node newNode = new Node(data);
        newNode.next = this.head;
        this.head = newNode;
        size++;
    }
    public void deleteAt(int index){
        if(index==0){
            head=head.next;
            return;
        }
     
        Node temp=head;
        for(int i=0;i<index-1;i++){
            temp=temp.next;
        }
        temp.next=temp.next.next;
        size--;
    }

    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }
}
public class DeleteAtTheIndex {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();

        list.insertAtBeginning(10);
        list.insertAtBeginning(20);
        list.insertAtBeginning(31);
        list.insertAtBeginning(70);
        list.insertAtBeginning(30);
        list.insertAtBeginning(7000);
        list.printList();
        list.deleteAt(5); 
        list.printList();
    }
}
