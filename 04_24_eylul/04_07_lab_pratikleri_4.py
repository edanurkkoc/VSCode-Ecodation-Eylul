#haneleri toplamı hane sayısına eşit olan 100-999 arası tam sayıları ekrana yazdıralım
#mesela 102,3 haneli ve toplamı:3
"""
i=100
while i<1000:
        kalan=i%10
        birler=kalan//1
        kalan=i%100
        onlar=kalan//10
        kalan=i%1000
        yüzler=kalan//100
        haneler=birler+onlar+yüzler
        if haneler==3:
                print(f"{i}(3 haneli,haneleri toplamı 3)")
        i+=1
"""
        


x=10
y=1
i=573
kalan=i%x
birler=kalan//y
x*=10
y*=10
kalan=i%x
onlar=kalan//y
x*=10
y*=10
kalan=i%x
yuzler=kalan//y
print(yuzler,onlar,birler)
