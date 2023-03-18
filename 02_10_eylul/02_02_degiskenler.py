#1-camel casing>>Deve Notasyonu
okulNumarasi=10001
ad="Edanur"
soyad="Kocakoc"
tcKimlikNo=11111
sinavNotu=96
print(okulNumarasi,"\n",ad,"\n",soyad,"\n",tcKimlikNo,"\n",sinavNotu)

#2-underscore casing->alt-tire notasyonu(kelimeler küçük arflerle arada alt tire)
okul_numarasi=10001
ad="Edanur"
soyad="Kocakoc"
tc_kimlik_no=11111
sinav_notu=96
print(okul_numarasi,"\n",ad,"\n",soyad,"\n",tc_kimlik_no,"\n",sinav_notu)

#Değişken İsimlendirme Kuralları
#1-Harf veya altçizgiyle başamalıdır
ad="ayse"
birinci="ordu"
_1nci="ORDU"
print(ad)
print(birinci)
print(_1nci)

#2-rakam ile başlayamaz
"""1_inci="Eda"
print(1_inci)"""

#3-ilk harf dışındakiler,harf,sayı,alt çizgi olabilir
plaka52="Ordu"
print(plaka52)
#4-alt çizgi dışında alfa sayısal karakterlerimiz (%,#,$,vs vs) kullanılmaz
plaka_52="Ordu"
print(plaka_52)
#5-case sensitive
"""ad="Eda"
print(AD)"""
ad="Eda"
print(ad)
#6-anahtar kelimeler if,pass,while,def bunlar kullanılmaz
import keyword
print(keyword.kwlist)
"""['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 
'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 
'raise', 'return', 'try', 'while', 'with', 'yield']""" """Bunları kullanamayız"""
#7-Türkçe karakter kullanmamaya özen gösterelim
"""okulÇantası="eda"
print(okulÇantası)"""






