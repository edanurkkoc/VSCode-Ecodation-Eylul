# ödev 
""" 
youtube abone sayısında çıktı anında son ek ekleme 
-izlenme 18000 → 18 B Abone 
-izlenme 1800000 → 1.8 Mn Abone 
-izlenme 1800000000 → 1.8 Ml Abone 
"""

abone_sayi=int(input("Youtube abone sayınızı giriniz: "))
while True:
    if abone_sayi>=1000 and abone_sayi<=999999:
        print(f"{abone_sayi//1000}B")
    elif abone_sayi>=1000000 and abone_sayi<=999999999:
        print(f"{(abone_sayi//1000)/1000}Mn")
    elif abone_sayi>=1000000000 and abone_sayi<=99999999999:
         print(f"{(abone_sayi//1000000)/1000}Ml")
    else:
        pass
    break