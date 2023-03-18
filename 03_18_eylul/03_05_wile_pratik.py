"""
eb=-9999999999999
sayi=int(input("Lütfen çıkmakiçin -1 sayısını giriniz:"))
while sayi!=-1:
    if sayi>eb:
        eb=sayi
    sayi=int(input("Lütfen çıkmakiçin -1 sayısını giriniz:"))
print(f"En byük sayiv{eb}")
"""

#Girilen 5 sayıdan en büyüğünü ekrana basar
eb=-9999999999999
i=0
while i<5:
    sayi=int(input(f"Lütfen {i+1}. sayı giriniz : "))
    if sayi>eb:
        eb=sayi
    i +=1
print(f"En büyük sayi {eb}")


    