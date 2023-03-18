#region pyton arama metodları
"""
1-List index metodu:Liste elemanlarında arama yapar.Bulduğu anda indexi geriye döndürür.Ancak
bulamadığı anda value error fırlatılır
2-List coun metodu:Tam olarak arama özelinde bir metod değildir.Parametre ile gönderilen değerin
listede kaç adet oldğunu geriye döndürdüğü için dolaylı şekilde arama sürecne dail edilebilir.
Geriye sıfır döndüğünde bulamadığı anlaşılır
3-In/Not In:Bir değer arama metodudur.Kullanımı oldukça basittir
"""
"""
#endregion
ogrenciListesi=["amet","sena","eda","furkan","ibraim","irem","mert ramazan"]
sName="eda"
if "eda" not in ogrenciListesi:
    print("bulamadım")
else:
    result=ogrenciListesi.index("sName")
    print(result)
    print(f"{sName} listenin {result+1}. sırasındadır ")
    #print("buldum")
"""

stokKodlari=[1002,1008,1009,1005,1002,1008,1007]
tekrarsizStoklar=[]
for i in stokKodlari:
    if i not in tekrarsizStoklar:
        tekrarsizStoklar.append(i)
print(tekrarsizStoklar)