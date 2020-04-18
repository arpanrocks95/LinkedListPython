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
    def delANodeWithKey(self,data):
        tempNode1 = self.head
        if self.head.data is data:
            self.head = self.head.next
            tempNode1 = None
            return
        tempNode2 = self.head
        tempNode2 = tempNode2.next
        while tempNode2.data is not data and tempNode1.data is not data and tempNode1.next is not None and tempNode2.next:
            tempNode2 = tempNode2.next
            tempNode1 = tempNode1.next
        if tempNode2.next is None:
            tempNode1.next = None
            tempNode2 = None
        elif tempNode2.next is not None:
            tempNode1.next = tempNode2.next
            tempNode2 = None






if __name__=='__main__':
    l1 = LinkedList();
    l1.insertAtStart(5);
    l1.insertAtStart(6);
    l1.insertLast(10);
    l1.insertLast(13);
    l1.insertAtPos(213,3);
    l1.displayLinkedList();
    l1.delANodeWithKey(5)
    print("After deleting")
    l1.displayLinkedList();
