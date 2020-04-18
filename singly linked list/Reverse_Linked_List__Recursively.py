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

    def reverse(self,head):
        if (head== None):
            return None

        if (head.next == None):
            self.head = head
            return head

        node1 = self.reverse(head.next)
        node1.next = head
        head.next = None
        return head

    def reverseRecursive(self):
        self.reverse(self.head)





if __name__=='__main__':
    ll = linkedList()
    ll.insertAtStart(5)
    ll.insertAtStart(4)
    ll.insertAtStart(3)
    ll.insertAtStart(2)
    ll.insertAtStart(1)
    ll.display()

    ll.reverseRecursive()
    print("after Reversing")
    ll.display()

