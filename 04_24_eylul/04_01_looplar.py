#Dögüler
"""
Lütfen sayı giriniz,çıkmak için 0...:3
Lütfen sayı giriniz,çıkmak için 0....:6
Lütfen sayı giriniz,çıkmak için 0.....:12
Lütfen sayı giriniz,çıkmak için 0.....:10
Lütfen sayı giriniz,çıkmak için 0....:11
Lütfen sayı giriniz,çıkmak için 0.....:0
Girdiğiniz tek sayıların toplamı 14
"""
"""
tek_sayılar_top=0
sayi=int(input("Lütfen bir  sayi giriniz,çıkmak için 0 giriniz: "))
while sayi!=0:
    if sayi%2==1:
        tek_sayılar_top+=sayi
    sayi=int(input("Lütfen bir  sayi giriniz,çıkmak için 0 giriniz: "))
print(f"Girdiğiniz tek sayıların toplamı :{tek_sayılar_top}")
"""

"""
Lütfen sayı giriniz,çıkmak için 0...:3
Lütfen sayı giriniz,çıkmak için 0....:6
Lütfen sayı giriniz,çıkmak için 0.....:12
Lütfen sayı giriniz,çıkmak için 0.....:10
Lütfen sayı giriniz,çıkmak için 0....:11
Lütfen sayı giriniz,çıkmak için 0.....:0
2 adet tek sayı,3adet çift sayı girdiniz 
"""
tekSayiAdeti=0
ciftSayiAdeti=0
sayi=int(input("Lütfen bir  sayi giriniz,çıkmak için 0 giriniz: "))
while sayi!=0:
    if sayi%2==1:
        tekSayiAdeti+=1
    else:
        ciftSayiAdeti+=1
    sayi=int(input("Lütfen bir  sayi giriniz,çıkmak için 0 giriniz: "))
print(f"{tekSayiAdeti} adet tek sayı ve {ciftSayiAdeti} adet çift sayı vardır")



