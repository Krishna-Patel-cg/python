# for i in range(0,3):
#     for j in range(0,1):
#         print("1 2 3" ,end="")
#     print()

for i in range(1,4):
    for j in range(1,4):
        print(j, end=" ")
    print()

    for i in range(1,6):
        for j in range(5,i-1,-1):
            print("*",end="")
        print()