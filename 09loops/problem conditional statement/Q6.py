a=input("Enter first number")
b=input("Enter second number")
c=input("Enter third number")
d=input("Enter fourth number")
e=input("Enter five number")
for i in a:
    if int(i)%2==0:
        print(f"{a} is even number")
    elif int(i)%2!=0:
        print(f"{a} is odd number")
for i in b:
    if int(i)%2==0:
        print(f" {b} is even number")
    elif int(i)%2!=0:
        print("Equal number")
for i in c:
    if int(i)%2==0:
        print(f"{c} is even number")
    elif int(i)%2!=0:
        print(f"{c} is odd number")
for i in d:
    if int(i)%2==0:
        print(f"{d} is even number")
    elif int(i)%2!=0:
        print(f"{d} is odd number")
for i in e:
    if int(i)%2==0:
        print(f"{e} is even number")
    elif int(i)%2!=0:
        print(f"{e} is odd number")
if a==b or a==c or a==d or a==e:
    print("two number  are equal")
