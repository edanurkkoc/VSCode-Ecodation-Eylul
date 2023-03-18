"""
Loop:(Döngüler)
-Sürekli tekrar edden işlemlerde kullanılır
"""

"""
While Döngüsü
1-Başlangıç
2-Bitiş
3-Artış Miktarı
b:None
i=0
while i < 5:
    print("İnanılmaz fırsat")
    i+=1
    a=None
"""


"""
print("a")
i=1
while i<=2:
        print("b")
        i+=1
print("c")   
"""


"""
print("a")
i=1
while i<2:
        print("b")
print("c") 
#b de sonsuz döngüye girer
"""
"""
sayac=5
while sayac!=0:
    print(f"Dögü içindeyim {sayac}")
    sayac-=1
"""
#Tam sayıyı koşulda kontrol ederken def.da "tam sayı 0 olduğuda döngü kırılır"
#int 0 olduğunda false döner
"""
sayac=5
while sayac:
    print(f"Dögü içindeyim {sayac}")
    sayac-=1
"""
"""
devamMi=True
sayac=5
while devamMi==True:
    print(f"Dögü içindeyim {sayac}")
    sayac-=1
    if sayac ==2:
        pass
"""
devamMi=True
sayac=5
while devamMi:
    print(f"Dögü içindeyim {sayac}")
    sayac-=1
    if sayac ==2:
        devamMi=False

