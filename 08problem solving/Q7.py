num=int(input("Enter number"))
if num%3==0 and num%7==0:
    print(f"{num} this number divigible by both 3 and 7")
elif num%3==0:
    print(f"{num} this number divigible by 3")
elif num%7==0:
    print(f"{num} this number divigible by 7")
else:
    print("Divisible by neither")