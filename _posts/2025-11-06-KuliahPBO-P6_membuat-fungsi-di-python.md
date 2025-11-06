---
layout: post
title:  Kuliah PBO Info 3 & 4 - Membuat Function pada Python P6
author: Ikhwan Elyas
description: Fungsi Python 🐍 mengelompokkan kode untuk reusable dan organisasi yang lebih baik. Penting bagi mahasiswa untuk mempelajarinya agar dapat membuat program yang efisien dan terstruktur..
---

Pada modul dan pertemuan ini, kita akan belajar tentang "Function" dalam bahasa pemrograman Python. Function adalah blok kode yang dirancang untuk melakukan tugas tertentu. Dengan menggunakan function, kode kita akan menjadi lebih rapi, mudah dibaca, dan bisa digunakan berulang kali.

### * **Arahan Praktikum** 
1. Buat File Baru sesuai arahan sebelumnya
2. Simpan dengan Nama : **`praktikum6_fungsi_24001.py`**, sesuaikan npm dengan npm anda (**`24001`**)
3. `Copy` dan `Paste` code `contoh fungsi 1` ke editor, setelah itu simpan dan jalankan
4. Setelah itu lanjutkan sampai Contoh fungsi 9, beri `batas` antara code contoh fungsi 1 dan seterusnya dengan batas `garis` dengan perintah: `print("-" * 25)`

    ```python
    # Contoh fungsi 1: 
    # Isi/copy-paste code contoh 1 dibawah:


    # Batas, berikutnya Contoh fungsi 2:
    print("-" * 25)


    # Batas, berikutnya Contoh fungsi 3:
    print("-" * 25)


    # dan seterusnya ...
    ```
5. Lakukan Bertahap satu per satu, setiap Contoh lakukan percobaan dijalankan agar anda paham apa yang dilakukan oleh code tersebut.

### ** **Membuat Function**

Function adalah bagian penting dalam pemrograman. Bayangkan kamu punya resep masakan. Setiap langkah dalam resep itu bisa kita anggap sebagai bagian dari function. Function membantu kita mengelompokkan langkah-langkah yang berhubungan menjadi satu kesatuan.

#### 1 Pengenalan Function Tanpa "return"

Function tanpa `return` adalah function yang hanya melakukan sesuatu, tapi tidak mengembalikan nilai apapun setelah selesai. Contohnya seperti menyapa seseorang.

**Contoh Fungsi 1:**
```python
def sapa_nama(nama):
    print(f"Halo, {nama}! Selamat datang.")

sapa_nama("Budi")
sapa_nama("Ani")
```

**Penjelasan:**
- `def sapa_nama(nama):` adalah cara kita membuat function. `sapa_nama` adalah nama function, dan `nama` adalah informasi yang kita berikan ke function (disebut parameter).
- `print(f"Halo, {nama}! Selamat datang.")` adalah apa yang dilakukan function ini.
- `sapa_nama("Budi")` adalah cara kita memanggil atau menjalankan function ini.

#### 2 Function yang Menggunakan "return"

Function yang menggunakan `return` akan mengembalikan sebuah nilai setelah selesai melakukan tugasnya. Nilai ini bisa kita simpan di variabel atau langsung kita gunakan. Contohnya seperti menghitung penjumlahan.

**Contoh Fungsi 2:**
```python
def tambah(angka1, angka2):
    hasil = angka1 + angka2
    return hasil

angka_pertama = 5
angka_kedua = 3
jumlah = tambah(angka_pertama, angka_kedua)
print(f"Hasil penjumlahan: {jumlah}")

print(f"Hasil 10 + 7 adalah: {tambah(10, 7)}") # Bisa langsung digunakan
```

**Penjelasan:**
- `return hasil` berarti function ini akan memberikan nilai dari variabel `hasil` kembali ke tempat function dipanggil.
- Kita bisa menyimpan nilai yang dikembalikan ke dalam variabel `jumlah`.

#### 3 Default Argument pada Python

Default argument adalah nilai bawaan yang akan digunakan oleh parameter function jika kita tidak memberikan nilai saat memanggil function tersebut. Ini sangat berguna untuk membuat function lebih fleksibel.

**Contoh Fungsi 3:**
```python
def sapa_kota(nama, kota="Jakarta"):
    print(f"Halo, {nama}! Kamu berasal dari {kota}.")

sapa_kota("Andi") # Menggunakan nilai default "Jakarta"
sapa_kota("Siti", "Surabaya") # Menggunakan nilai yang diberikan "Surabaya"
```

**Penjelasan:**
- `kota="Jakarta"` berarti jika kita tidak mengisi `kota` saat memanggil `sapa_kota`, maka `kota` akan otomatis bernilai "Jakarta".

#### 4 Variable-length Argument pada Python (*args)

Kadang kita tidak tahu berapa banyak argumen yang akan diberikan ke function. Dengan `*args`, kita bisa menerima banyak argumen dan function akan menganggapnya sebagai sebuah tuple (kumpulan data yang tidak bisa diubah).

**Contoh Fungsi 4:**
```python
def total_belanja(*harga_barang):
    total = 0
    for harga in harga_barang:
        total += harga
    return total

print(f"Total belanja 1: {total_belanja(10000, 5000, 2000)}") # 3 argumen
print(f"Total belanja 2: {total_belanja(15000, 25000)}") # 2 argumen
print(f"Total belanja 3: {total_belanja(50000)}") # 1 argumen
```

**Penjelasan:**
- `*harga_barang` akan mengumpulkan semua angka yang diberikan menjadi sebuah tuple bernama `harga_barang`.

#### 5 Keyword Argument pada Function

Keyword argument adalah cara memanggil function dengan menyebutkan nama parameternya secara langsung. Ini membuat kode lebih jelas, terutama jika function punya banyak parameter.

**Contoh Fungsi 5:**
```python
def buat_pesan(penerima, isi_pesan, pengirim):
    print(f"Dari: {pengirim}")
    print(f"Untuk: {penerima}")
    print(f"Pesan: {isi_pesan}")

buat_pesan(pengirim="Admin", penerima="Pengguna", isi_pesan="Selamat datang di aplikasi kami!")
buat_pesan(isi_pesan="Ada promo menarik!", penerima="Pelanggan Setia", pengirim="Marketing")
```

**Penjelasan:**
- Kita bisa memanggil function dengan urutan parameter yang berbeda asalkan kita menyebutkan nama parameternya.

#### 6 Keyword-length Argument pada Function (**kwargs)

Mirip dengan `*args`, tapi `**kwargs` digunakan untuk menerima argumen dalam bentuk pasangan `key=value` (seperti kamus atau dictionary). Ini berguna jika kita ingin memberikan informasi tambahan yang tidak terstruktur ke function.

**Contoh Fungsi 6:**
```python
def info_pengguna(**data_tambahan):
    print("Informasi Pengguna:")
    for kunci, nilai in data_tambahan.items():
        print(f"- {kunci}: {nilai}")

info_pengguna(nama="Rina", usia=22, kota="Bandung")
info_pengguna(nama="Joko", pekerjaan="Programmer", status="Menikah", hobi="Membaca")
```

**Penjelasan:**
- `**data_tambahan` akan mengumpulkan semua argumen `key=value` menjadi sebuah dictionary bernama `data_tambahan`.

#### 7 Pass by Reference dan Pass by Value pada Python

Di Python, saat kita memberikan variabel ke function, sebenarnya yang diberikan adalah "referensi" ke objek tersebut. Ini berarti jika kita mengubah objek di dalam function, perubahan itu juga akan terlihat di luar function, terutama untuk tipe data yang bisa diubah (mutable) seperti list atau dictionary.

**Contoh 7, dengan tipe data mutable (list):**
```python
def tambah_elemen(daftar):
    daftar.append("Apel")
    print(f"Di dalam function: {daftar}")

buah = ["Mangga", "Jeruk"]
print(f"Sebelum function dipanggil: {buah}")
tambah_elemen(buah)
print(f"Setelah function dipanggil: {buah}")
```

**Penjelasan:**
- Karena `list` adalah mutable, perubahan di dalam function (`daftar.append("Apel")`) akan mempengaruhi `buah` di luar function.

**Contoh 8, dengan tipe data immutable (angka):**
```python
def ubah_angka(nilai):
    nilai = nilai + 10
    print(f"Di dalam function: {nilai}")

angka_saya = 5
print(f"Sebelum function dipanggil: {angka_saya}")
ubah_angka(angka_saya)
print(f"Setelah function dipanggil: {angka_saya}")
```

**Penjelasan:**
- Angka adalah immutable. Saat `nilai = nilai + 10` terjadi, sebenarnya `nilai` menunjuk ke objek angka baru, bukan mengubah objek angka_saya yang asli.

#### 8 Variable Scope pada Python

Variable scope adalah area di mana sebuah variabel bisa diakses. Ada dua jenis scope utama:
- **Global Scope:** Variabel yang dibuat di luar function bisa diakses di mana saja (di dalam atau di luar function).
- **Local Scope:** Variabel yang dibuat di dalam function hanya bisa diakses di dalam function itu saja.

**Contoh Fungsi 9, Variabel Locak dan Global:**
```python
# Global Scope
nama_global = "Dunia"

def sapa_dunia():
    # Bisa mengakses nama_global
    print(f"Halo dari function, {nama_global}!")

    # Local Scope
    pesan_lokal = "Ini pesan lokal"
    print(pesan_lokal)

sapa_dunia()
print(f"Halo dari luar function, {nama_global}!")

# Akan error jika mencoba mengakses pesan_lokal di sini
# print(pesan_lokal)
```

**Penjelasan:**
- `nama_global` bisa diakses di mana saja.
- `pesan_lokal` hanya bisa diakses di dalam function `sapa_dunia()`.

---
By : Elyas@fedora.linux