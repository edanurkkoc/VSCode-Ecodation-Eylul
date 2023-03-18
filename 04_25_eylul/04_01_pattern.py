#pattern->şekil,sembol yazdırma
"""
i=0
while i<5:
    i+=1
    print(i)

i=5
while i>0:
    print(i)
    i-=1
"""

"""
*(1 kez dönmüş)
* *(2 kez dönmüş)
* * *(3 kez dönmüş)
* * * *(4 kez dönmüş)
* * * * *(5 kezdönmüş)
"""
"""
i,j=0,0
while i<5:
    while j<=i:
        print(" *",end=" ")
        j+=1
    print()
    j=0
    i+=1
"""

"""
* * * * * 
* * * *
* * *
* * 
*
"""
"""
i,j=0,5
while i<5:
    while j>0:
        print(" * ",end=" ")
        j-=1
    i+=1
    print()
    j=5-i
"""
"""
* * * *  
. * * *
. . * *
. . . *
"""
"""
i,j=0,0
while i<4:
    while j<4:
        if i<=j:
         print(" * ",end=" ")
        else:
            print(" . ",end=" ")
        j+=1
    print()
    j=0
    i+=1
"""
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
