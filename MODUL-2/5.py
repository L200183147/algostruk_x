class Mahasiswa(object):
    """Class Mahasiswa yang dibangun dari class Manusia"""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi inisiasi di class manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.listKuliah = []

    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp. ' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return s

    def ambilNama(self):
        return self.nama

    def ambilNIM(self):
        return self.NIM
    
    def ambilUangSaku (self):
        return self.uangSaku
    
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau makan sambil belajar,"""
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan = 'kenyang'
        
    def ambilKotaTinggal(self):
        return self.kotaTinggal

    def perbaruiKotaTinggal (self, kotaBaru):
        self.kota = kotaBaru

    def tambahUangSaku (self, uangBaru):
        self.uangSaku += uangBaru

    def listKuliah(self):
        return self.listKuliah

    def ambilKuliah(self, matkul):
        self.listKuliah.append(matkul)

    def hapusKuliah(self, matkul):
        self.listKuliah.remove(matkul)
            
