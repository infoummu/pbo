class Mahasiswa():
    nama=""
    __kelas=""
    jurusan=""
    def __init__(self, nama, kelas,jurusan):
           self.nama =nama
           self.__kelas = kelas
           self.jurusan = jurusan
    def tampil(self):
           print("Nama :", self.nama)
           print("Kelas :", self.__kelas)
           print("Jurusan :", self.jurusan)

siswa1 = Mahasiswa("diyana ","info 5", "sistem informasi")
siswa1.tampil()
#print("kelas : ", siswa1.kelas) 