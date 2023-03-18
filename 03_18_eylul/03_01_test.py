"""
urun_fiyati=float(input("Satın alınan ürün fiyatı"))
kargo_fiyati=7.5
if urun_fiyati>250:
    print(f"Ürünün toplam fiyatı:{urun_fiyati}")
if urun_fiyati<=250:
    print(f"Ürünün toplam fiyatı:{urun_fiyati+kargo_fiyati}")
"""

urun_fiyati=float(input("Satın alınan ürün fiyatı"))
kargo_fiyati=7.5
if urun_fiyati<=250:
    urun_fiyati+=kargo_fiyati
    print(f"Ürünün toplam fiyatı:{urun_fiyati+kargo_fiyati}")
    




