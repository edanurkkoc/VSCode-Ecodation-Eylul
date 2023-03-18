"""
Sayı giriniz:5
5*1=5
5*2=10
5*3=15
5*4=20
5*5=25
"""
"""
sayi=int(input("Lütfen 1-9 arası rakam giriniz: "))
i=1
while i<=sayi:
    print(f"{sayi}*{i}={sayi*i}")
    i+=1
"""
"""
1  1
2  2
3  6
4  24
5  120
"""
"""
i=1
sonuc=1
while i<=5:
    sonuc=i * sonuc
    print(f"{i} {sonuc}")
    i+=1

"""
"""
1 den 100e kadar 7ye tam bölünen sayıları ekrana bas
"""
"""
i=1
while i<=100:
    if i %7==0:
        print(f"{i}",end=" ")
    i+=1
"""
"""
1 den 100e kadar 7ye tam bölünen sayıları ekrana bas ve kaç tane 
olduğunu söyle
i=1
adet=0
while i<=100:
    if i %7==0:
        adet+=1
    i+=1

print(adet)
"""
"""
Lütfen bir rakam giriniz:7
7 14 21..
7 ye tam bölünenlerinin adedi 8
ve bölnenlerin toplamı
"""

sayi=int(input("Bir sayi giriniz= "))
i=1
counter=0
toplam=0
while i<100:
    if i%sayi==0:
        toplam+=i
        print(i,end=" ")
        counter+=1
    i+=1

print(f"Girilen {sayi} sına tam bölünenlerin adeti={counter}")
print(f"Girilen {sayi} sına tam bölünenlerin toplamı={toplam}")
    
    
    
    