class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None
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
            self.head.next = self.head.next.next
        elif pos >2 :
            for i in range(1,pos-1):
                if tempNode.next is not None:
                        tempNode=tempNode.next
            tempNode2 = tempNode.next
            tempNode.next = tempNode.next.next
            tempNode2 = None


    def find(self,data):
        tempNode = self.head
        while tempNode:
            if tempNode.data == data:
                print("IN SEARCHING DATA FOUND {0}".format(tempNode.data))
                return
            tempNode = tempNode.next
        print("{0} DOES NOT EXISTS IN THIS LINKED LIST ".format(data))
    def LengthLinkedListIterative(self):
        temp = self.head
        count = 0
        while temp:
            count = count + 1
            temp = temp.next
        return count

    def returnNodeAtPos(self, pos):
        temp = self.head
        if pos is 1:
            return temp
        else:
            for i in range(1, pos):
                temp = temp.next
        return temp

    def partition(self, low, upper):
        pivot = self.returnNodeAtPos(upper).data
        i = low - 1
        for j in range(low, upper):
            if self.returnNodeAtPos(j).data < pivot:
                i = i + 1
                self.returnNodeAtPos(i).data, self.returnNodeAtPos(j).data = self.returnNodeAtPos(j).data , self.returnNodeAtPos(i).data

        self.returnNodeAtPos(i+1).data, self.returnNodeAtPos(upper).data = self.returnNodeAtPos(upper).data, self.returnNodeAtPos(i+1).data
        return (i + 1)

    def sortLinkedList(self,low,upper):
        if low < upper:
            n = self.partition(low, upper)
            self.sortLinkedList(low, n - 1)
            self.sortLinkedList(n + 1, upper)


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
    l1.sortLinkedList(1,l1.LengthLinkedListIterative());
    print("After sorting")
    l1.displayLinkedList();
    l1.delANodeAtPos(3)
    print("After deletig at position3 ")
    l1.displayLinkedList();
    l1.find(5);
    l1.find(100);
    l1.delANodeWithKey(213);
    print("After deleting at key 213 ")
    l1.displayLinkedList();