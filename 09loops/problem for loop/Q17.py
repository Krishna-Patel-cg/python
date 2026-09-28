# for i in range(1,10):
#     print(i,end=" ")
#     if i%3==0:
#       print()


# for i in range(1,8,3):
#     for j in range(i,i+3):
#         print(j,end=" ")
#     print()

num=int(input("Enter your number"))
a=1
for i in range(1,num):
    for j in range(i,i+3):
        print(j,end=" ")
        a+=1
    print()

