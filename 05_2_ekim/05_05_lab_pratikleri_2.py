"""
İstenilen aradığınız 55 değeri,6.indeksli elemandır
sayilar=[3,56,4,8,19,56,55,4,53]
a=55
#####################################
sayilar=[3,56,4,8,19,56,55,4,53]
a=55
point=0
for i in sayilar:
    if a==i:
        break
    else:
        point+=1
print(f"Aradığınız {i} değeri,{point}.indeksli elemandır.")
"""
"""
#İTERABLE
meyveTabagi=["jkl","jkl","gjkl","jsjd"]
print(meyveTabagi[1])
print(meyveTabagi)

ad="Eda"
print(ad[0])
print("Eda")

ad="Edanur"
print(ad[5],ad[4],ad[3],ad[2],ad[1],ad[0])

ad="Edanur"
print(len(ad)-1)
print(ad[len(ad)-1])

for i in range(len(ad)-1,-1,-1):
    print(ad[i])
"""


"""
ogrenciListesi=["amet","sena","eda","furkan","ibraim","irem","mert","ramazan","şenaz","şakir","ayşe","nisa","tural"]
aradığınız öğrenci=Furkan
furkan isimli öğrenci listemizde mevcut

aradığınız öğrenci=murat 
murat isimli öğrenci listemizde bulunamadı"""

"""ogrenciListesi=["amet","sena","eda","furkan","ibraim","irem","mert","ramazan","şenaz","şakir","ayşe","nisa","tural"]
ogrenci=input("Aradığınız öğrenci ismini giriniz=")
for i in ogrenciListesi:
    if ogrenci==i:
        print(f"Aradığınız {ogrenci} isimli öğrenci listemizde vardır")
        break
else:
    print(f"Aradığınız {ogrenci} isimli öğrenci listemizde yoktur")
"""
ogrenciListesi=["amet","sena","eda","furkan","ibraim","irem","mert","ramazan","şenaz","şakir","ayşe","nisa","tural"]
while True:
    ogrenci=input("Aradığınız öğrenci ismini giriniz ve çıkmak için ç'ye basınız=")
    if ogrenci=="ç":
        break
    for i in ogrenciListesi:
        if ogrenci==i:
            print(f"Aradığınız {ogrenci} isimli öğrenci listemizde vardır")
            break
    else:
        print(f"Aradığınız {ogrenci} isimli öğrenci listemizde yoktur")
        