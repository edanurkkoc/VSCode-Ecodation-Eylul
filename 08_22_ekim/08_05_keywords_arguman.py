#KEYWORDS ARGUMAN
"""
def hastaKarti(ad,soyad):
    print(f"Sağlıklı günler günler dileriz {ad} {soyad}")
hastaKarti(soyad="kocakoc",ad="eda")
"""

def urunSatistaMi(uKodu,uAdi,fiyat,satistaMi):
    if satistaMi:
        print(f"urun kodu {uKodu} nolu {uAdi}, {fiyat} fiyatı ile satışta")
    else:
        print(f"urun kodu {uKodu} nolu {uAdi} satışta değil")
        
urunSatistaMi(1001,"kuru kahve",25,True)
