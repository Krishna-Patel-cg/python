age=int(input("Enterb your age"))
if age<0:
    print("Invalid age")
elif age<18:
    print("Cannot vote")
else:
    print("Can vote")