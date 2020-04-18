class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedList:
    def __init__(self):
        self.head = None
    def insertAtStart(self,data):
        temp = node(data)
        if self.head is None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp
    def display(self):
        temp = self.head
        i=0
        while temp is not None:
            print("data is {0} node is {1}".format(i,temp.data))
            i = i+1
            temp = temp.next
    def deleteDuplicatesInSortedLinkedList(self):
        temp = self.head
        while temp.next != None:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next



if __name__=='__main__':
    ll = linkedList()
    ll.insertAtStart(10)
    ll.insertAtStart(10)
    ll.insertAtStart(10)
    ll.insertAtStart(1777)
    ll.insertAtStart(1777)
    ll.insertAtStart(122)
    ll.display()
    ll.deleteDuplicatesInSortedLinkedList()
    print("after duplicate key deletions")
    ll.display()
