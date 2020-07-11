#INHERITANCE(TURUNAN)
class mahasiswa:
  nama=""
  _kelas=""
  jurusan=""

  def _init_(self,nama,kelas,jurusan):
    self.nama=nama
    self._kelas=kelas
    self.jurusan =jurusan

  def tampil(self):
    print("Nama      :",self.nama)
    print("Kelas    :",self._kelas)
    print("Jurusan   :",self.jurusan)
    print("===============================")

#tambahan class baru (turunan dari kelas mahasiswa)
class Krs(mahasiswa):

 def _init_(self,nama,kelas,jurusan,semester):
  super()._init_(nama,kelas,jurusan)
  self.semster=semster

 def matakuliah(self):
   matakuliah=[]
   tanya=input("apakah anda ingin menginput matakuliah ya|tidak?")
   if tanya=="ya":
      a=input("silahkan masukan matakuliah:")
      matakuliah.append(a)
      print("Matakuliah Berhasil ditambahkan!")
      print("matakuliah yang diambil:",matakuliah)
   else:
      print("anda tidak menginput matakuliah")

#objeK
mahasiswa1=mahasiswa("Nina","3","Sistem Informasi")
mahasiswa2=Krs("Kartika","3","Jaringan","Semester 4")

#fungsi tampil
print("Tampil Data mahasiswa I",)
mahasiswa1.tampil()
print("Tampil Data mahasiswa II",)
mahasiswa2.tampil()

#atribut baru pada class krs:semester
print("Semester:",mahasiswa2.semester)
mahasiswa2.matakuliah()
