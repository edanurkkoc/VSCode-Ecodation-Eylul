"""
WİLE-ELSE 
-döngüsü break satırı ÇALIŞMADAN biterse,else içine girer
-döngüsü break satırı ÇALIŞARAK biterse,else içine girer
i=1
while i<=10:
        print(i)
        i+=1
        if i==55:
            break
else:
            print("Ben şu an while-else içindeyim")
"""
#FOR DÖNGÜSÜ
#döngüsü break satırı ÇALIŞMADAN biterse,else içine girer
#döngüsü break satırı ÇALIŞARAK biterse,else içine girer
for i in range(1,11):
    if i==4:
        #break
        pass
    print(i)
else:
    print("Şu anda for elsedeyim")
print("for döngüsü bitti")

