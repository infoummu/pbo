---
layout: post
title:  Kuliah PBO Info 3 & 4 - Pengenalan Class pada Python P7-II
author: Ikhwan Elyas
description: Fungsi Python 🐍 mengelompokkan kode untuk reusable dan organisasi yang lebih baik. Penting bagi mahasiswa untuk mempelajarinya agar dapat membuat program yang efisien dan terstruktur..
---


Selamat datang di modul praktikum 7! Kali ini kita akan belajar tentang dua konsep penting dalam Pemrograman Berorientasi Objek (PBO) di Python: **Class** dan **Fungsi**. Kita akan lihat apa itu, bagaimana cara menggunakannya, dan apa perbedaannya.

## 1. Fungsi (Function)

Bayangkan kamu punya beberapa langkah yang sering kamu lakukan berulang-ulang. Daripada menulis langkah-langkah itu terus-menerus, kamu bisa membungkusnya dalam sebuah "fungsi". Fungsi adalah blok kode yang bisa kamu panggil kapan saja kamu butuhkan.

**Contoh Sederhana Fungsi:**

```python
def sapa_nama(nama):
    print(f"Halo, {nama}! Selamat belajar Python.")

# Memanggil fungsi
sapa_nama("Budi")
sapa_nama("Ani")
```

**Penjelasan:**
*   `def sapa_nama(nama):` : Ini adalah cara kita membuat fungsi. `sapa_nama` adalah nama fungsinya, dan `nama` adalah informasi yang kita berikan ke fungsi (disebut parameter).
*   `print(f"Halo, {nama}! Selamat belajar Python.")` : Ini adalah apa yang dilakukan fungsi ketika dipanggil.
*   `sapa_nama("Budi")` : Ini adalah cara kita "memanggil" atau menjalankan fungsi `sapa_nama` dengan memberikan nilai "Budi" untuk `nama`.

**Kapan menggunakan fungsi?**
*   Ketika kamu punya kode yang berulang.
*   Ketika kamu ingin memecah program menjadi bagian-bagian kecil yang lebih mudah diatur.

## 2. Class

Sekarang, bayangkan kamu ingin membuat banyak "benda" yang punya sifat dan perilaku yang mirip. Misalnya, kamu ingin membuat banyak objek "Mahasiswa". Setiap mahasiswa punya nama, NIM, dan bisa melakukan hal-hal seperti "belajar" atau "mengerjakan tugas".

Nah, **Class** itu seperti "cetakan" atau "blueprint" untuk membuat objek-objek tersebut. Dari satu cetakan `Mahasiswa`, kamu bisa membuat banyak objek mahasiswa yang berbeda.

**Contoh Sederhana Class:**

```python
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        print(f"Objek Mahasiswa {self.nama} dibuat!")

    def belajar(self):
        print(f"{self.nama} sedang belajar.")

    def kerjakan_tugas(self, mata_kuliah):
        print(f"{self.nama} sedang mengerjakan tugas {mata_kuliah}.")

# Membuat objek (instance) dari class Mahasiswa
mahasiswa1 = Mahasiswa("Andi", "12345")
mahasiswa2 = Mahasiswa("Siti", "67890")

# Mengakses sifat (atribut) objek
print(f"Nama Mahasiswa 1: {mahasiswa1.nama}")
print(f"NIM Mahasiswa 2: {mahasiswa2.nim}")

# Memanggil perilaku (metode) objek
mahasiswa1.belajar()
mahasiswa2.kerjakan_tugas("PBO")
```

**Penjelasan:**
*   `class Mahasiswa:` : Ini adalah cara kita membuat class. `Mahasiswa` adalah nama class-nya.
*   `def __init__(self, nama, nim):` : Ini adalah fungsi khusus yang akan otomatis dipanggil saat kamu membuat objek baru dari class `Mahasiswa`. Ini gunanya untuk "menginisialisasi" atau memberikan nilai awal pada objek. `self` itu merujuk pada objek itu sendiri.
*   `self.nama = nama` dan `self.nim = nim` : Ini adalah "sifat" atau "atribut" dari objek mahasiswa. Setiap objek mahasiswa akan punya `nama` dan `nim` masing-masing.
*   `def belajar(self):` dan `def kerjakan_tugas(self, mata_kuliah):` : Ini adalah "perilaku" atau "metode" yang bisa dilakukan oleh objek mahasiswa. Metode ini mirip fungsi, tapi dia "milik" sebuah objek.
*   `mahasiswa1 = Mahasiswa("Andi", "12345")` : Ini adalah cara kita membuat objek baru dari class `Mahasiswa`. `mahasiswa1` adalah objeknya.
*   `mahasiswa1.nama` : Cara mengakses atribut `nama` dari objek `mahasiswa1`.
*   `mahasiswa1.belajar()` : Cara memanggil metode `belajar` dari objek `mahasiswa1`.

**Kapan menggunakan class?**
*   Ketika kamu ingin membuat banyak objek yang punya sifat dan perilaku yang sama.
*   Ketika kamu ingin mengorganisir kode yang berhubungan dengan satu jenis "benda" tertentu.

## 3. Perbedaan Utama Class dan Fungsi

| Fitur           | Fungsi (Function)                               | Class                                                              |
| :-------------- | :---------------------------------------------- | :----------------------------------------------------------------- |
| **Tujuan**      | Melakukan serangkaian tugas tertentu.           | Membuat "cetakan" untuk objek yang punya sifat dan perilaku.       |
| **Organisasi**  | Blok kode yang berdiri sendiri.                  | Mengelompokkan data (atribut) dan perilaku (metode) menjadi satu. |
| **Output**      | Menjalankan kode dan bisa mengembalikan nilai. | Membuat objek (instance) baru.                                     |
| **Konsep PBO**  | Bukan inti PBO, tapi bagian dari program.       | Inti dari PBO (Object-Oriented Programming).                       |
| **`self`**      | Tidak ada (kecuali jika fungsi adalah metode). | Selalu ada di metode untuk merujuk pada objek itu sendiri.         |

**Analogi Sederhana:**

*   **Fungsi** itu seperti resep masakan. Kamu bisa mengikuti resepnya untuk membuat makanan.
*   **Class** itu seperti cetakan kue. Dari satu cetakan, kamu bisa membuat banyak kue yang bentuknya sama, tapi mungkin rasanya atau hiasannya berbeda.

Semoga modul ini membantu kamu memahami perbedaan antara fungsi dan class di Python! Selamat mencoba dan bereksperimen dengan kode-kode di atas.