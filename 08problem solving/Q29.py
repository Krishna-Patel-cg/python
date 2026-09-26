a,b,c=map(int,input("Enter three number").split()[:3])
if a==c==b:
    print("All number same")
elif a==b!=c or a!=b==c or c==a!=b:
    print("Two number are same")
elif a<c<b:
    print(f"{c} is second largest number")
elif b<c<a:
    print(f"{a} is second largest number")
elif a<c<b:
    print(f"{b} is second largest number")
elif c<a<b:
    print(f"{b} is second largest number")
elif c<b<a:
    print(f"{b} is second largest number")
elif b<a<c:
    print(f"{b} is second largest number")