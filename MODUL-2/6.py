class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'

    def __init__(self, nama):
        self.nama = nama

    def ucapkanSalam(self):
        print('Salam, namaku', self.nama)

    def makan(self,s):
        print('Saya baru akan makan', s)
        self.keadaan = 'kenyang'

    def olaharaga(self, k):
        print('saya baru saja latihan', k)
        self.keadaan = 'lapar'

    def mengalikandenganDua(self, n):
        return n*2

class SiswaSMA(Manusia):
    def __init__(self, nama, umur, alamat, uj):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        self.uangJajan = uj

    def __str__(self):
        n = self.nama + ', umurnya ' + str(self.umur) \
            + '. alamatnya di ' + self.alamat \
            + '. uang jajannya sebanyak Rp. ' + str(self.uangJajan)\
            + '. tiap harinya.'
        return n

    def ambilNama(self):
        return self.nama

    def ambilUmur(self):
        return self.umur

    def ambilAlamat(self):
        return self.alamat

    def perbaruiAlamat(self, kota):
        self.alamat = kota

    def ambilUangJajan(self):
        return self.uj

    def kuranginUangJajan(self, uang):
        self.uangJajan -= uang
