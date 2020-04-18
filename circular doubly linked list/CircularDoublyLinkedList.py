class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


class DoublyCircularLinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def insertAtLast(self, data):
        temp = Node(data)

        if self.end is None:
            temp.prev = self.start
            temp.next = self.start
            self.start = temp
            self.end = temp;
            return

        else:
            iterator = self.start
            while iterator is not self.end:
                iterator = iterator.next

            iterator.next = temp
            temp.prev = iterator
            temp.next = self.start
            self.end = temp
            self.start.prev = self.end

    def display(self):
        temp = self.start
        print("data in node 1 is {0}".format(self.start.data))
        count = 1
        while temp.next is not self.end:
            temp = temp.next
            count = count + 1
            print("data in node {1} is {0}".format(temp.data, count))
        print("data in node {1} is {0}".format(temp.next.data, count + 1))

    def insertAtStart(self, data):
        temp = Node(data)
        if self.start is None:
            temp.next = self.start
            temp.prev = self.start
            self.end = temp
            self.start = temp

        temp.next = self.start
        self.start.prev = temp
        self.start = temp
        temp.prev = self.end
        self.end.next = self.start

    def insertAtPosition(self, data, pos):
        temp = Node(data)
        if pos is 1:
            temp.next = self.start
            self.start.prev = temp
            self.start = temp
            temp.prev = self.end
            self.end.next = self.start

        else:
            iterNode = self.start
            for i in range(1, pos - 1):
                iterNode = iterNode.next
            if pos is not self.lenOfDoublyCircularLinkedList() + 1:
                temp.prev = iterNode
                temp.next = iterNode.next
                iterNode.next.prev = temp
                iterNode.next = temp
            else:
                iterNode.next = temp
                temp.prev = iterNode
                self.end = temp
                self.end.next = self.start
                self.start.prev = self.end

    def lenOfDoublyCircularLinkedList(self):
        temp = self.start.next
        if self.start is None:
            return 0
        count = 1
        while temp is not self.start:
            temp = temp.next
            count = count + 1
        return count

    def deleteNodeWithData(self, data):
        temp1 = self.start
        if temp1.data is data:
            self.start = temp1.next
            self.start.prev = self.end
            self.end.next = self.start
            return
        temp2 = self.start.next
        while temp2.data is not data:
            temp1 = temp1.next
            temp2 = temp2.next
        temp1.next = temp2.next
        temp2.next.prev = temp1
        if temp2 is self.end:
            self.end = temp1

    def returnNodeAtPosition(self,pos):
        temp = self.start
        for i in range(pos-1):
            temp = temp.next
        return temp

if __name__ == '__main__':
    l1 = DoublyCircularLinkedList()
    l1.insertAtLast(10)
    l1.insertAtLast(11)
    l1.insertAtLast(12)
    l1.insertAtStart(9)
    l1.insertAtPosition(8, 1)
    l1.display()
    print("after entering dataa t pos len+1")
    l1.insertAtPosition(14, 6)
    l1.display()
    print("after entering dataa t pos len")
    l1.insertAtPosition(13, 6)
    l1.display()
    print("after entering deleting 14")  # 8,9,14
    l1.deleteNodeWithData(14)
    l1.display()
    print("data at 5 position is ",l1.returnNodeAtPosition(5).data)
