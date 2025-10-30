---
layout: post
title:  Kuliah PBO Info 3 & 4 - Percabangan dan Perulangan dalam Python
author: Ikhwan Elyas
description: Pertemuan ini membahas konsep dasar percabangan (struktur kondisi) dan perulangan (looping) dalam bahasa Python. Mahasiswa akan belajar bagaimana komputer membuat keputusan berdasarkan kondisi tertentu serta mengulangi proses secara efisien menggunakan berbagai bentuk loop. Contoh kode diberikan agar mahasiswa dapat memahami logika program dan menerapkannya dalam kasus nyata seperti perhitungan, validasi data, dan pengulangan proses otomatis.
---

### # Tugas: Lakukan Praktikum Mandiri 
#### * **Panduan Menyimpan dan Menjalankan Program Python**
1. Buka **Visual Studio Code** atau **Text Editor** favorit Anda.  
2. Buat file baru di folder kerja Anda dengan nama:  
   **`praktikum5_percabangan_24001.py`**:   
3. Simpan file tersebut di folder kerja, misalnya:  
   `/home/namauser/pbo/`
   atau kalau di Windows:
   `Documents\PBO-24001\`
4. Untuk menjalankan program, buka **Terminal** atau **CMD**, lalu ketik perintah:

    ```bash
    python3 praktikum5_percabangan_24001.py
    ```

#### * **Arahan Praktikum Mandiri** 
1. Buat File Baru sesuai arahan sebelumnya
2. Simpan dengan Nama : **`praktikum5_percabangan_24001.py`**, sesuaikan npm dengan npm anda (**`24001`**)
3. `Copy` dan `Paste` code `contoh 1` ke editor, setelah itu simpan dan jalankan
4. Setelah itu lanjutkan sampai contoh 14, beri `batas` antara code contoh 1 dan seterusnya dengan batas `garis` dengan perintah: `print("-" * 25)`

    ```python
    # Contoh 1: 
    # Isi/copy-paste code contoh 1 dibawah:


    # Batas, berikutnya Contoh 2:
    print("-" * 25)


    # Batas, berikutnya Contoh 3:
    print("-" * 25)


    # dan seterusnya ...
    ```
5. Lakukan Bertahap satu per satu, setiap Contoh lakukan percobaan dijalankan agar anda paham apa yang dilakukan oleh code tersebut.
6. Setelah Selesai sampai `Contoh 14`, dan `berhasil` jalan tanpa `error`, silahkan `Absen` dan `Upload` file praktikum anda ke link berikut: **[[Absen dan Upload](https://pbo.tifor.site/){:target="_blank"}]**


### 1 Percabangan (Conditional Statements)

Percabangan adalah struktur logika untuk menjalankan bagian kode tertentu berdasarkan kondisi yang benar (True) atau salah (False).
Python menggunakan kata kunci if, elif, dan else.

Struktur umum:
```python
if kondisi1:
    # blok kode jika kondisi1 benar
elif kondisi2:
    # blok kode jika kondisi2 benar
else:
    # blok kode jika semua kondisi salah
```
**Contoh 1**:
```python
nilai = 75

if nilai >= 90:
    print("Nilai A")
elif nilai >= 75:
    print("Nilai B")
elif nilai >= 60:
    print("Nilai C")
else:
    print("Nilai D")
```

Penjelasan:
Python akan memeriksa kondisi dari atas ke bawah dan mengeksekusi blok pertama yang bernilai benar.


### 2 Percabangan Bersarang (Nested If)

Kadang kondisi membutuhkan pengecekan di dalam kondisi lain.
Struktur ini disebut nested if.

**Contoh 2**:
```python
umur = 20
status = "mahasiswa"

if umur >= 18:
    if status == "mahasiswa":
        print("Anda dewasa dan seorang mahasiswa")
    else:
        print("Anda dewasa tapi bukan mahasiswa")
else:
    print("Anda belum dewasa")
```

### 3 Percabangan Sederhana (Single If)

Jika hanya ada satu kondisi tanpa else, gunakan if tunggal.

**Contoh 3**:
```python
x = 10
if x > 5:
    print("x lebih besar dari 5")
```

### 4 Operator Logika dalam Percabangan

Gunakan and, or, not untuk membuat kondisi lebih kompleks.

**Contoh 4:**
```python
umur = 22
izin = True

if umur >= 18 and izin:
    print("Boleh masuk")
else:
    print("Tidak boleh masuk")
```

## PERULANGAN (LOOPING)
### 1 Pengertian

Perulangan digunakan untuk mengeksekusi blok kode berulang kali selama kondisi tertentu masih terpenuhi.
Python memiliki dua jenis utama perulangan: for dan while.

### 2 Perulangan for

Digunakan untuk mengulang setiap elemen dari koleksi (seperti list, string, atau range).

Menggunakan `range()`:

**Contoh 5:** 
```python
for i in range(5):
    print("Iterasi ke-", i)
```

**Output:**

    Iterasi ke-0
    Iterasi ke-1
    Iterasi ke-2
    Iterasi ke-3
    Iterasi ke-4

Mengakses elemen `list`:

**Contoh 6:** 
```python
buah = ["apel", "pisang", "jeruk"]
for item in buah:
    print("Saya suka", item)
```

### 3 Perulangan while

Digunakan ketika kita ingin mengulang selama kondisi benar (True).

**Contoh 7:**
```python
angka = 1
while angka <= 5:
    print("Angka:", angka)
    angka += 1
```
### 4 Perulangan Bersarang (Nested Loop)

Loop dapat diletakkan di dalam loop lainnya.

**Contoh 8:**
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)
```
### 5 Pernyataan break, continue, dan pass

**break**
Digunakan untuk menghentikan loop sebelum waktunya.

**Contoh 9:**
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

**continue**
Melewati iterasi saat ini dan lanjut ke iterasi berikutnya.

**Contoh 10:**
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

**pass**
Digunakan sebagai placeholder (tidak melakukan apa pun).

**Contoh 11:**
```python
for i in range(3):
    pass  # digunakan ketika blok kode belum diisi
```

### 6 Perulangan dengan else

Blok else akan dieksekusi jika loop berakhir tanpa break.

**Contoh 12:**
```python
for i in range(5):
    print(i)
else:
    print("Loop selesai tanpa break")
```

### 7 Kombinasi Percabangan dan Perulangan

Kedua struktur ini sering digunakan bersamaan untuk membuat program dinamis.

**Contoh 13:**
```python
for i in range(1, 6):
    if i % 2 == 0:
        print(i, "adalah bilangan genap")
    else:
        print(i, "adalah bilangan ganjil")
```

### 8 Studi Kasus: Program Login Sederhana

Contoh penerapan percabangan dan perulangan bersama.

**Contoh 14:**
```python
password_benar = "python123"
percobaan = 0

while percobaan < 3:
    pwd = input("Masukkan password: ")
    if pwd == password_benar:
        print("Login berhasil!")
        break
    else:
        print("Password salah.")
        percobaan += 1
else:
    print("Akses ditolak. Terlalu banyak percobaan.")
```

---
By : Elyas@fedora.linux