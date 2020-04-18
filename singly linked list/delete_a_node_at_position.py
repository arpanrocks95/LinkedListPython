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

    def delANodeAtPos(self, pos):
        tempNode = self.head
        if pos is 1:
            self.head = self.head.next
            tempNode = None
        elif pos is 2:
            tempNode = tempNode.next
            self.head.next = self.head.next.next
            tempNode =None
        elif pos >2 :
            for i in range(1,pos-1):
                if tempNode.next is not None:
                        tempNode=tempNode.next
            tempNode2 = tempNode.next
            tempNode.next = tempNode.next.next
            tempNode2 = None


if __name__=='__main__':
    l1 = LinkedList();
    l1.insertAtStart(5);
    l1.insertAtStart(6);
    l1.insertLast(10);
    l1.insertLast(13);
    l1.insertAtPos(213,3);
    l1.displayLinkedList();
    l1.delANodeAtPos(3)
    print("After deletig at position3 ")
    l1.displayLinkedList();
