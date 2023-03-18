#random-Rastgele sate sayılar üretir
#built-in
#seed-rastgeleliği sabitleyerek aynı sayıyı ekrana basar

#Böyle de yazılabiliyor
#import random
#print(random.random())#Mesela birsürü değer üretir ama 1.0 değerini üretmez.

#import random as  rnd#tüm random kütüpanesini çağırdık az önce mesela
#print(rnd.random()

#from random import randrange#Mesela burda tüm random kütüpanesini değil de  randrange çağrıldı sadece
"""
import random as  rnd
for i in range(5):
    print(rnd.random(),end=" ")

from random import randrange
print(randrange(3))#min<=x<max:0,1,2
print(randrange(3,6))#min<=x<max:3,4,5

for i in range(25):
    print(randrange(3,6),end=" ")

from random import randrange
print(randrange(10,50,10))

from random import randrange,randint
for i in range(10):
    print(randrange(3,6))#Burda min ve max da daildir,mesela 3,4,5,6 olabilir

import random
random.seed("şakir")#sabitlemek istediğimiz yere ad koyuyoruz,
print(f"1.sayı {random.randint(25,75)} ")
random.seed("şakir")
print(f"2.sayı {random.randint(25,75)} ")
random.seed("şakir2")#mesela yerin adını değiştirdiğimiz için 3.sayı farklı,1 ve 2 aynı oldu
print(f"3.sayı {random.randint(25,75)} ")
"""
"""
from random import sample,choice,randrange
oListesi=["irem","mert","furkan","ibraim"]
i=randrange(0,4)
print(oListesi[i])
"""
"""
from random import sample,choice,randrange
oListesi=["irem","mert","furkan","ibraim"]
#print=(choice(oListesi))
result=sample(oListesi,2)
print(result)
print(type(result))

#####################################################################
from random import sample,choice,randrange
oListesi=["irem","mert","furkan","ibraim"]
kListesi=[
    ["irem",0],
    ["mert",1],
    ["furkan",2],   
    ["ibraim",3],
]
_1,_2,_3,_4=0,0,0,0
for i in range(100):
    o=choice(oListesi)
    if o =="irem":
        _1+=1
    elif o=="mert":
        _2+=1
    elif o=="furkan":
        _3+=1
    elif o=="ibraim":
        _4+=1
kListesi[0][1]=_1#pars ettik ve skor bilgilerini gösterdik
kListesi[1][1]=_2
kListesi[2][1]=_3
kListesi[3][1]=_4
print(kListesi)
"""

import random as rnd
z1=int(input("z1 :"))
z2=int(input("z2 : "))
sayac=0
if 0<z1<7 and 0<z2<7:
    while True:
        zar1=rnd.randint(1,6)
        zar2=rnd.randint(1,6)
        sayac+=1
        if(z1==zar1 and z2==zar2) or (z2==zar1 and z1==zar2):
            print(f"{sayac}.seferde bulundu {zar1}-{zar2}")
            break
else:
    print("atalı giriniz")


