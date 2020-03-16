class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
class LinkedList():
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    def listprint(self):
        printval = self.head
        hasil = []
        while printval is not None:
            hasil.append(printval.data)
            printval = printval.next
        print(hasil)
    def cari(self, nilai):
        cek = self.head
        a = 1
        while cek is not None:
            if cek.data == nilai:
                print("terdapat pada urutan ke-"+str(a))
                break
            if cek.data != nilai:
                a += 1
                cek = cek.next
    def tambahDepan(self, b):
        b.next = self.head
        self.head = b
    def tambahAkhir(self, c):
        self.tail.next = c
        self.tail = c
    def tambah(head, posisi):
        newNode = Node(8)
        newNode.next = posisi.next
        posisi.next = newNode
        head.head = posisi
        return head
    def hapus(self, posisi): 
        hapus = self.head 
        if posisi == 0: 
            self.head = temp.next
            hapus = None
        for i in range(posisi-1): 
            hapus = hapus.next
            if hapus is None: 
                break
        next = hapus.next.next
        hapus.next = next 
        
        
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

linked.listprint()
linked.cari(16)

#b
k = Node(22)
linked.tambahDepan(k)
linked.listprint()
print(linked.head.data)

#c
l = Node(44)
linked.tambahAkhir(l)
linked.listprint()
print(linked.tail.data)

#d
linked.tambah(b)
linked.listprint()
print(linked.head.data)

#e
linked.hapus(5)
linked.listprint()
