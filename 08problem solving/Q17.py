print("1.Addition") 
print("2.Subtraction")
print("3.division") 
print("4.Multiplication") 
opration=int(input("Enter a number of operation tht you want to work"))
if opration >4:
    print("Invalid")
num=input("two digit number")
a,b = map(int,input("Enter number").split()[:2])
if opration==1:
    print(a+b)
elif opration==2:
    print(a-b)
elif opration==3:
    print(a*b)
elif opration==4:
    print(a/b)
else:
    print("Thanks")