a,b,c=map(int,input("Enter three number").split()[:3])
if (a+b)>c and (a+c)>b and(b+c)>a:
    print("Valid triangle")
elif (a+b)<c or (a+c)<b or (b+c)<a:
    print("Invalid triangle")