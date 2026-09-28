# number=int(input("Enter a valid number"))
# for i in range (0,number):
#     if i%2==0:
#         print(f"{i} is even")
# n=int(input("enter number"))
# for i in range (1,11):
#     print(f"{n} x {i}  =  {n*i} ")
# name=input("Enter charecter").strip().lower()
# length=len(name)
# sum=""
# for charecter in (len(name)-1,-1,-1):
#     sum=sum+name[charecter]
# print(sum)


# name=input("Enter charecter").strip().lower()
# length=len(name)
# sum=""
# for charecter in range (length-1,-1,-1):
#     sum=sum+name[charecter]
# print(sum)

# name=input("Enter charecter :").strip().lower()
# length=len(name)
# sum=""
# for charecter in range (length-1,-1,-1):
#     sum=sum+name[charecter]
#     print(sum)

# name=input("Enter charecter").strip().lower()
# length=len(name)
# sum=""
# for charecter in range (length-1,-1,-1):
#     sum=sum+name[charecter]
# if name==sum :
#     print(f"{name} charecter is palidrome")
# else:
#     print(f"{name} charecter  not palidrome")


# name="Python"
# for character in "Krishna":
#     print(character)

# for i in range(3):
#     for j in range(3):
#         print(i,j)

# for i in range(srt(krishna)):
#     for j in range(str(2)):
#         print(i,j)


# print("Hello", end=" ")
# print("World")

# age = 15

# if age >= 18:
#     print("You are an adult.")

# age = 20

# if age >= 18:
#     print("Adult," )
#     print("Age requirement satisfied", end="")
#     print("You can continue")

# for row in range(1, 5):
#     for column in range(1,5):
#         print("*", end="")
#     print()

# ****
# ****
# ****
# ****

# for row in range(0,5):
#     for column in range(0,row+1):
#         print("*", end="")
#     print()

# *
# **
# ***
# ****
# *****
# for row in range(5,1,-1):
#     for column in range(row-1):
#         print("*", end="" )
#     print()

# ****
# ***
# **
# *

# for k in range(1):
#     print("*")    

# for i in range (1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#       print("*",end="")
#     print("")

#    *
#    **
#   ***
#  ****
# *****
# for i in range (6,1,-1):
#     for j in range(0,6-i):
#         print(" ",end="")
#     for k in range(1,i):
#       print("*",end="")
#     print("")
# *****
#  ****
#   ***
#    **
#     *
# for i in range(0,5):
#     for j in range(6-i):
#         print(" ",end="")
#     for k in range (2*i+1):
#         print("*",end="")
#     print()
#       *
#      ***
#     *****
#    *******
#   *********
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# *
# **
# ***
# ****
# *****

# for i in range(0,10):
#     for j in range (10-i,0,-1):
#        print("0",end="")
#     for k in range (1,2*i-2):
#         print("*",end="")
#     # for l in rnge()
#     print()

# for i in range (0,8):
#    for j in range(8-i-1):
#       print("8",end="")
#    for k in range(2*i+1):
#       print("*",end="")
#    for m in range(0,5):
#       for l in range(5-i):
#          print("9",end="")
#    print()

# total=0
# flag=True
# for i in range(5):
#    marks=int(input("enter your marks"))
#    total+=marks
#    if marks<35:
#       flag=False
# if flag:
#    percentage=total/5
#    if percentage>=90:
#       grade="A+"
#    elif percentage>=80:
#       grade="A"
#    elif percentage>=70:
#       grade="B+"
#    elif percentage>=60:
#       grade="B"
#    elif percentage>=50:
#      grade="C"
#    elif percentage>35:
#      grade="D"
#    else:
#       grade="F"
# if flag==True:
#    print(total,grade,percentage)
#    print("You are pass")
# if flag==False:
#    print(total,grade,percentage)
#    print("You are fail")
# n=int(input(("enter your number")))
# for i in range(1,n+1):
#    for j in range(1,n+1):
#       if j==1 or j==n or i==n or (n/2==j and n/2==i):
#          print("*",end=" ") 
#       else:
#          print(" ",end=" ")
#    print()

n=int(input("Enter number"))
nu=int(input("Enter number"))
for i in range(1,2):
   print(n**nu ,end=" ")
print()