#INHERITANCE (TURUNAN)
class Mahasiswa:
    Nama=""
    __kelas=""
	jurusan=""

    def __init__(self, nama, kelas,jurusan):
	  self.nama =nama
	  self.__kelas =kelas
	  self.jurusan =jurusan
		
    def tampil(self):
	  print("Nama	  :",self.nama)
	  print("Kelas   :",self.__kelas)
	  print("Jurusan  :",self.jurusan)
	  print("====================================")

#tambahan class baru (turunan dari kelas mahasiswa)
class Krs(Mahasiswa):

    def __init__(self, nama, kelas, jurusan, semester):
	  super().__init__(nama, kelas,jurusan)
	  self.semester=semester
	  
    def matakuliah(self):
	  matakuliah=[]
	  tanya=input("apakah anda ingin menginput matakuliah ya|tidak?")
	  if tanya == "iya":
		  a=input("silakan masukan matakuliah: ")
		  matakuliah.append(a)
		  print("Matakuliah Berhasil di tambahkan!")
		  print("matakulia yang di ambil:",matakuliah)
		else:
		  print("anda tidak menginput matakuliah")

#objeK
siswa1=Mahasiswa("Nina","3","Sistem Informasi")
siswa2=Krs("Kartika","3","Jaringan","semester 4")


#fungsi tampil
print("Tampil Data Siswa I", )
siswa1.tampil()	
print("Tampil Data Siswa II", )
siswa2.tampil()	

#atribut baru pada class krs : semester
print("Semester:",siswa2.semester)
siswa2.matakuliah()
