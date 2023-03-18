#koleksiyonlar
#list,tuple,dictionary
#ad1="seda"
#ad2="eda"
#ad3="emre"
#s1=56
#s2=526
#s3=5
"""
ogrenciIsimleri=["seda","eda","emre"]
print(ogrenciIsimleri)
ayakkabiKoleksiyonum=[]#empty
print(ayakkabiKoleksiyonum)
meyveler=["elma" "armut" "muz" "elma"]#duplicate
print(meyveler)
favIller=["ordu","samsun","eskişeir"]
sevdigimRenkler=["kırmızı","kırmızı"," "]
print(sevdigimRenkler)

#2.sayının yerine dört yaz
sayilar=[3,56,4,8,19,56,5.8,55,4,53]
sayilar[2]="dört"
result=sayilar
print(sayilar)
#2.sayının yerine 4. sayıyı yaz
sayilar=[3,56,4,8,19,56,5.8,55,4,53]
sayilar[2] = sayilar[4]
result=sayilar
print=(sayilar)
#listenin eleman sayısını öğrenmek için LEN basarız
sayilar=[3,56,4,8,19,56,5.8,55,4,53]
print(f"listedeki eleman sayısı= {len(sayilar)}")
del sayilar [2]
print(f"listedeki eleman sayısı= {len(sayilar)}")


#Listenin elemanlarını çıktıda tek tek görmek istiyosak for dögüsünü kullanırız
sayilar=[3,56,4,8,19,56,5.8,55,4,53]
print("Listedeki float olan sayıları ekrana yaz")
for i in sayilar:
    if isinstance(i,float):
        print(i)

sayilar=[3,56,4,8,19,56,5.8,55,4,53]
print("Listedeki tek olan sayıları ekrana yaz")
for i in sayilar:
    if i%2==1:
        print(i)

#Listenin elemanlarını çıktıda tek tek görmek istiyosak for dögüsünü kullanırız
sayilar=[3,56,4,8,19,56,5.8,55,4,53]
print("Listedeki elemanlar")
for i in sayilar:
        print(i) 
#Uzun metod
sayilar=[3,56,4,8,19,56,5.8,55,4,53]
for i in range(0,len(sayilar)):
    print(sayilar[i]) 
    
"""
sayilar=[3,52,55,53]
sayilarIndex=[]
for i in range(0,len(sayilar)):
    sayilarIndex.append(i)
print(sayilarIndex)
