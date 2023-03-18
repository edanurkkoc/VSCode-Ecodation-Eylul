"""
#VKİ(Vücut kitle indeksi)
#zayıf->18,5
#ideal->18,5-24,9
#şişman->25-29,9
#obez->30-34,9
#aşırı obez->35>

durum=True
while True:
    kilo=float(input("Lütfen kilonuzu kg olarak giriniz: "))
    print(kilo)
    boy=float(input("Lütfen boyunuzu m olarak giriniz: "))
    print(boy)
    vci=kilo/(boy**2) #vücut kitle indeksi
    if vci<18.5:
        vci="Zayıf"
    elif 18.5<vci and  vci<24.9:
        vci="İdeal"
    elif 25<vci  and vci<29.9:
        vci="Şişman"
    elif 30<vci  and vci<34.9:
        vci="Obez"
    else :
        vci="Aşırı Obez"
    print(vci)
    devam=input("Devam edecek misiniz [e/E]? ")
    print(devam)
    if devam in " e\E":
        durum=False
#ÖDEV:İdeal kilo için şu kadar kio al-ver
"""

"""
1 den 20ye kadar olan sayıların angisinin asal olup olmadığını ekrana bassın
mesela 3->Asal
       12->Asal değil
gibi
"""
"""
for i in range(2,19+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(f"{i}")

"""
a=int(input("Lütfen aralık giriniz a: "))
b=int(input("Lütfen aralık giriniz b:"))
say=0
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        say+=1
print(f"<{a}-{b}> aralığında {say} adet asal sayı vardır")

