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
    def LengthLinkedListRecursive(self,current):
        if (not current):
            return 0
        else:
            return 1+self.LengthLinkedListRecursive(current.next)
    def LengthofllR(self):
        return self.LengthLinkedListRecursive(self.head)
    def LengthLinkedListIterative(self):
        temp = self.head
        count = 0
        while temp:
            count = count+1
            temp = temp.next
        return count


if __name__=='__main__':
    ll = linkedList()
    ll.insertAtStart(10)
    ll.insertAtStart(11)
    ll.insertAtStart(12)
    ll.display()
    print("length of linked list recursively is ",ll.LengthofllR());
    print("length of linked list iteratively is ", ll.LengthLinkedListIterative());
