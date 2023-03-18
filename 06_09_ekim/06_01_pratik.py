"""
#2 basamaklı bir sayıyı 10luğa ayır
birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz","","",""]#zero base saydık
onlar=["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan","",""]#yani 0,1,2,...
sayi=int(input("Bir sayı giriniz: "))
print(f"{onlar[sayi//10] } {birler[sayi%10]}")
#mesela sayi//10 nedir felan diye öğrenmek istiyoruz ya onu sell(yani terminal) ekranında
#deniyip sürekli print yapmadan zaman kazanarak alledebiliriz
"""

#Sıralama algoritması,küçükten büyüğe
#Sıralama=Yer değiştirmedir(swaping tekniğini kullanıcaz yani)
"""
9,7,6,3,4,1,5,2,8
7,6,3,4,1,5,2,8,9
6,3,4,1,5,2,7,8,9
....
1,2,3,4,5,6,7,8,9

"""

say=0
listem=[9,7,6,3,4,1,5,2,8]
while True:
    siraliMi=True
    for i in range(len(listem)-1):
        if listem[i]>listem[i+1]:
            listem[i],listem[i+1]=listem[i+1],listem[i]
            siraliMi=False#Mesela burda sürekli dösün ve bir kerede koşulu sağlayıp ekran basamasın diye böyle yazdık
        say+=1
    if siraliMi:
        break
print(listem)
print(say)

