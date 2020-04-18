class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtStart(self,data):
        temp = node(data)
        if self.head is not None:
            temp.next = self.head
        self.head = temp
    def deleteLinkedList(self):
        temp1= self.head
        temp2 = self.head
        temp2 = temp2.next
        while temp1:
            temp1 = None
            temp1 = temp2
            if temp2.next is not None:
                temp2 = temp2.next
    def display(self):
        print("inside display")
        temp = self.head
        if temp is None:
            print("no elements in the linked list ")
            return
        count = 0
        while temp:
            print("element in node {0} is {1}".format(count,temp.data))
            temp = temp.next
            count = count+1

if __name__=='__main__':
    ll = LinkedList()
    ll.insertAtStart(10)
    ll.insertAtStart(15)
    ll.insertAtStart(12)
    ll.insertAtStart(14)
    ll.display()
    ll.deleteLinkedList()

