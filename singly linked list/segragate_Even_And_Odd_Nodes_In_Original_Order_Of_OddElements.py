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
    def returnNodeAtPos(self,pos):
        temp = self.head
        if pos is 1:
            return temp
        else:
            for i in range(1,pos):
                temp = temp.next
        return temp

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
            count = count+1
            temp = temp.next
        return count

    def segragateEvenAndOddNodesNotInOriginalOrderOfOddElements(self):
        len = self.LengthLinkedListIterative()
        for i in range(len):
            kl = 0
            temp = self.head

            while (temp.data%2) == 0:
                temp = temp.next
                kl = kl+1

            if (temp.data%2) ==1:
                tempLastNode = self.returnNodeAtPos(len)
                if temp == self.head:
                    self.head = self.head.next
                    temp.next = None
                    tempLastNode.next = temp
                else:
                    tempNode = self.returnNodeAtPos(kl)
                    tempNode.next = temp.next
                    temp.next = None
                    tempLastNode.next = temp



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



