class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
        
    def cetakIni(self):
        print(self.teks)
        
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
        
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
        
    def jumKar(self):
        return len(self.teks)
    
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai', len(self.teks), 'karakter.')
        
    def perbarui(self, stringBaru):
        self.teks = stringBaru
        
    #a
    def apakahTerkandung(self,cari):
        if cari in self.teks:
            return True
        else:
            return False

    def cetakTeks(self):
        return self.teks

    #b
    def hitungKonsonan(self):
        vokal = 'aiueoAIUEO'
        c = 0
        for i in self.teks:
            if i not in vokal:
                c += 1
        return c
    
    #c
    def hitungVokal(self):
        vokal = 'aiueoAIUEO'
        c = 0
        for i in self.teks :
            if i in vokal:
                c += 1
        return c
