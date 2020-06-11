class Saya(object):
    def __init__(self, nama, tinggi, berat):
        self.nama = nama
        self.tinggi = tinggi
        self.berat = berat

    def berjalan(self):
        print("Berjalan ke depan")

    def berlari(self):
        print("Berlari dengan cepat")


#class Teman turunan dari class Saya
class Teman(Saya):
    pass


b = Saya("Viviyanti", 163, 57)
print()
print("Nama:", b.nama)
print("Tinggi:", b.tinggi, "cm")
print("Berat:", b.berat, "kg")
b.berjalan()
b.berlari()

#objek dari class Teman memiliki seluruh yang dimiliki class Saya
a = Teman("Evalovita", 158, 50)
print()
print("Nama:", a.nama)
print("Tinggi:", a.tinggi, "cm")
print("Berat:", a.berat, "kg")
a.berjalan()
a.berlari()