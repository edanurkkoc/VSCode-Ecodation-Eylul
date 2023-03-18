"""

Eklenecek film adı giriniz.Çıkmak için -1:Yeşil yol
Eklenecek film adı giriniz.Çıkmak için -1:Titanik
Eklenecek film adı giriniz.Çıkmak için -1:Rocky
Eklenecek film adı giriniz.Çıkmak için -1:Yüzüklerin Efendisi
Eklenecek film adı giriniz.Çıkmak için -1:-1
Yeşil yol,Titanik,Rocky,Yüzüklerin Efendisi


print(
        1-Ekle
        2-Çıkart
        3-Listele
        4-Çıkarmak

)
favoriFilm=[]
while True:
    x=int(input("Lütfen seçiminiz yapınız:"))
    if x==4:
        break
    elif x==1:
        film=input("Eklenecek film adı giriniz.Çıkmak için -1:")
        favoriFilm.append(film)
    elif x==2:
        film=input("Çıkarılacak film adı giriniz: ")
        favoriFilm.remove(film)
    elif x==3:
        print(favoriFilm)
        for i in range(0,len(favoriFilm)):
            print(f"{i+1}.filmin adı {favoriFilm[i]}")#Filmin tüm karakterlerini yazdırmak için i yazıyoruz
    else:
        print("Yanlış seçim")

    if film=="-1":
        break

"""
"""
ogrenciListesi=["furkan","amet","sena","eda","mert","şakir","ayşe"]
output=""
for i in ogrenciListesi:
    output+=f"{i} - "
print(output.rstrip(" - "))
"""
"""notlar=[]
while True :
    oAdSoyad=input("Bir öğrenci adı giriniz,çıkmak için-1/t:")
    if oAdSoyad=="-1":
        break
    n1=int(input(f"{oAdSoyad} öğrencinin 1.notunu giriniz: "))
    n2=int(input(f"{oAdSoyad} öğrencinin 2.notunu giriniz: "))
    ort=(n1+n2)/2
    notlar.append(ort)
notlar.sort()#Ortalama değerleri küçükten büyüğe diziyor
for i in notlar:
    print(i)
print(f"en düşük not:{min(notlar)}--en yüksek not:{max(notlar)}")
"""

aciklama="Auagdaak adakdjsdoıaoean dfgjkryftugyjıedytgjnedbjmfcxmwes bswrfıysbsfsfjıopffoppjıjpjıb bdfofjıjf "
#print(len(aciklama))
yeni=" "
x=0
if len(aciklama)>30:
    for i in aciklama:
        yeni+=i
        x+=1
        if x==30:
            break
    print(f"{yeni}...")


    






