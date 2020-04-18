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


def createInterSectedLinkedList( linkedlist1, linkedlist2, linkedlistInterSection):

    linkedlist1head = linkedlist1.head

    while linkedlist1head is not None:
        linkedlist2head = linkedlist2.head
        while linkedlist2head.next is not None:


            if linkedlist1head.data == linkedlist2head.data:
                break
            linkedlist2head = linkedlist2head.next

        if linkedlist1head.data == linkedlist2head.data:
            linkedlistInterSection.insertAtStart(linkedlist1head.data)
        linkedlist1head = linkedlist1head.next


if __name__ == '__main__':
    linkedlist1 = linkedList()
    linkedlist2 = linkedList()
    linkedlistInterSection = linkedList()
    linkedlist1.insertAtStart(6)
    linkedlist1.insertAtStart(4)
    linkedlist1.insertAtStart(3)
    linkedlist1.insertAtStart(2)
    linkedlist1.insertAtStart(1)
    print("Nodes In First Linked List Are")
    linkedlist1.display()

    linkedlist2.insertAtStart(6)
    linkedlist2.insertAtStart(4)
    linkedlist2.insertAtStart(2)
    print("Nodes In Second Linked List Are")
    linkedlist2.display()

    createInterSectedLinkedList(linkedlist1, linkedlist2, linkedlistInterSection)

    print("Nodes In InterSected Linked List Are")
    linkedlistInterSection.display()
