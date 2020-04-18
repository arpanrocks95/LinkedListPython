class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def insertAtStart(self, data):
        temp = node(data)

        if self.end is None:
            self.start = self.end = temp

        else:
            temp.next = self.start
            self.start = temp
        self.end.next = self.start


    def insertAtLast(self,data):
        temp = node(data)
        if self.end is None:
            self.start = self.end = temp
        else:
            self.end.next = temp
            self.end = temp

        self.end.next = self.start

    def insertAtPosition(self,data,pos):
        temp = node(data)
        iterator = self.start
        if pos >1 :
            for i in range(1,pos):
                iterator = iterator.next
            temp.next = iterator.next
            iterator.next = temp

            if pos == self.LengthOfCircularLinkedList():
                self.end = temp
        else:
            if self.end is None:
                self.start = self.end = temp
            else:
                temp.next = self.start
                self.start = temp
            self.end.next = self.start


    def LengthOfCircularLinkedList(self):
        if self.end is None:
            return 0
        count = 1
        temp = self.start.next
        while temp.next is not self.start:
            temp = temp.next
            count = count+1
        return count+1

    def display(self):
        print("data in 1 node is {0}".format(self.start.data))
        temp = self.start.next
        i = 2
        while temp is not self.start:
            print("data in {1} node is {0}".format(temp.data, i))
            temp = temp.next
            i = i + 1

    def returnNddeAtPos(self,pos):
        temp = self.start
        if pos == 1:
            return temp
        for i in range(1,pos):
            temp = temp.next
        return temp

    def deleteNodeAtData(self,data):
        temp1 = self.start
        temp2 = self.start.next
        if temp1.data == data:
            self.start = temp2
            self.end.next = self.start
            return

        else:
            while temp2.data is not data:
                temp2 = temp2.next
                temp1 = temp1.next
            temp1.next = temp1.next.next

            if self.end is None:
                self.end = temp1



if __name__ == '__main__':
    cl = CircularLinkedList()
    cl.insertAtStart(3)
    cl.insertAtStart(2)
    cl.insertAtStart(1)
    cl.insertAtLast(4)
    cl.display()
    print(cl.LengthOfCircularLinkedList())
    cl.insertAtPosition(1000,1)
    print()
    cl.display()
    print()
    print()
    print(cl.returnNddeAtPos(3).data)

    cl.deleteNodeAtData(4)
    print()
    cl.display()