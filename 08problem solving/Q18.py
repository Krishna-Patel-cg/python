temp=int(input("Enter temperature"))
if temp<0:
    print("Freezing")
elif temp>=0 and temp<=15:
    print("Very Cold")
elif temp>=16 and temp<=25:
    print("Very Cold")
elif temp>=26 and temp<=35:
    print("Very Cold")
else:
    print("Hot")