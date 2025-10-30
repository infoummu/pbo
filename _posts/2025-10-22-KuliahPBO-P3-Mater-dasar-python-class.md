---
layout: post
title:  Kuliah PBO Info 3 & 4 - Basic of Python Class P3
author: Ikhwan Elyas
description: Pada pertemuan ke-2 mata kuliah Pemrograman Berorientasi Objek (PBO) ini, mahasiswa akan mempelajari konsep dasar tentang variabel dan berbagai tipe data di Python, termasuk list, string, tuple, dan dictionary. Selain itu akan dibahas juga penggunaan operator, ekspresi, dan aturan operasi dalam Python.
---

## Pertemuan 3 – Variabel dan Jenis Tipe Data

### Panduan Menyimpan dan Menjalankan Program Python

1. Buka **Visual Studio Code** atau **Text Editor** favorit Anda.  
2. Buat file baru dengan nama:  
   **`praktikum2_list_24001.py`**  
3. Simpan file tersebut di folder kerja, misalnya:  
   `/home/namauser/pbo/`
4. Untuk menjalankan program, buka **Terminal**, lalu ketik perintah:

```bash
python3 praktikum2_list_24001.py
```
atau jika menggunakan Windows:

```bash
#/perintah
py praktikum2_list_24001.py
```

### 2.1 Nilai dan Tipe Data
Nilai adalah representasi data yang diproses program, seperti angka atau teks.
Tipe data menentukan jenis nilai yang dapat disimpan dan operasi yang dapat dilakukan.
Python memiliki beberapa tipe data dasar seperti int (bilangan bulat), `float` (desimal), `str` (string/teks),` bool` (benar/salah).

Contoh kode:
```python
x = 10
y = 3.5
z = "Halo Dunia"
b = True

print(type(x), type(y), type(z), type(b))
```
Python secara otomatis mengenali tipe data tanpa deklarasi eksplisit.

### 2.2 Variabel
Variabel digunakan untuk menyimpan nilai dalam memori komputer.
Nama variabel bertindak sebagai label untuk data tertentu.
Dalam Python, Anda cukup menulis nama_variabel = nilai tanpa menentukan tipe datanya.

Contoh kode:
```python
nama = "Elyas"
umur = 20
nilai = 88.5
print("Nama:", nama, "Umur:", umur, "Nilai:", nilai)
```

### 2.3 Nama Variabel dan Kata Kunci
Nama variabel harus diawali huruf atau garis bawah _, tidak boleh diawali angka.
Python memiliki kata kunci khusus seperti if, for, while, yang tidak boleh dijadikan nama variabel.

Contoh kode:
```python

# Benar
_nama = "Ali"
umur1 = 19

# Salah (akan error)
# 1umur = 19
# for = "data"
```

### 2.4 Mengevaluasi Ekspresi
Ekspresi adalah kombinasi variabel, nilai, dan operator yang menghasilkan suatu nilai.
Python akan mengevaluasi ekspresi dari kiri ke kanan sesuai prioritas operator.

Contoh kode:
```python
a = 5
b = 2
hasil = a + b * 3
print("Hasil:", hasil)
```

Ekspresi di atas menghasilkan 11 karena perkalian dilakukan lebih dahulu.

### 2.5 Operator dan Operand
Operator adalah simbol yang digunakan untuk melakukan operasi pada operand (nilai/variabel).
Contohnya: +, -, *, /, //, %, **.

Contoh kode:
```python
x = 10
y = 3
print(x + y, x - y, x * y, x / y, x // y, x ** y)
```

### 2.6 Operator Logika
Digunakan untuk operasi boolean: and, or, not.
Biasanya digunakan dalam kondisi logika.

Contoh kode:
```python

a = True
b = False
print(a and b)
print(a or b)
print(not a)
```

### 2.7 Operator Modulus
Operator % digunakan untuk mendapatkan sisa hasil bagi.
Berguna dalam banyak logika, seperti menentukan bilangan ganjil/genap.

Contoh kode:
```python

x = 10
y = 3
print(x % y)   # hasil: 1
```
### 2.8 Aturan pada Operasi
Python mengikuti aturan prioritas operator (seperti matematika).
Urutan: kurung → pangkat → kali/bagi → tambah/kurang → logika.

Contoh kode:
```python

hasil = (2 + 3) * 4 ** 2
print(hasil)
```

### 2.9 Lists
List menyimpan kumpulan nilai dalam satu variabel.
List bersifat mutable (dapat diubah).

Contoh kode:
```python

buah = ["apel", "pisang", "jeruk"]
print(buah)
buah.append("mangga")
print(buah)
```

### 2.9.1 Fungsi del
del digunakan untuk menghapus elemen tertentu dari list.

Contoh kode:
```python

angka = [1, 2, 3, 4, 5]
del angka[2]
print(angka)
```


### 2.10 String
String adalah urutan karakter diapit tanda kutip.
Dapat diolah dengan operator + (gabung) atau * (ulang).

Contoh kode:
```python

teks = "Halo"
print(teks + " Dunia")
print(teks * 3)
```

### 2.11 Tuples
Tuple mirip list tetapi immutable (tidak dapat diubah).
Digunakan untuk data tetap.

Contoh kode:
```python

data = (10, 20, 30)
print(data)

# data[0] = 50  # Akan error
```

### 2.12 Dictionaries
Dictionary menyimpan data dalam pasangan key:value.
Sangat berguna untuk struktur data seperti data mahasiswa atau produk.

Contoh kode:
```python

mahasiswa = {"nama": "Ali", "umur": 20, "nilai": 85}
print(mahasiswa)
```

#### 2.12.1 Mengakses Dictionary
Akses data dengan menyebutkan key-nya.

```python

print(mahasiswa["nama"])
```

#### 2.12.2 Operasi pada Dictionary
Kita dapat menambah, menghapus, atau mengubah isi dictionary.

```python

mahasiswa["kelas"] = "PBO"
del mahasiswa["nilai"]
print(mahasiswa)
```

#### 2.12.3 Metode pada Dictionary
Beberapa metode umum: .keys(), .values(), .items()

```python

print(mahasiswa.keys())
print(mahasiswa.values())
print(mahasiswa.items())
```

#### 2.12.4 Alias dan Penggandaan
Jika dua variabel menunjuk ke dictionary yang sama, perubahan pada satu akan memengaruhi yang lain.

```python

a = {"x": 1, "y": 2}
b = a
b["x"] = 99
print(a)  # ikut berubah
```

Untuk menggandakan tanpa efek, gunakan .copy():

```python

c = a.copy()
c["y"] = 88
print(a, c)
```
