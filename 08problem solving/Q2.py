num=int(input("Enter any number"))
if num>0 and num%2==0:
    print(f"Positive Even number:{num}")
elif num>0 and num%2!=0:
    print(f"Positive Odd number:{num}")
elif num<0 and num%2==0:
    print(f"Negative Even number:{num}")
elif num<0 and num%2!=0:
    print(f"Negative Odd number:{num}")
else:
    print("Zero")