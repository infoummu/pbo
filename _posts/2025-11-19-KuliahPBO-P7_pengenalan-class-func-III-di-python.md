---
layout: post
title:  Kuliah PBO Info 3 & 4 - Pengenalan Class dan Fungsi pada Python P7-III
author: Ikhwan Elyas
description: Fungsi Python 🐍 mengelompokkan kode untuk reusable dan organisasi yang lebih baik. Penting bagi mahasiswa untuk mempelajarinya agar dapat membuat program yang efisien dan terstruktur.
---

Class adalah pondasi utama dalam Pemrograman Berorientasi Objek (PBO). Dengan memahami class, mahasiswa dapat membuat program yang lebih rapi, terstruktur, dan mudah dikembangkan.

Selain itu, modul ini juga membahas perbedaan antara class dan fungsi, sehingga mahasiswa dapat memahami kapan menggunakan class dan kapan cukup memakai fungsi.


- **Mata Kuliah:** Pemrograman Berorientasi Objek (PBO)
- **Topik:** Pengenalan Class di Python & Perbedaan Class dengan Fungsi
- **Semester:** 2
- **Bahasa Pemrograman:** Python

## Tujuan Praktikum

1. Mengerti apa itu `class` dan `object`
2. Bisa membuat class sederhana
3. Mengerti perbedaan antara fungsi biasa dengan `method` di dalam class
4. Bisa membuat object dari class

## Apa itu Class dan Object?

Bayangkan kamu mau membuat banyak karakter di game.
Kalau pakai fungsi biasa, kamu harus buat fungsi terpisah untuk setiap karakter → ribet!
Dengan `class`, kamu buat "cetakan” dulu, lalu bisa bikin banyak karakter dari cetakan itu.

*   `Class` = cetakan / blueprint
*   `Object` = benda yang dibuat dari cetakan itu

### Contoh:

```python
class Mahasiswa: # ini cetakannya (class)
    pass

budi = Mahasiswa() # ini object yang dibuat dari cetakan
ani = Mahasiswa() # ini object lain dari cetakan yang sama
```

## Bagian-Bagian Penting di Class

```python
class NamaClass:
    def __init__(self, parameter1, parameter2): # constructor, dipanggil otomatis saat bua
        self.nama = parameter1 # atribut / variabel di dalam object
        self.nim = parameter2

    def method_nama(self): # method = fungsi di dalam class
        print(f"Halo, saya {self.nama}")
```

`self` wajib ditulis di parameter pertama setiap method (artinya “object itu sendiri”).

## Praktikum 1: Class Mahasiswa Sederhana

Buat file `praktikum7_1.py`

```python
# Cetakan Mahasiswa
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama # atribut nama
        self.nim = nim # atribut nim

    def perkenalan(self):
        print(f"Hai! Nama saya {self.nama}, NIM saya {self.nim}")

# Membuat object (instansiasi)
m1 = Mahasiswa("Budi", "12345")
m2 = Mahasiswa("Siti", "67890")

# Memanggil method
m1.perkenalan()
m2.perkenalan()

# Mengakses atribut
print("NIM Budi:", m1.nim)
```

### Output yang diharapkan:

```text
Hai! Nama saya Budi, NIM saya 12345
Hai! Nama saya Siti, NIM saya 67890
NIM Budi: 12345
```

## Perbedaan Fungsi Biasa vs Method di Class

| Fungsi Biasa              | Method di Class                 |
| :------------------------ | :------------------------------ |
| Berdiri sendiri           | Harus ada di dalam class        |
| Dipanggil langsung: `cetak_nama()` | Dipanggil lewat object: `m1.perkenalan()` |
| Tidak punya `self`        | Selalu punya parameter `self`   |
| Tidak "ingat" data object | Bisa mengakses atribut object lewat `self` |

### Contoh fungsi biasa:

```python
def perkenalan(nama, nim):
    print(f"Nama saya {nama}, NIM {nim}")

perkenalan("Budi", "12345") # harus kasih data setiap kali panggil
```

Dengan class → data sudah “nyantol” di object, tidak perlu kirim ulang.

## Praktikum 2: Class Mobil (Latihan)

Buat file `praktikum7_2.py`

```python
class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
        self.kecepatan = 0

    def gas(self, tambah):
        self.kecepatan += tambah
        print(f"{self.merk} ngegas! Kecepatan sekarang {self.kecepatan} km/h")

    def rem(self, kurang):
        self.kecepatan -= kurang
        if self.kecepatan < 0:
            self.kecepatan = 0
        print(f"{self.merk} ngerem. Kecepatan sekarang {self.kecepatan} km/h")

# Membuat object mobil
mobilku = Mobil("Toyota", "Merah")
mobilmu = Mobil("Honda", "Hitam")
```

```python
mobilku.gas(50)
mobilku.gas(30)
mobilku.rem(20)

print(f"Warna mobilku: {mobilku.warna}")
```

Coba jalankan dan lihat hasilnya!

## Tugas Mandiri (Kerjakan di Rumah)

1.  Buat class `Kucing` yang punya atribut:
    *   nama
    *   umur
    *   warna_bulu
    Dan method:
    *   `meong()` → print "Meong! Nama saya ..."
    *   `info()` → tampilkan semua atribut
2.  Buat class `RekeningBank` yang punya:
    *   atribut: nama_pemilik, saldo
    *   method: `tambah_saldo(jumlah)`, `tarik_saldo(jumlah)`, `cek_saldo()`

Kirim file `.py` ke dosen paling lambat minggu depan.

## Kesimpulan Hari Ini

*   Class itu seperti cetakan untuk membuat object
*   Object adalah hasil jadi dari cetakan itu
*   Method itu fungsi yang "tahu” data object-nya karena ada `self`
*   Class membuat kode lebih rapi dan bisa dipakai berkali-kali

## Selamat mencoba!

Kalau ada yang bingung, tanya teman atau dosen ya! 😊

*   Penjelasan inheritance di class
*   Konsep encapsulation Python
*   Tambah visual diagram class