"""
matris yapılar oluşturma
veri tabanı mimarisine benzer satırxsütun yapıları ouşturma
"""
"""
a=[[1,2,3,4],[2,4,6,8]]#Bu da olur
a=[
    [1,2,3,4],
    [2,4,6,8]       #Bu gösterim de uygundur
]
print(a)

#1,2,3,4
#2,4,6,8

print(a[0])
print(a[1])
print(a[0][2])
"""
#Liste elemanlarına iç içe for ile yaklaşım,
#ama işte biz bu kodda bir eleman ekle-çıkar durumunda zor duruma düşeriz
#o yüzden genel bir tanım içeren kod lazım;statik değil dinamik bir kod lazım
"""
a=[
    [1,2,3,4],
    [2,4,6,8]       #Bu gösterim de uygundur
]
for i in range(2):
    for j in range(4):
        print(a[i][j],end=" ")
    print()
"""
#dinamik bir yapı yazalım
"""
a=[
    [1,2,3,4],
    [2,4,6,8]       #Bu gösterim de uygundur
]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
    print()
"""
"""
#wpde attım,çok boyutlu liste örneği var burda bir tane
for i in range(8):
    row=["piyon" for j in range(8)]
    print(row)
#---------------------------
row=[["piyon" for j in range(8)]for i in range(8) ]
print(row)
#---------------------------------
row=[[f"{i}{j}" for j in range(8)]for i in range(8) ]
print(row)
"""
ogrenciler=[
        ["Ali","Çalışkan",90,100],
        ["Murat","Dost",30,38],
        ["Ajime","Minabe",30,100]
]
for i in ogrenciler:
    ort=(i[2]+i[3])/2
    if ort<50:
        print(f"{i[0]} {i[1]} Ortalamanız {ort}->KALDI")
    else:
        print(f"{i[0]} {i[1]} Ortalamanız {ort}->GECTİ")
    

for i in ogrenciler:
        if i[3]==100:
            print(i[0],i[1])


