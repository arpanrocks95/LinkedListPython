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
    def SearchLinkedListIterative(self,data):
        tempNode = self.head
        while tempNode:
            if tempNode.data == data:
                print("{0} is found in the linked list".format(tempNode.data))
                return
            tempNode = tempNode.next
        print("{0} DOES NOT EXISTS IN THIS LINKED LIST ".format(data))


    def SearchLinkedListRecursive(self,current,data):

        if current.data is data:
            print("{0} is found in the linked list ".format(data))
            return
        elif current.data is not data :
            return self.SearchLinkedListRecursive(current.next,data)
    def SearchofllR(self,data):
        return self.SearchLinkedListRecursive(self.head,data)




if __name__=='__main__':
    ll = linkedList()
    ll.insertAtStart(10)
    ll.insertAtStart(11)
    ll.insertAtStart(12)
    ll.display()
    ll.SearchLinkedListIterative(10)
    ll.SearchofllR(12)
