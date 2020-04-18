class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        temp = node(data)
        if self.head is None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def display(self):
        temp = self.head
        i = 0
        while temp is not None:
            print("data is {0} node is {1}".format(i, temp.data))
            i = i + 1
            temp = temp.next

    def LengthLinkedListIterative(self):
        temp = self.head
        count = 0
        while temp:
            count = count + 1
            temp = temp.next
        return count

    def returnNodeAtPos(self, pos):
        temp = self.head
        if pos is 1:
            return temp
        else:
            for i in range(1, pos):
                temp = temp.next
        return temp

    def partition(self, low, upper):
        pivot = self.returnNodeAtPos(upper).data
        i = low - 1
        for j in range(low, upper):
            if self.returnNodeAtPos(j).data < pivot:
                i = i + 1
                self.returnNodeAtPos(i).data, self.returnNodeAtPos(j).data = self.returnNodeAtPos(j).data , self.returnNodeAtPos(i).data

        self.returnNodeAtPos(i+1).data, self.returnNodeAtPos(upper).data = self.returnNodeAtPos(upper).data, self.returnNodeAtPos(i+1).data
        return (i + 1)

    def quickSort(self, low, upper):
        if low < upper:
            n = self.partition(low, upper)
            self.quickSort(low, n - 1)
            self.quickSort(n + 1, upper)

    def deleteDuplicatesInUnSortedLinkedList(self):
        self.quickSort(1, self.LengthLinkedListIterative())
        temp = self.head
        while temp.next != None:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next


if __name__ == '__main__':
    ll = linkedList()
    ll.insertAtStart(10)
    ll.insertAtStart(10)
    ll.insertAtStart(10)
    ll.insertAtStart(1777)
    ll.insertAtStart(1777)
    ll.insertAtStart(122)
    ll.display()
    ll.deleteDuplicatesInUnSortedLinkedList()
    print("after duplicate key deletions")
    ll.display()
