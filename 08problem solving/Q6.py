num=map(int,input("Enter number"))
if num%5==0 and num%11==0:
    print(f"{num} this number divigible by both 5 and 11")
elif num%5==0:
    print(f"{num} this number divigible by 5")
elif num%11==0:
    print(f"{num} this number divigible by 11")
else:
    print("Divisible by neither")