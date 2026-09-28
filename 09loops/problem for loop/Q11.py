# for i in range(0,5):
#     # for j in range(65,71):
#     for j in range(65,66+i):
#         print(chr(j),end="")
#     print()

num=int(input("Enter your number"))
for i in range(1,num):
    for j in range(65,65+i):
        print(chr(j),end=" ")
    print()
