#EKOK Sorusu
ekok=1
s1=15
s2=20
liste=[2,3,5]
for i in liste:
    while True:
        if s1%i==0 and s2%i==0:
            ekok*=i
            s1=int(s1/i)
            s2=int(s2/i)
        elif s1%i==0:
            ekok*=i
            s1=int(s1/i)
        elif s2%i==0:
            ekok*=i
            s2=int(s2/i)
        else:
            break
ekok=ekok*s1*s2
print(ekok)
        
