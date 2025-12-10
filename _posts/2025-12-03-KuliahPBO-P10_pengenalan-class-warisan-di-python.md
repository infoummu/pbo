---
layout: post
title:  Kuliah PBO Info 3 & 4 - Lanjutan Class Inheritance (Pewarisan) P10
author: Ikhwan Elyas
description: Inheritance atau "pewarisan" adalah mekanisme di mana sebuah class dapat mewarisi atribut dan metode dari class lain. Konsep ini digunakan untuk menghindari duplikasi kode dan mempermudah pengembangan program.
---




## Class Inheritance 

Dalam Pemrograman Berorientasi Objek (PBO), *Inheritance* atau
**pewarisan** adalah mekanisme di mana sebuah class dapat mewarisi
atribut dan metode dari class lain. Konsep ini digunakan untuk
menghindari duplikasi kode dan mempermudah pengembangan program.

Class yang mewariskan disebut **Parent Class (Superclass)**, sedangkan
class yang menerima warisan disebut **Child Class (Subclass)**.

------------------------------------------------------------------------

## 2. Konsep Dasar Inheritance

### a. Tujuan Inheritance

-   Mengurangi duplikasi kode
-   Mempermudah pengembangan program
-   Meningkatkan keteraturan struktur program
-   Memudahkan pengembangan lanjutan

### b. Ilustrasi Sederhana

Misalnya: - Class `Hewan` memiliki sifat `nama` dan metode `makan()`. -
Class `Kucing` mewarisi `Hewan`, sehingga `Kucing` otomatis memiliki
`nama` dan `makan()`.

------------------------------------------------------------------------

## 3. Sintaks Inheritance dalam Python

``` python
class Parent:
    pass

class Child(Parent):
    pass
```

Contoh nyata:

``` python
class Hewan:
    def makan(self):
        print("Hewan sedang makan")

class Kucing(Hewan):
    def suara(self):
        print("Meong")
```

Penggunaan:

``` python
k = Kucing()
k.makan()
k.suara()
```

------------------------------------------------------------------------

## 4. Pewarisan Atribut dan Method

``` python
class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

    def info(self):
        print("Merk kendaraan:", self.merk)

class Motor(Kendaraan):
    def jalan(self):
        print("Motor berjalan")

m = Motor("Honda")
m.info()
m.jalan()
```

------------------------------------------------------------------------

## 5. Method Overriding

Method overriding adalah teknik mengganti method dari parent class di
child class.

``` python
class Hewan:
    def suara(self):
        print("Suara hewan")

class Anjing(Hewan):
    def suara(self):
        print("Guk guk")

a = Anjing()
a.suara()
```

------------------------------------------------------------------------

## 6. Penggunaan super()

`super()` digunakan untuk memanggil method dari parent class.

``` python
class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

class Mobil(Kendaraan):
    def __init__(self, merk, warna):
        super().__init__(merk)
        self.warna = warna

m = Mobil("Toyota", "Merah")
print(m.merk)
print(m.warna)
```

------------------------------------------------------------------------

## 7. Jenis-Jenis Inheritance

1.  **Single Inheritance**
2.  **Multiple Inheritance**
3.  **Multilevel Inheritance**
4.  **Hierarchical Inheritance**

Contoh Multiple Inheritance:

``` python
class A:
    def metodeA(self):
        print("Ini dari class A")

class B:
    def metodeB(self):
        print("Ini dari class B")

class C(A, B):
    pass

obj = C()
obj.metodeA()
obj.metodeB()
```

------------------------------------------------------------------------


## 8. Kesimpulan

Inheritance mempermudah pengelolaan kode, meningkatkan efisiensi, dan
membantu pengembangan aplikasi skala besar.

