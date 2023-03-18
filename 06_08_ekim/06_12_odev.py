"""
iki basamaklı sayıyı metne dönüştüren uygulama
95-->Doksan beş
"""
birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]#zero base saydık
onlar=["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]#yani 0,1,2,...
sayi=int(input("Bir sayı giriniz: "))
print(f"{onlar[sayi//10] } {birler[sayi%10]}")
