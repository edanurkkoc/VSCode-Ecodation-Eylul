"""
print("Leylek uygulamasına hoşgeldiniz!!!
Sürüş ücreti 1.99/dk")

s=int(input("Lütfen sürüş süresini giriniz [saat]\t:  "))
d=int(input("Lütfen sürüş süresini giriniz [dakika]\t:  "))
tDakika =s*60
tDakika+=d
print(f"Sürüşünüzün süresi {s} : {d} - {tDakika} dk.da bitmiştir.")
print(f"Kartınızdan {1.99*tDakika} tutar çekilmiştir")
"""


s=int(input("Lütfen sayı giriniz ->"))
kalan=s%10
birler=kalan//1
kalan=s%100
onlar=kalan//10
kalan=s%1000
yuzler=kalan//100
print(f"basamakları {birler} {onlar} {yuzler} sayının haneleri toplamı {birler+ onlar+yuzler}")

