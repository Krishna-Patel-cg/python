a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a>b and a>c:
    print(f"{a} is maximum number")
elif b>a and b>c:
    print(f"{b} is maximum number")
elif c>a and c>b:
    print(f"{c} is maximum number")
else:
    print(f"{a} , {b} , {c} are equal")