"""
Bankada 10 bin tlsi olan biri para transferi yapmak istiyor,transfer yapacak 
olan banka farklı banka ise %5  kesinti yapılıyor.Gün sonunda güncel banka bakiyesi
gösterilecek
Lütfen banka kodunu giriniz:1001
Lütfen transfer banka kodunu giriniz:1001
Transfer edilecek tutarı giriniz:5000
Güncel Bakiye:
"""
"""
bakiye=10000
transfer_tutar=int(input("Transfer edilecek tutarınız?: "))
banka_kodu=int(input("Lütfen banka kodunuzu giriniz: "))
transfer_kodu=int(input("Lütfen transfer banka kodunuzu giriniz: "))
kesinti=0

if banka_kodu!=transfer_kodu:
   kesinti=transfer_tutar*0.05
print(f"Bankanız sizden {kesinti} ücret alıcaktır.Yeni bakiyeniz {bakiye-(transfer_tutar+kesinti)}")
"""
""""
Y.İçi Uçuşlarda KDV %18
Kontuar görevlisi fiyat girecek
Bavul ağırlığı ise 15 kg üzerindeki er bir ağırlık için bilete 5 tl ek ücret verilecek
Günün sonunda güncel fiyatı ekrana basıcaz
"""
"""
bilet_fiyati=int(input("Bilet fiyatını giriniz: "))
bavul_agirligi=int(input("Bavul ağırlığınızı giriniz: "))
if bavul_agirligi>15:
    güncel_fiyat=(bavul_agirligi-15)*5 +( (bilet_fiyati * 0.18) + bilet_fiyati)
    print(f"Ödemeniz gereken tutar {güncel_fiyat}'dir.")

print(f"Ödemeniz gereken tutar {( (bilet_fiyati * 0.18) + bilet_fiyati)} 'dir.")"""
    
"""
1.sınav notunu giriniz:90
2.sınav notunu giriniz:100
Yıl sonu notunuz 95,Başarı durumu peki
"""

"""
sinav1,sinav2=int(input("1.sınav notunuzu giriniz: ")),int(input("2.sınav notuuzu giriniz: "))
ort=(sinav1+sinav2)/2
if ort>=85:
    print(f"{ort} yıl sonu notu ile başarı durumu pek iyi ")
elif ort>70:
    print(f"{ort} yıl sonu notu ile başarı durumu iyi ")
elif ort>=55:
    print(f"{ort} yıl sonu notu ile başarı durumu orta ")
elif ort>=45:
    print(f"{ort} yıl sonu notu ile başarı durumu geçer ")
else :
    print(f"{ort} yıl sonu notu ile başarı durumu çok kötü ")
"""

"""
Kullanıcı adı:user
Parola:1234
Kullanıcı adı yanlış,Lütfen tekrar deneyiniz

Kullanıcı adı:admin
Parola:1234
Parola yanlış,Lütfen tekrar deneyiniz

Kullanıcı adı:admin
Parola:123
Login başarılı
"""




"""
k_id="admin"
pw=123
k_id=input("Kullanıcı adınız giriniz:  ")
pw=int(input("Lütfen şifre giriniz: "))
if pw !=1234 and k_id !="admin":
    print("Kullanıcı adınız ve parolanız yanlıştır,tekrar deneyiniz: ")
elif pw!=1234:
    print("Parola yanlış,tekrar deneyiniz: ")
elif k_id!="admin":
    print("Kullanıcı adı yanlıs,lütfen tekrar giriniz")
else :
   print("Login başarılı:))")
"""
"""
Lütfen 1.sayıyı girin=63
Lütfen 2.sayıyı girin=2
Lütfen 3.sayıyı girin=25
63>25>2
"""

s1=int(input("1.sayıyı girin= "))
s2=int(input("2.sayıyı girin= "))
s3=int(input("3.sayıyı girin= "))
#s1,s2=s2,s1
if s1<s2:
    s1,s2=s2,s1
if s2<s3:
    s2,s3=s3,s2
if s1<s3:
    s1,s3=s3,s1
print(f"Sıralama: {s1}>{s2}>{s3}  ")














