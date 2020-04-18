class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,data):
        p = node(data)
        p.next = self.head
        temp = self.head
        if self.head != None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = p
        else:
            p.next = p
        self.head = p

    def display(self):
        temp = self.head
        print("data in node {1}  is {0}".format(temp.data,1))
        temp = temp.next
        i = 1
        while temp.next != self.head:
            i = i+1
            temp = temp.next
            print("data in node {1}  is {0}".format(temp.data,i))



if __name__ =='__main__':
    ll = linkedlist()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.display()