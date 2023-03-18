#region fonksiyon_turu
"""
Fonksiyon tanımlama anında argüman almaz,değer döndürmez

"""
#endregion
"""
def kullaniciGiris():
    kAd=input("Lütfen kullanici adinizi giriniz :   ")
    print(f"oşgeldiniz {kAd}")

kullaniciGiris()
"""
#Topla diye fonks yapıp kullanıcıdan değer alıp ekrana bas
"""def topla():
    deger1=int(input("Lütfen değer giriniz : "))
    deger2=int(input("Lütfen değer giriniz : "))
    print(f"{deger1} ve {deger2}'nin toplamı = {deger1 +deger2}")
topla()
"""

#region fonksiyon_turu
"""
Fonksiyon tanımlama anında argüman alır,değer döndürmez

"""
#endregion
def isValid(dTarihi):
    if str(dTarihi).isdigit():#isdigit()->tüm değerler rakamlardan oluşmalıdır o zmn TRUE döndürür
        yas=2022-int(dTarihi)
        if yas>=19:
            print("askere gidebilirsin")
        else:
            print("12 yıllık eğitimini tamamla sonra askerlik")
    else:
        hataKodu100()

def hataKodu100():
    print("Lütfen sayısal değer giriniz !!!")

isValid("nisan")

#region positional_arguments_siralı_argumanlar
"""


"""
#endregion








