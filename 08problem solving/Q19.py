num=int(input("Enter number"))
if num<0:
    print("this number belong Negative")
elif num>=0 and num<=10:
    print(f"this number belong to {num}")
elif num>=11 and num<=50:
    print(f"this number belong 11-50 {num}")
elif num>=51 and num<=100:
    print(f"this number belong to 51-100 {num}")
else:
    print(f"this number above to 100: {num}")