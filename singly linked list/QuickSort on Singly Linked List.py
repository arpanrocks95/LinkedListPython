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

    def displayLinkedList(self):
        iterNode = self.head
        i=1
        while iterNode:
            print("element in node {0} is {1}".format(i,iterNode.data))
            i=i+1
            iterNode = iterNode.next


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





if __name__ == '__main__':
    ll = LinkedList()
    ll.insertAtStart(10)
    ll.insertAtStart(10)
    ll.insertAtStart(10)
    ll.insertAtStart(1777)
    ll.insertAtStart(1777)
    ll.insertAtStart(122)
    ll.displayLinkedList()
    ll.sortLinkedList(1,ll.LengthLinkedListIterative())
    print("after sorting")
    ll.displayLinkedList()
