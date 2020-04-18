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

    def LengthLinkedListIterative(self):
        temp = self.head
        count = 0
        while temp:
            count = count + 1
            temp = temp.next
        return count

    def returnNodeAtMiddle(self):
        pos = int(self.LengthLinkedListIterative()/2)+1
        temp = self.head
        if pos is 1:
            return temp
        else:
            for i in range(1,pos):
                temp = temp.next
        return temp







if __name__=='__main__':
    ll = linkedList()
    ll.insertAtStart(10)
    ll.insertAtStart(11)
    ll.insertAtStart(12)
    ll.display()
    newnode = ll.returnNodeAtMiddle()
    print(newnode.data)
