class MhsTIF(object):
    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    
    def __str__(self):
        x=str(self.NIM)+" "+self.nama+" "+self.kotaTinggal+" "+str(self.uangSaku)
        return x
    
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.NIM
    def ambilKota(self):
        return self.kotaTinggal
    def ambilUangSaku(self):
        return self.uangSaku

c0 = MhsTIF("Annida", "L200183147", "Pelaihari", 240000)
c1 = MhsTIF("Aulia", "L200183070", "Boyolali", 230000)
c2 = MhsTIF("Azie", "L200183174", "Sragen", 250000)
c3 = MhsTIF("Dipa", "L200184137", "Sidoarjo", 235000)
c4 = MhsTIF("Hapsa", "L200184172", "Kendal", 240000)
c5 = MhsTIF("Sipa", "L200183203", "Ciamis", 250000)
c6 = MhsTIF("Farah", "L200183094", "Klaten", 245000)
c7 = MhsTIF("Naura", "L200183159", "palembang", 245000)
c8 = MhsTIF("Lulu", "L200183103", "Solo Baru", 245000)
c9 = MhsTIF("Anggit", "L200180119", "Bima", 270000)
c10 = MhsTIF("Ulin", "L200180125", "Madiun", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp
def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i]<A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

def bubbleSort(A):
    n=len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j]>A[j+1]:
                swap(A,j,j+1)


def selectionSort(A):
    n= len(A)
    for i in range(n-1):
        indexKecil=cariPosisiYangTerkecil(A,i,n)
        if indexKecil != i:
            swap(A,i,indexKecil)


def insertionSort(A):
    n=len(A)
    for i in range(1,n):
        nilai = A[i]
        pos=i
        while pos>0 and nilai<A[pos-1]:
            A[pos]=A[pos-1]
            pos=pos-1
        A[pos]=nilai
        
def mhsSort(A):
    n= len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos>0 and nilai.NIM<A[pos-1].NIM:
            A[pos]=A[pos-1]
            pos=pos-1
        A[pos] = nilai

mhsSort(Daftar)
print('\n'.join(map(str, Daftar)))
