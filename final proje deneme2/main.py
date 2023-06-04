from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
#import pandas as pd

def main():

    insan1 = Insan("12345678910", "Ahmet", "Yılmaz", 30, "Erkek", "Türk")
    insan2 = Insan("98765432100", "Aliye", "Ata", 22, "Kadın", "Türk")
    print(insan1)
    print(insan2)
    issiz1 = Issiz("12345678910", "Ali", "Demir", 33, "Erkek", "Türk")
    issiz1.set_statu({"mavi yaka": 2, "beyaz yaka": 4, "yönetici": 6})
    issiz2 = Issiz("98765432100", "Veli", "Şen", 24, "Kadın", "Türk")
    issiz2.set_statu({"mavi yaka": 1, "beyaz yaka": 3, "yönetici": 5})
    issiz3 = Issiz("56789012345", "Ayşe", "Mutlu", 35, "Erkek", "Türk")
    issiz3.set_statu({"mavi yaka": 3, "beyaz yaka": 5, "yönetici": 7})
    print(issiz1)
    print(issiz2)
    print(issiz3)

    calisan1 = Calisan("12345678910", "Fatma", "Gür", 32, "Erkek", "Türk", "teknoloji", 10, 12000)
    calisan2 = Calisan("28765432100", "Aylin", "Kaya", 26, "Kadın", "Türk", "muhasebe", 2, 18000)
    calisan3 = Calisan("36789012345", "Elif", "Eren", 35, "Erkek", "Türk", "inşaat", 7, 25000)

    print(calisan1)
    print(calisan2)
    print(calisan3)
    mavi_yaka1 = MaviYaka("44545678910", "Bengü", "Murat", 30, "Erkek", "Türk", "teknoloji", 3, 12000, 0.2)
    mavi_yaka2 = MaviYaka("55565432100", "Yavuz", "Kaya", 27, "Kadın", "Türk", "muhasebe", 2, 18000, 0.5)
    mavi_yaka3 = MaviYaka("76789012342", "Alp", "Yıldız", 32, "Erkek", "Türk", "inşaat", 12, 25000, 0.3)
    print(mavi_yaka1)
    print(mavi_yaka2)
    print(mavi_yaka3)

    beyaz_yaka1 = BeyazYaka("89945678910", "Merve", "Yılmaz", 32, "Erkek", "Türk", "teknoloji", 12, 12000, 500)
    beyaz_yaka2 = BeyazYaka("98765992100", "Mehmet", "Şen", 45, "Kadın", "Türk", "muhasebe", 5, 18000, 1500)
    beyaz_yaka3 = BeyazYaka("16709012305", "Zeynep", "Demir", 35, "Erkek", "Türk", "inşaat", 1, 25000, 1000)

    print(beyaz_yaka1)
    print(beyaz_yaka2)
    print(beyaz_yaka3)

if __name__ == "__main__":
    main()

