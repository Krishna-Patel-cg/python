a,b,c=map(int,input("Enter three number").split()[:3])
if a>b and c<a:
    print(f"{a} is biggest number")
elif b>a and c<b:
    print(f"{b} is biggest number")
else:
    print(f"{c} is biggest number")