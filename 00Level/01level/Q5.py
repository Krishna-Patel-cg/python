age=int(input("Enter your age"))
if 0<=age<=12:
    print("Child")
elif age>=13 and age<=19:
    print("Teenager")
elif age>=20:
    print("Adult")
else:
    print("Invalid year")