a,b=0,0
sayilar=[3,56,4,8,19,56,55,4,53]
for i in sayilar:
    if i%2==0:
        print("Çift sayıdır->",i)
        a+=1
    else:
        print("Tek sayıdır->",i)
        b+=1
print(f"Çift sayılar={a} adet ve Tek sayılar={b} adettir")

