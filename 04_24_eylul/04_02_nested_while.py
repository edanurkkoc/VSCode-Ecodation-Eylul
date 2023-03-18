"""
i,j=0,0
while i<3:
    while j<3:
        print(f"{i}x{j}",end=" ")
        j +=1
    j=0
    i+=1
    print()#Eğer bu print olmazsa kodda yan yana çıktı elde ederiz.
"""

"""
. . . . . . . . . . 
. . . . . . . . . . 
. . . . . . . . . . 
. . . . . . . . . . 
. . . . . . . . . . 
. . . . . . . . . . 
. . . . . . . . . . 
. . . . . . . . . . 
. . . . . . . . . . 
. . . . . . . . . . 
. . . . . . . . . . 
"""
x,y=0,0
while x<=10:
    while y<=11:
        print(".",end=".")
        y+=1
    x+=1
    y=0
    print()
    




