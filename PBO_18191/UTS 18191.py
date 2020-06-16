class orang: 
    def __init__(self, npm, nama):
        self.np=npm
        self.nm=nama
    def tampilkan(self):
        print ("1:","satu")
        print ("2:","Dua")
        print ("3:","tiga")
        print ("0:","nol")
        print ("4:","empat")
        print ("5:","lima")
        print ("npm:", self.nm,"\nnama:", self.np)
class mahasiswa(orang):
    pass
 
orang=orang("haris senen", "18191")
orang.tampilkan()

