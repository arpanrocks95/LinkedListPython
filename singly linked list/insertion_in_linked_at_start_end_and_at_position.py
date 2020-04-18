class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtStart(self, y):
        tempNode = Node(y)
        if self.head is not None:
            tempNode.next = self.head
        self.head = tempNode
    def insertLast(self,y):
        tempNode = Node(y)
        if self.head is None:
            self.head = tempNode
        iterNode = self.head
        while iterNode.next:
            iterNode = iterNode.next
        iterNode.next = tempNode

    def insertAtPos(self,y,pos):
        tempNode = Node(y)
        iterNode = self.head
        for i in range(1,pos-1):
            iterNode = iterNode.next
        tempNode.next = iterNode.next
        iterNode.next = tempNode
    def displayLinkedList(self):
        iterNode = self.head
        i=1
        while iterNode:
            print("element in node {0} is {1}".format(i,iterNode.data))
            i=i+1
            iterNode = iterNode.next

if __name__=='__main__':
    l1 = LinkedList();
    l1.insertAtStart(5);
    l1.insertAtStart(6);
    l1.insertLast(10);
    l1.insertLast(13);
    l1.insertAtPos(213,3);
    l1.displayLinkedList();
