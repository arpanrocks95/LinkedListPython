class node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class doublyLinkedList():
    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        temp = node(data)
        if self.head is None:
            temp.prev = self.head
            temp.next = None
            self.head = temp
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
            temp.prev = self.head

    def insertATLast(self,data):
        temp = node(data)
        if self.head is None:
            self.head = temp
            temp.prev = self.head
            temp.next = None
        else:
            iternode = self.head
            while iternode.next is not None:
                iternode = iternode.next
            iternode.next = temp
            temp.prev = iternode
            temp.next = None

    def insertAtPosition(self,data,pos):
        temp = node(data)
        if pos == 1:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
            temp.prev = self.head
        else:
            iternode = self.head
            for i in range(1,pos-1):
                iternode = iternode.next
                print("data in iternode is ",iternode.data)
            if pos == self.lengthOfDoubleeLinkedList()+1:
                iternode.next = temp
                temp.prev = iternode
                temp.next = None
            else:
                temp.prev = iternode
                temp.next = iternode.next
                iternode.next.prev = temp
                iternode.next = temp

    def deleteAtData(self,data):

        temp1 = self.head
        if data == temp1.data:
            temp1.next.prev = self.head
            self.head = temp1.next
            temp1 = None
        else:

            temp2 = self.head.next
            while temp2.data != data:
                temp2 = temp2.next
                temp1 = temp1.next
            temp1.next = temp2.next
            if temp2.next is not None:
                temp2.next.prev = temp1
            temp2 = None


    def display(self):
        temp = self.head
        count = 1
        while(temp is not None):
            print("data in node {0} is {1}".format(count,temp.data))
            temp = temp.next
            count = count + 1
    def lengthOfDoubleeLinkedList(self):
        temp = self.head
        count = 0
        while(temp is not None):
            temp = temp.next
            count = count + 1
        return count

if __name__ =='__main__':
    l1 = doublyLinkedList()
    l1.insertATLast(12)
    l1.insertAtStart(11)
    l1.insertAtStart(10)
    l1.insertATLast(13)
    print("length of linked list is :",l1.lengthOfDoubleeLinkedList())
    l1.display()
    l1.insertAtPosition(9 , 1)
    print("after inserting at pos 1")
    l1.display()
    l1.insertAtPosition(15, 6)
    print("after inserting at pos last")
    l1.display()
    l1.insertAtPosition(14, 6)
    print("after inserting at pos last-1")
    l1.display()
    l1.deleteAtData(13)
    print("after deleting ")
    l1.display()
