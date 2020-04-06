class MhsTIF(object):
    def __init__(self,nama,nim,kota):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota


c0 = MhsTIF("Annida", "L200183147", "Pelaihari")
c1 = MhsTIF("Aulia", "L200183070", "Boyolali")
c2 = MhsTIF("Azie", "L200183174", "Sragen")
c3 = MhsTIF("Dipa", "L200184137", "Sidoarjo")
c4 = MhsTIF("Hapsa", "L200184172", "Kendal")
c5 = MhsTIF("Sipa", "L200183203", "Ciamis")
c6 = MhsTIF("Farah", "L200183094", "Klaten")
c7 = MhsTIF("Naura", "L200183159", "palembang")
c8 = MhsTIF("Lulu", "L200183103", "Solo Baru")
c9 = MhsTIF("Anggit", "L200180119", "Bima")
c10 = MhsTIF("Ulin", "L200180125", "Madiun")


Daftar = [c0.nim, c1.nim, c2.nim, c3.nim, c4.nim, c5.nim, c6.nim, c7.nim, c8.nim, c9.nim, c10.nim]


def merge_sort(A, B):
    start = A[0]
    end = A[1]
    mid = (end - start) // 2 + start
    
    if start < mid:
        merge_sort((start, mid), B)

    if mid + 1 <= end and end - start != 1:
       merge_sort((mid + 1, end), B)

    subList(B, A[0], A[1])
    
    return B
    
    
def subList(B, start, end):
    mulai = start
    List = (end - start)//2 + start + 1
    List2 = List
    new_list = []
    
    while start < List and List2 <= end:
        first1 = B[start]
        first2 = B[List2]
        if first1 > first2:
            new_list.append(first2)
            List2 += 1
        else:
            new_list.append(first1)
            start += 1
            
    while start < List :
        new_list.append(B[start])
        start += 1

    while List2 <= end:
        new_list.append(B[List2])
        List2 += 1
        
    for i in new_list:
        B[mulai] = i
        mulai += 1
        
    return B

def mergeSort(B):
    return merge_sort((0, len(B) - 1), B)

print(Daftar)
mergeSort(Daftar)
print(Daftar)
