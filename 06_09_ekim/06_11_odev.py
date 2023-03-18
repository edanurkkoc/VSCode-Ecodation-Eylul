"""
Ödev
Sıra No         Ad Soyad            Matematik       Fizik       Kimya
1               Ali Kemal           80              50          80
2               Murat Çalışkan      50              30          70
3               Efe Aydın           50              20          100
Output
Ali Kemal isimli öğrencinin ortalaması 70
Murat Çalışkan isimli öğrencinin en yüksek notu 70
Matematik dersinin sınıf ortalması 60
"""

ogrenciler=[
    ["Sıra No","Ad Soyad","Matematik","Fizik","Kimya"],
    [1,"Ali Kemal",80,50,80],
    [2,"Murat Çalışkan",50,30,70],
    [3,"Efe Aydın",50,20,100]
    ]
for i in ogrenciler:
    ort=(i[2]+i[3]+i[4])/3
    print(f"{i[1]} {i[1]} isimli örencinin ortalaması: {ort}")
    print(f"{i[0]} {i[3]} dersinin sınıf ortalaması: {ort}")



