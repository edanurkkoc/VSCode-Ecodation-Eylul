#a ile başlayan isimleri sırala

"""
ogrenciListesi=["ahmet","sena","eda","furkan","ibraim","irem","mert","ramazan","şenaz","şakir","ayşe","nisa","tural"]
isim=ogrenciListesi
x=0
arananKarakterler=["a","ş"]
for i in arananKarakterler:
    for j in ogrenciListesi:
        if j[0]==i:
                print(j)
                x+=1
    print(f"{i} ile başlayan {x} adet isim var")
    x=0
"""
#angi sesli arften kaç tane olduğunu yazdırıyoruz
ad="edanur"
karakterler=["a","e","ı","i","o","ö","ü","u"]
say=0
for i in karakterler:
    for j in ad:
        if i==j:
            say+=1
    print(f"{i} karakterinden {say} adet vardır")
    say=0

