---
layout: post
title:  Kuliah PBO Info 3 & 4 - Pengenalan Class pada Python P7
author: Ikhwan Elyas
description: Selamat datang di modul praktikum ke-7! Kali ini kita akan belajar salah satu konsep paling penting dalam Pemrograman Berorientasi Objek (PBO) yaitu **Class** di Python.
---


Selamat datang di modul praktikum ke-7! Kali ini kita akan belajar salah satu konsep paling penting dalam Pemrograman Berorientasi Objek (PBO) yaitu **Class** di Python. 

## Apa itu Class?

Bayangkan kamu ingin membuat banyak objek yang punya karakteristik dan perilaku yang sama. Misalnya, kamu ingin membuat banyak objek "Kucing". Setiap kucing punya nama, warna, dan bisa mengeong. Daripada membuat setiap kucing satu per satu dengan menulis ulang semua karakteristiknya, kita bisa membuat sebuah "cetakan" atau "blueprint" yang disebut **Class**.

Jadi, **Class adalah cetakan atau rancangan untuk membuat objek.**

Dari satu cetakan `Class Kucing`, kita bisa membuat banyak objek kucing yang berbeda-beda (Kucing A, Kucing B, dst.), tapi semuanya punya karakteristik dasar yang sama (nama, warna, bisa mengeong).

## Bagian-bagian Class

Sebuah Class biasanya punya dua hal utama:

1.  **Atribut (Attributes):** Ini adalah karakteristik atau sifat dari objek. Contoh: nama kucing, warna kucing.
2.  **Metode (Methods):** Ini adalah perilaku atau aksi yang bisa dilakukan objek. Contoh: kucing bisa mengeong, kucing bisa tidur.

## Cara Membuat Class di Python

Kita akan membuat Class `Kucing` sebagai contoh, simpan dengan nama file **`praktikum7_class.py`**.

```python
class Kucing:
    # Ini adalah metode khusus yang akan dipanggil saat objek baru dibuat
    def __init__(self, nama, warna):
        self.nama = nama  # Atribut nama
        self.warna = warna # Atribut warna
        print(f"Seekor kucing baru bernama {self.nama} telah lahir!")

    # Ini adalah metode (perilaku) dari objek Kucing
    def mengeong(self):
        print(f"{self.nama} sedang mengeong: Meow! Meow!")

    def tidur(self):
        print(f"{self.nama} sedang tidur... Zzzzz...")

    def info(self):
        print(f"Nama: {self.nama}, Warna: {self.warna}")
```

**Penjelasan Kode:**

*   `class Kucing:`: Ini cara kita mendeklarasikan sebuah class bernama `Kucing`.
*   `def __init__(self, nama, warna):`: Ini adalah metode spesial yang disebut **konstruktor**. Metode ini akan otomatis dipanggil setiap kali kita membuat objek baru dari class `Kucing`. 
    *   `self`: Ini adalah parameter wajib pertama di setiap metode dalam class. `self` merujuk pada objek itu sendiri. Kamu bisa membayangkan `self` sebagai "aku" atau "diriku sendiri" dari objek yang sedang dibuat.
    *   `nama` dan `warna`: Ini adalah parameter yang kita berikan saat membuat objek, misalnya nama kucingnya "Kitty" dan warnanya "putih".
    *   `self.nama = nama`: Ini artinya kita menyimpan nilai `nama` yang diberikan ke dalam atribut `nama` milik objek ini.
*   `def mengeong(self):`, `def tidur(self):`, `def info(self):`: Ini adalah metode-metode biasa yang mendefinisikan perilaku objek `Kucing`. Mereka juga punya parameter `self`.

## Cara Membuat Objek (Instance) dari Class

Setelah punya cetakan `Kucing`, sekarang kita bisa membuat objek-objek kucing yang nyata!

```python
# Membuat objek kucing pertama
kucing1 = Kucing("Kitty", "Putih")

# Membuat objek kucing kedua
kucing2 = Kucing("Milo", "Oren")

# Membuat objek kucing ketiga
kucing3 = Kucing("Blacky", "Hitam")
```

Setiap kali kita memanggil `Kucing("nama", "warna")`, kita sedang membuat sebuah objek baru dari class `Kucing`. Objek ini sering disebut juga **instance**.

## Mengakses Atribut dan Memanggil Metode Objek

Kita bisa mengakses atribut dan memanggil metode dari objek menggunakan tanda titik (`.`).

```python
print("\n--- Informasi Kucing ---")
kucing1.info() # Memanggil metode info dari kucing1
kucing2.info()
kucing3.info()

print("\n--- Aksi Kucing ---")
kucing1.mengeong() # Memanggil metode mengeong dari kucing1
kucing2.tidur()
kucing3.mengeong()

# Mengakses atribut secara langsung
print(f"Warna {kucing1.nama} adalah {kucing1.warna}")
print(f"Nama kucing kedua adalah {kucing2.nama}")
```

**Output yang diharapkan:**

```
Seekor kucing baru bernama Kitty telah lahir!
Seekor kucing baru bernama Milo telah lahir!
Seekor kucing baru bernama Blacky telah lahir!

--- Informasi Kucing ---
Nama: Kitty, Warna: Putih
Nama: Milo, Warna: Oren
Nama: Blacky, Warna: Hitam

--- Aksi Kucing ---
Kitty sedang mengeong: Meow! Meow!
Milo sedang tidur... Zzzzz...
Blacky sedang mengeong: Meow! Meow!
Warna Kitty adalah Putih
Nama kucing kedua adalah Milo
```

## Latihan Praktikum

Sekarang giliran kamu! Buatlah sebuah class baru dengan nama `Mobil`.

**Class `Mobil` harus memiliki:**

1.  **Atribut:**
    *   `merk` (contoh: "Toyota", "Honda")
    *   `warna` (contoh: "Merah", "Biru")
    *   `tahun_produksi` (contoh: 2020, 2023)
2.  **Metode:**
    *   `nyalakan_mesin()`: Mencetak pesan "Mobil [merk] warna [warna] tahun [tahun_produksi] mesinnya menyala! Vroom vroom!"
    *   `matikan_mesin()`: Mencetak pesan "Mobil [merk] mesinnya mati."
    *   `info_mobil()`: Mencetak semua informasi mobil (merk, warna, tahun produksi).

**Setelah membuat class `Mobil`:**

1.  Buatlah 3 objek mobil yang berbeda (misalnya `mobil1`, `mobil2`, `mobil3`) dengan merk, warna, dan tahun produksi yang berbeda. 
2.  Panggil metode `info_mobil()` untuk setiap objek mobil.
3.  Panggil metode `nyalakan_mesin()` untuk `mobil1`.
4.  Panggil metode `matikan_mesin()` untuk `mobil2`.

Selamat mengerjakan! Jika ada pertanyaan, jangan ragu bertanya kepada asisten praktikummu.


---
By : Elyas@fedora.linux