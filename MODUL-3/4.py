class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    def listPrint(self):
        isi = self.head
        tempat = []
        while isi is not None:
            tempat.append(isi.data)
            isi = isi.next
        print(tempat)
    def tampilkan(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
    def tambahDepan(self, a):
        a.next = self.head
        self.head = a
    def tambahAkhir(self, b):
        self.tail.next = b
        self.tail = b
            
a = Node(16)
b = Node(26)
c = Node(36)
d = Node(46)
e = Node(56)

a.next = b
b.next = c
c.next = d
d.next = e

linked = LinkedList()
linked.head = a
linked.tail = e

#a
linked.tampilkan()

#b
linked.tambahDepan(b)
linked.listPrint()

#c
A = Node(44)
linked.tambahAkhir(A)
linked.listPrint()
