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

for i in range (0,8):
    for j in range(8-i-1):
       print(" ",end="")
    for k in range(2*i+1):
       print("*",end="")
    print()