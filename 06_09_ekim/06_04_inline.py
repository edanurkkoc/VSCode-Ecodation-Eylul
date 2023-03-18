#liste=[]
#for i in range(1,9):
#    liste.append(i)
#print(liste)
#--------------------------------------
#liste=[i for i in range(1,9)]
#print(liste)
"""
aftaninGunleri=["","pazartesi","sali","carsamba","persembe","cuma","cumartesi","pazar"]
listem=[f"aftanın {i}. günü {aftaninGunleri[i]}" for i in range(1,8)]
print(listem)
"""
"""
fav mevsim ,çıkmak için -1 giriniz:yaz
fav mevsim ,çıkmak için -1 giriniz:güz
fav mevsim ,çıkmak için -1 giriniz:yaz
önceden eklediniz
fav mevsim ,çıkmak için -1 giriniz:ilkbaar
fav mevsim ,çıkmak için -1 giriniz-1
fav mevsimlerimiz yaz,güz,ilkbaar

mevsimler=[]
while True:
    mevsim=input("fav mevsim ,çıkmak için -1 giriniz: ")
    if mevsim=="-1":
        break
    if mevsim in mevsimler:
        print("önceden eklediniz")
        continue
    mevsimler.append(mevsim)
print(f"favori mevsimleriniz :{mevsimler}")
"""
"""
#İki tane verilen grup arasındaki aynı olan değerleri ayrıştırır,eşitler

list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
#1,2,3,4,5,6,7,8
tekilListe=list1.copy()
for i in list2:
    if i not in tekilListe:
        tekilListe.append(i)
print(tekilListe)
"""
#İki tane verilen grup arasındaki aynı olan değerleri döndürüp,yazar
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
ortakElemanlar=[]
for i in list1:
    if i  in list2:
        ortakElemanlar.append(i)
print(ortakElemanlar)
    




