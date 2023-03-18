"""
1-ve     and
2-veya   or
3-değil  not
print(5==5 and 3<6)
"""


"""
T T:T
T F:F
F T:F
F F:F
print(5==5 or 3<6)
"""

"""
T T:T
T F:T
F T:T
F F:F
"""
"""
print(5!=5)
print(not 5==5)

result=5!=5
result= not 5==5
print(result)
"""
"""
kurs1->4,5,6 yaş
...
yaşınız 9 kurs1 e uygun değil
....
yaşınız:5
kurs1e uygun değil
"""

kurs1=4 and 5 and 6
yas=int(input("Kurs için yaş giriniz: "))
if yas<7 and yas>3:
    print("Kursa hoşgeldin:)")
else:
    print(f"{yas} kurs1 için uygun değildir!!!")
    