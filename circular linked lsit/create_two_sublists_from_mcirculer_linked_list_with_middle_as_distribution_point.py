class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def insertAtLast(self, data):
        temp = node(data)
        if self.end is None:
            self.start = self.end = temp
        else:
            self.end.next = temp
            self.end = temp

        self.end.next = self.start

    def LengthOfCircularLinkedList(self):
        if self.end is None:
            return 0
        count = 1
        temp = self.start.next
        while temp.next is not self.start:
            temp = temp.next
            count = count + 1
        return count + 1

    def display(self):
        print("data in 1 node is {0}".format(self.start.data))
        temp = self.start.next
        i = 2
        while temp is not self.start:
            print("data in {1} node is {0}".format(temp.data, i))
            temp = temp.next
            i = i + 1

    def returnNddeAtPos(self, pos):
        temp = self.start
        if pos == 1:
            return temp
        for i in range(1, pos):
            temp = temp.next
        return temp

    def createTwoSubCircularLinkedList(self, circularlinkedlist2, circularlinkedlist3):
        len = self.LengthOfCircularLinkedList()
        if len % 2 is 1:
            len = len / 2
            len = int(len + 1)
        else:
            len = int(len / 2)
        temp = self.start
        for i in range(1, len):
            temp = temp.next
        circularlinkedlist2.start = self.start
        circularlinkedlist2.end = temp
        circularlinkedlist3.start = temp.next
        temp.next = circularlinkedlist2.start
        circularlinkedlist3.end = self.end
        circularlinkedlist3.end.next = circularlinkedlist3.start




if __name__ == '__main__':
    cl1 = CircularLinkedList()
    cl1.insertAtLast(1)
    cl1.insertAtLast(2)
    cl1.insertAtLast(3)
    cl1.insertAtLast(4)
    cl1.insertAtLast(5)
    cl1.display()
    cl2 = CircularLinkedList()
    cl3 = CircularLinkedList()
    cl1.createTwoSubCircularLinkedList(cl2,cl3)
    print("Data in circular linked list 2 is :\n")
    cl2.display()
    print("Data in circular linked list 3 is :\n")
    cl3.display()