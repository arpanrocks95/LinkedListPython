class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        temp = node(data)
        if self.head is None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def display(self):
        temp = self.head
        i = 0
        while temp is not None:
            print("data is {0} node is {1}".format(i, temp.data))
            i = i + 1
            temp = temp.next
    def returnNodeAtPos(self,pos):
        temp = self.head
        if pos is 1:
            return temp
        else:
            for i in range(1,pos):
                temp = temp.next
        return temp

def intersectNode( linkedlist1, linkedlist2):

    linkedlist1head = linkedlist1.head

    while linkedlist1head is not None:
        linkedlist2head = linkedlist2.head
        while linkedlist2head.next is not None:
            if linkedlist1head.data == linkedlist2head.data:
                print(linkedlist1head.data ,"is the data at intersection node ")
                break
            linkedlist2head = linkedlist2head.next
        linkedlist1head = linkedlist1head.next


if __name__ == '__main__':
    linkedlist1 = linkedList()
    linkedlist2 = linkedList()

    linkedlist1.insertAtStart(30)
    linkedlist1.insertAtStart(15)
    linkedlist1.insertAtStart(9)
    linkedlist1.insertAtStart(6)
    linkedlist1.insertAtStart(3)
    print("Nodes In First Linked List Are")
    linkedlist1.display()

    linkedlist2.head = linkedlist1.returnNodeAtPos(4)
    linkedlist2.insertAtStart(10)
    print("Nodes In Second Linked List Are")
    linkedlist2.display()

    intersectNode(linkedlist1, linkedlist2)

