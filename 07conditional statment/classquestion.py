# num=12
# if num%2==0 :
#     print("Even number")

#     if num%2==1 :
#         print("Odd number")

# name=input("enter your name")

# if name=="krishna":
#     age=int(input("Enter your name: "))
#     if age>=18:
#         city=input("eneter yuor city name: ")
#         if city=="varanasi":
#             mobile=input("enter mobile number: ")
#             if mobile=="7398924004":
#                 print("student profile detail right")
# print("18"==18)
# print(int("18")>=18)
# name=input("Enter you name")
# if name  =="krishna":
#     print("your document all match")
# else :
#     print("Unsuccesful varification")
# indian=input("are you indian? Yes or No")
# marks =int(input("Enter your marks"))
# if marks >= 90:
#     print("Excellent")
# elif marks >= 60:
#     print("Good")
# elif marks >= 40:
#     print("Pass")
# else:
#     print("Fail")
# marks=int(input("Enter your marks"))
# if marks>90 and marks<=100:
#     print("A")
# elif marks>60 and marks<=89:
#     print("B")
# else:
#     print("fail")

print("1.Addition") 
print("2.Subtraction")
print("4.division") 
print("3.Multiplication") 
opration=int(input("Enter a number of operation tht you want to work"))
if opration >4:
    print("Invalid")

# num=input("two digit number")
a,b = map(int,input("Enter two number").split()[:2])
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
     