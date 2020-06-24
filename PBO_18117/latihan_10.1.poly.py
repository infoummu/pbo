class Burung :
    def __init__(self,name,age):
        self.name = name
        self.age  = age

    def info(self):
        print(f"saya sekor burung bernama {self.name}. dan umur {self.age}")

    def gerak_cepat(self):
        print("Terbang")

class Singa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"saya seekor singa bernama {self.name}. dan umur {self.age}")

    def gerak_cepat(self):
        print("Berlari")

burung1 = Burung("leo" , 2.5)
singa1 = Singa ("sipu" , 4)

for animal in (burung1, singa1):
    animal.gerak_cepat()
    animal.info()
    animal.gerak_cepat()