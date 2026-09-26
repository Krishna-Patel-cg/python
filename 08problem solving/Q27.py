hours=int(input("Enter hours"))
if 0<=hours<=23:
    minutes=int(input("Enter minutes"))
    if 0<=minutes<=59:
        second=int(input("Enter second"))
        if 0<=second<=59:
            print("Valid time")
else:
    print("please enter valid number")