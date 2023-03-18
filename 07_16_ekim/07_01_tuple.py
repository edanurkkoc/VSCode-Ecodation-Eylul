"""
1-list
2-tuple
3-dictionary

1-list özellikleri
-tek bir değişken adında birden fazla eleman saklama
-sıralı index özelliği
-zera base'dir.İlk elemanlar[0] ,ikinci [0]
-duplicate eleman saklamay izin vermesi
-eleman değerlerinin değiştirilebilmesi
-tanımlama anında köşeli parantez kullanılması[]

2-tuple özellikleri
-tek eğişken adında birden fazla elman saklama
-sıralı index özelliği
-zero base'dir.İlk eleman [0] ikinci eleman [1]
-duplicate eleman saklamaya izin vermesi
-eleman değeğerlerinin değiştirilememesi
-tanımlama anında,aç kapa parantez() kullanılması

3-dictionary özellikler
-tek bir değişken adı altında birden fazla eleman saklama
-en önemli özelliği indisli değildir,sıralı değildir
-key-value pair dediğimiz çiftler ainde tanımlanır
-duplicate eleman saklamaya izin vermemesi
-eleman değerlerinin değiştirilebilir olması
-tanımlama anında,aç kapa süslü oarantez {} kullanılması
"""
"""
myTuples=("kırmızı","beyaz","sarı","mor")
#myTuples="kırmızı","beyaz","sarı","mor"
myTuples="kırmızı","beyaz","sarı","mor",155,200,300,"mor"
myTuples[1]="wite"#bunu çağıramaz çünkü yok 
print(myTuples)
print(myTuples[1])
for i in myTuples:
    print(i)
"""
"""
myTuples="kırmızı","beyaz","sarı","mor"
myList=[]
for i in myTuples:
    myList.append(i)
print(myList)
myList[1]="wite"
print(myList)
"""
"""
                                     tuple   list
1-birden fazla veri toplama           +        +
2-iki farklı tipte veri toplama       +        +
3-itterable/indeksli                  +        +
4-ekleme/çıkarma                      -        +
5-arama                               +        -
6-debugging                           +        -
7-afıza kullanımı                     -        +      
"""

isimListesi=("ali","ayşe","murat","memet","murat")
x=input("Aradığınız elelman: ")
print(f"aradığınız öğrenci isminden {isimListesi.count(x)} adet vardır")

sKodlari=(1001,1004,1007,1006)
x=input("aradığınız stok kodu : ")
if x.isdigit():
    x=int()
    if x not in sKodlari:
        print(f"aradığınız {x} kodlu stok mevcut değildir")
    else:
        print(f"aradığınız {x} kodlu stok {sKodlari.index(x)} stokdur")
else:
    print("Lütfen sayısal bir değer giriniz")
    

