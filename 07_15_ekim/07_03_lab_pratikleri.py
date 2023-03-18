"""
#s1=int(input("Lütfen bir sayı giriniz:  "))
#Mesela burda terminale "kırk beş " gibi bir değer girersek kod patlar
#AMA alttaki kodu yazarsak en azından ata alırız ve kod patlamaz
#Bu kodda - değerleri string olarak sayıp ata veriyor
s2=(input("Lütfen bir sayı giriniz:  "))
s1=(input("Lütfen bir sayı giriniz:  "))
if s1.isdigit() and s2.isdigit():
    s1,s2=int(s1),int(s2)
    print(f"iki sayının toplamı {s1+s2}")
else:
    print("Lütfen sadece sayısal bir değer giriniz: ")
"""
#Bu kodda yukardaki atayı lstrip ile giderdik ve artık - değerleri sayısal olarak tanımlıyor
s2=(input("Lütfen bir sayı giriniz:  "))
s1=(input("Lütfen bir sayı giriniz:  "))
if s1.lstrip("-").isdigit() and s2.lstrip("-").isdigit():
    s1,s2=int(s1),int(s2)
    print(f"iki sayının toplamı {s1+s2}")
else:
    print("Lütfen sadece sayısal bir değer giriniz: ")