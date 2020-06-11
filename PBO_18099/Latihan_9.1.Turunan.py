#INHERITANCE (TURUNAN)

class Mahasiswa:
    nama = ""
    __kelas = ""
    jurusan = ""

    def __init__(self, nama, kelas, jurusan):
        self.nama = nama
        self.__kelas = kelas
        self.jurusan = jurusan

    def tampil(self):
        print("Nama     : ", self.nama)
        print("Kelas    : ", self.__kelas)
        print("Jurusan  : ", self.jurusan)
        print("===========================================================")

#Tambahan class baru (turunan dari kelas mahasiswa)

class Krs(Mahasiswa):

    def __init__(self, nama, kelas, jurusan, semester):
        super().__init__(nama, kelas, jurusan)
        self.semester = semester

    def matakuliah(self):
        matakuliah=[]
        tanya=input("Apakah Anda Ingin Menginput Matakuliah Ya|Tidak?")
        if tanya == "ya":
            a = input("Silahkan Masukkan Matakuliah : ")
            matakuliah.append(a)
            print("Matakuliah Berhasil Di Tambahkan!")
            print("Matakuliah Yang Di Ambil : ", matakuliah)
        else:
            print("Anda Tidak Menginput Matakuliah")
    
#Objek
siswa1 = Mahasiswa("Vivi","3","Sistem Informasi")
siswa2 = Krs("Eva","3","Jaringan","Semester4")

#Fungsi Tampil
print("Tampil Data Siswa 1",)
siswa1.tampil()
print("Tampil Data Siswa 2",)
siswa2.tampil()

#Atribut baru pada class krs : semester
print("Semester : ", siswa2.semester)
siswa2.matakuliah()