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

    def segragateEvenAndOddNodesNotInOriginalOrderOfOddElements(self):
        tempEven = self.head
        tempOdd = self.head
        while tempEven !=None:
            if (tempEven.data%2) == 0:
                if (tempOdd.data%2) ==1:
                    temp = tempOdd.data
                    tempOdd.data = tempEven.data
                    tempEven.data = temp
                    tempOdd = tempOdd.next
            tempEven = tempEven.next



if __name__=='__main__':
    ll = linkedList()
    ll.insertAtStart(6)
    ll.insertAtStart(7)
    ll.insertAtStart(1)
    ll.insertAtStart(4)
    ll.insertAtStart(5)
    ll.insertAtStart(10)
    ll.insertAtStart(12)
    ll.insertAtStart(8)
    ll.insertAtStart(15)
    ll.insertAtStart(17)
    ll.display()

    ll.segragateEvenAndOddNodesNotInOriginalOrderOfOddElements()
    print("\n\nafter segragating \n\n")
    ll.display()



