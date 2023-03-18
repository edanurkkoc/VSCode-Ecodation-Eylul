#Biz kendimiz listedeki eleman sayısını bulabiliriz
#Biz kendimiz son elemanı sil şeklinde bir alg. da geliştirebiliriz
"""
eleman sayısını bulma uzun yol vs metodlu yol
ogrenciListesi=["ahmet","sena","eda","furkan","ibraim","irem","mert","ramazan","şenaz","şakir","ayşe","nisa","tural"]
#say=0
#for i in ogrenciListesi:
#   say+=1
#print(f"listede {say} öğrenci vardır")
print(len(ogrenciListesi))
"""
"""
Listedeki son elemanı silme yolu uzun vs metodlu yol
ogrenciListesi=["ahmet","sena","eda","furkan","ibraim","irem","mert","ramazan","şenaz","şakir","ayşe","nisa","tural"]
#say=0
#for i in ogrenciListesi:
#       say+=1
#print(f"listede {say} öğrenci vardır")
#print(len(ogrenciListesi))
#del ogrenciListesi[say-1]
ogrenciListesi.pop()
print(ogrenciListesi)
"""
"""
               #########LİSTE METODLARI ÖRNEKLERİ#############
ogrenciListesi=["ahmet","sena","eda","furkan","ibraim","irem","mert","ramazan","şenaz","şakir","ayşe","nisa","tural"]
#ogrenciListesi.append("aziz")#sona ekle
#ogrenciListesi.insert(2,"aziz")#burda başa yazdığımız indekse ekliyoz
#ogrenciListesi.insert("aziz",2)#yanlış kod
ogrenciListesi.insert(100,"aziz")#sona atar
print(ogrenciListesi)

ogrenciListesi=["furkan","ahmet","sena","eda","furkan","ibraim","irem","mert","ramazan","şenaz","şakir","ayşe","nisa","tural"]
#ogranciListesi.remove("Furkan")#eğer birsürü furkan varsa ilkini siler diğerlerini bırakır
#ogrenciListesi.remove("")
#ogrenciListesi.pop()#son elemanı siler ekrana öyle yazar
#ogrenciListesi.pop(1)#indeksi 1 olanı siler ,ekrana da öyle yazar
ogrenciListesi.remove("furkan")
print(ogrenciListesi)

sebzeler=[]
sebzeler.pop()
"""
"""
ogrenciListesi=["furkan","ahmet","sena","eda","furkan","ibraim","irem","mert","ramazan","şenaz","şakir","ayşe","nisa","tural"]
ogrenciListesi.clear()
del ogrenciListesi#afızada var olan yerini silerek tümüyle siler
print(ogrenciListesi)


ogrenciListesi=["furkan","ahmet","sena","eda","furkan","ibraim","irem","mert","ramazan","şenaz","şakir","ayşe","nisa","tural"]
searchItem="furkan"
result=ogrenciListesi.count(searchItem)
print(f" Aradığınız {searchItem} elemanından {result} adet bulundu")
sayiListesi=[3,6,7,8,9,3]
items=["amet","sena",True,3<9,5>10]
print(items.count(True))


notListesi=[30,50,60,70,99]
#notListesi.sort() #küçükten->büyüğe
#notListesi.sort(reverse=False)#küçükten->büyüğe
#notListesi.sort(reverse=True)#büyükten->küçüğe
notListesi.reverse()#? bunu anlamadım ama küçükten büyüğe diye duymuştum sanki
print(notListesi)

notListesi=[30,50,60,70,99]
result=notListesi.index(50)#öyle bir değer yoksa yazma,error veriyor
print(result)
"""

#Global Talent

#extend SSS->FAQ
a=[3,5,8,1,2,7]
b=[2,6,8]
lenA,lenB=len(a),len(b)
diff=abs(lenA-lenB)
if lenA<lenB:
    a.extend([0]*diff)
else:
    b.extend([0]*diff)
print(a)
print(b)
"""
a=[3,5,8,1,2,7]
b=[2,6,8,0,0,0]
"""

