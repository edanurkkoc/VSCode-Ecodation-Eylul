def selamlama(ad:str):
    import datetime
    saat=datetime.datetime.now().hour
    if saat <12:
        print(f"Gunaydın {ad}")
    else:
        print(f"Meraba {ad}")

selamlama("Eda")