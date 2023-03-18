#for ve while arası farklar
"""
sDizisi=list(range(10,3,-1))
print(sDizisi)

sDizisi=list(range(5))
print(sDizisi)

sDizisi=list(range(2,20,2))
print(sDizisi)

sDizisi=list(range(2,10))
print(sDizisi)
"""
"""
1.Öğrenci
2.Öğrenci
3.Öğrenci
.
.
.
10.Öğrenci

import time
for i in range(1,11):
    if i!=5:
        print(f"{i}. öğrenci ")
    time.sleep(1)
"""
"""for i in range(1,6):
    for j in range(1,6):
        print(f"{i}-{j}\t",end=" ")
    print()
"""
"""
Mesela 30 a kadar 30 un bölenlerini ekrana bas
"""
adet=0
sayi=int(input("Bir sayi giriniz: "))
for i in range(1,sayi+1):
    if sayi%i==0:
        print(f"{i}",end=" ")
        adet+=1
print(f"\n{sayi} sayısının {adet} adet tam böleni vardır",end=" ")
