"""
açıl .... açıl:kahve
heheheheheheheh ne oldu çıkamıyor musun:-)
açıl .... açıl:nane
heheheheheheheh ne oldu çıkamıyor musun:-)
açıl .... açıl:susam
"""


"""
secret="susam"
answer=input("Açıl ... açıl.Lütfen boşluğu doldurunuz: ")
while answer!=secret:
    print("Kapı açılmıyo bitch")
    if answer=="susam":
        pass
    else:
        answer=input("Açıl ... açıl.Lütfen boşluğu doldurunuz:")
"""
"""
secret="susam"
answer=input("Açıl ... açıl.Lütfen boşluğu doldurunuz: ")
while answer!=secret:
    print("Kapı açılmıyo bitch")
    answer=answer=input("Açıl ... açıl.Lütfen boşluğu doldurunuz: ")
"""
    
"""
açıl .... açıl:kahve
heheheheheheheh ne oldu çıkamıyor musun:-)
açıl .... açıl:nane
heheheheheheheh ne oldu çıkamıyor musun:-)
açıl .... açıl:susam
kaç denemede bulduğumuzu da ekrana bassın
"""
"""
secret="susam"
deneme=0
answer=input("Açıl ... açıl.Lütfen boşluğu doldurunuz: ")
while answer!=secret:
    print("Kapı açılmıyo bitch")
    answer=answer=input("Açıl ... açıl.Lütfen boşluğu doldurunuz: ")
    deneme+=1
print(f"{deneme} kez denediniz!!!")
"""

"""
#1 3 5 6 7 9 ...99
i=0
while i<100:
    if i%2!=0:
        print(i,end=" ")
    i+=1
"""
#1 3 5 6 7 9 ...99'li grubu 10'arlı şekilde yaz
"""
i=0
x=0
while i<100:
    if i%2!=0:
        if i==49:
            print("..",end=" ")
        else:
            print(i,end=" ")
            x+=1
    if x==10:
        print()
        x=0
i+=1
"""
#1 den 99a kadar olan tüm sayıları 10 şekilde yaz ve 49un yerine .. yaz
i=0
x=0
while i<100:
    if i %2 !=0:
        if i==49:
            print("..",end=" ")
        else:
            print(i,end=" ")
        
        x+=1
        if x==10:
            print()
            x=0
    i+=1
    

