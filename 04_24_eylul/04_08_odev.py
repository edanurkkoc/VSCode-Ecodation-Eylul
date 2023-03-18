""" 
ödev 
→ 
 - kullanıcıdan ad ve şifre değeri alınır. 
 - taaki kullancı admin 123 değerleri girene kadar. 
 - girilen her hatalı girişte HATALI GIRIS, 
 - doğru girildiğinde HOŞGELDİNİZ yazar. 
""" 

ad=input("Lütfen kullanıcı adı giriniz\t:")
sifre=int(input("Lütfen kullanıcı şifresini giriniz\t:"))
if ad=="admin":
    if sifre==123:
        print("HOŞGELDİNİZ")
    else:
        print("HATALI GIRIS")
else:
     print("HATALI GIRIS")


