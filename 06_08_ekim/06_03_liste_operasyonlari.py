#liste=[1,2,3,4,5]
#liste[2]=liste[3]#liste=[1,2,4,4,5]
#liste[3]=liste[2]#liste=[1,2,4,4,5]
#print(liste)
"""
liste=[1,2,3,4,5]
temp=liste[2]
liste[2]=liste[3]#liste[2],liste[3]=liste[3],liste[2]
liste[3]=temp
print(liste)
"""
"""
#slice çalışmalarımız
kurum="ecodation"
result=kurum
result=kurum[2]
result=kurum[3]
result=kurum[-3]
result=kurum[:]#outout:ecodation,bize tümünü slice etti
result=kurum[0:3]#output:eco
result=kurum[-1]#n
result=kurum[1:4]#output:cod
result=kurum[-1:-1:-1]#output:?
result=kurum[-1:0:-1]#output:noitadoc
result=kurum[:3]#output:eco
result=kurum[::-1]#output:noitadoce
liste=[1,2,3,4,5]
result=kurum[::-1]#output:[5,4,3,2,1]
result=kurum[-3:-1]#output:[3,4]
print(result)
"""

site=input("Lütfen bir site ismi giriniz: ")
if site[-3:]!="com" or site[:3]!="www":
    print("Yanlış adres")
else:
    print(f"internet adresiniz {site}")