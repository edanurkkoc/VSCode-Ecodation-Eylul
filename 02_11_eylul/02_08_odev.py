
""" odev->
Lütfen Günlük Ortalama Adım Sayınızı Giriniz; 5000 
Harcanan Kalori 
Günlük; ... 
Haftalık; ... 
Aylık; ... 
"""
ort_adimsayisi=int(input("Lütfen Günlük Ortalama Adım Sayınızı Giriniz: "))
hk_gunluk=ort_adimsayisi/8
hk_haftalik=(ort_adimsayisi*7)/8
hk_aylik=(ort_adimsayisi*30)/8
print(f"Harcanan Günlük Kalori:{hk_gunluk}\nHarcanan Haftalık Kalori{hk_haftalik}\nHarcanan Aylık Kalori{hk_aylik}")
