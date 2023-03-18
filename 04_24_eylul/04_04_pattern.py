#Pattern
"""
10 tane yan yana $ işareti  yazdır ekrana
"""
"""
i=0
while i<10:
    i+=1
    print("$",end=" ")
"""
"""
$ # $ # $ # $ # $ # 
"""

"""i=0
while i<5:
    i+=1
    print("$" " " "#",end=" ")
"""
"""
x=0
while x<10:
    if x%2==0:
        print("#",end=" ")
    else:
        print("$",end=" ")
    x+=1
"""    
"""
*
*
*
*
*
*
*
*
*
*
"""
"""
x=0
while x<10:
    x+=1
    print("*")
"""
"""
*
$
*
$
*
$
*
$
*
$
"""
"""
x=0
while x<10:
    if x%2==0:
        print("*")
    else:
        print("$")
    x+=1
"""
"""
. . . . . . . . . .
* * * * * * * * * *
. . . . . . . . . .
* * * * * * * * * *
. . . . . . . . . .
* * * * * * * * * *
. . . . . . . . . .
* * * * * * * * * *
. . . . . . . . . .
* * * * * * * * * *
"""    
x,y=0,0
while x<10 :
    while y<10:
        if x%2==0:
            print(" * ",end=" ")
        else :
            print(" . ",end=" ")
        y+=1
    x+=1
    y=0
    print()



    


