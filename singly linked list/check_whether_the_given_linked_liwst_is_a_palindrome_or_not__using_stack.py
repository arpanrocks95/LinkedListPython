
class stackNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None
    def push(self,data):
        temp = stackNode(data)
        temp.next = self.top
        self.top = temp
    def peek(self):
        return  self.top.data
    def pop(self):
        temp = self.top
        self.top = self.top.next
        print("popped data is {0}".format(temp.data))
        temp = None



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
        i=1
        while temp is not None:
            print("data is {0} node is {1}".format(i,temp.data))
            i = i+1
            temp = temp.next
    def isPlaindrome(self):
        desc = 0
        temp = self.head
        tempStack = stack()
        while(temp):
            tempStack.push(temp.data)
            temp = temp.next
        temp = self.head
        while (temp):
            if temp.data == tempStack.peek():
                desc = 1
            else:
                desc = 0
                break
            tempStack.pop()
            temp = temp.next
        if desc == 1:
            print("The given linked list is a palindrome ")
        elif desc == 0:
            print("The given linked list is not a palindrome ")


if __name__=='__main__':
    ll = linkedList()
    ll.insertAtStart(10)
    ll.insertAtStart(11)
    ll.insertAtStart(12)
    ll.insertAtStart(11)
    ll.insertAtStart(10)

    ll.display()
    ll.isPlaindrome()