a,b,c=map(int,input("Enter three number").split()[:3])
if a==b and b==c and a==c:
    print("Equilateral")
elif a==b and b==c and a!=c:
    print("Scalene")
else:
    print("Isosceles")