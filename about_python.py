# print("krishna")
# print(10+2)
# print(10/2)
# a = 12
# b = 15
# print(a == b)
# print(2**5)

# print(-7 % 3)

# print(1 == 5.0)

# # for i in range(3):
# #     if i == 1: continue
# #     print(i, end=" ")

# for i in range(3):
#     pass
# print(i)

# print(all([1, 2, 0]))
# print(any([0, 0, 1]))

# a = 10
# b = a
# a = 20
# print(b)
# # num=input("Enter your name")
# # print(num)


# print(int("20.776"))
# print("a" if 5 > 3 else "b")

# string="krishna"
# print(*string,sep="-")
# print("-".join(string))

# for row in range(3):
#     for column in range(4):
#         print("*", end=" ")
#     print()
# salary = 1000
# pay_raise = 100
# print(new_salary)
# new_salary = salary + pay_raise

# number = int(input("Enter a number: "))

# while number != 0:
#     print("You entered:", number)
#     number = int(input("Enter a number: "))

# print("Loop ended")


# num=int(input("Enter a number "))
# count=0
# while count !=3:
#     count+=1
#     print(("You enter  ",num))
#     print(count)
#     num=int(input("Enter a number "))
# print("Loop ended")

number = int(input("Enter a number: "))
total = 0
while number != 0:
    total = total + number
    number = int(input("Enter a number: "))

print("Sum:", total)


number = int(input("Enter a number: "))
total=0
while   number>0:
    digit=number%10
    total=total+digit
    number=number//10
print(total)



#  reverse number

number = int(input("Enter a number: "))
reverse=0
while number>0:                
    digit=number%10
    reverse=reverse*10+digit
    number=number//10