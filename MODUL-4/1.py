#1
class Mahasiswa(object):
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
 
    def __str__ (self):
        s = self.nama + ", NIM " + str(self.NIM)\
            + ", tinggal di " + self.kotaTinggal\
            + ", uang saku " + str(self.uangSaku)\
            + " tiap bulannya"
        return s

    def ambilNama(self):
        return self.nama

    def ambilNIM(self):
        return self.NIM

    def ambilUangSaku(self):
        return self.uangSaku

    def makan(self, s):
        print("saya baru saja makan", s, "sambil belajar")
        self.keadaan = "kenyang"

    def ambilKotaTinggal(self):
        return self.kotaTinggal

    def perbaruiKotaTinggal(self, p):
        self.kotaTinggal = p

    def tambahUangSaku(self, k):
        self.uangSaku += k

class MhsTIF(Mahasiswa):
    def katakanPy(self):
        print("Python is cool")




#bikin object
c0 = MhsTIF("Ika", 10, "Sukoharjo", 240000)
c1 = MhsTIF("Budi", 51, "Sragen", 230000)
c2 = MhsTIF("Ahmad", 2, "Surakarta", 250000)
c3 = MhsTIF("Chandra", 18, "Surakarta", 235000)
c4 = MhsTIF("Eka", 4, "Boyolali", 240000)
c5 = MhsTIF("Fandi", 31, "Salatiga", 250000)
c6 = MhsTIF("Deni", 13, "Klaten", 245000)
c7 = MhsTIF("Galuh", 5, "Wonogiri", 245000)
c8 = MhsTIF("Janto", 23, "Klaten", 245000)
c9 = MhsTIF("Hasan", 64, "Karanganyar", 270000)
c10 = MhsTIF("Khalid", 29, "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#case
target = "Klaten"
list = []
for i in range (len(Daftar)) :
    if Daftar[i].kotaTinggal == target :
        list.append(i)
print("object dengan asal kota ", target, "berada pada index ke- ", list)
