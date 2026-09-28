# n=int(input("enter number"))
# for i in range(0,n):
#     for j in range(0,1):
#         print("1",end="")
#         for i in range(1,2):
#            for j in range(0,1):
#                print("2",end="")
#         for i in range(0,1):
#             for j in range(0,1):
#                 print("x",end="")
#         for i in range(0,1):
#             for j in range(0,1):
#                 print("4",end="")
#         for i in range(0,1):
#             for j in range(0,1):
#                 print("5",end="")
#         for i in range(0,1):
#             for j in range(0,1):
#                 print("x",end="")
#         for i in range(0,1):
#             for j in range(0,1):
#                 print("7",end="")
#         for i in range(0,1):
#             for j in range(0,1):
#                 print("8",end="")
#         for i in range(0,1):
#             for j in range(0,1):
#                 print("x",end="")
#     print()

n = int(input("Enter number -> "))
for i in range(1, n + 1):  
    for j in range(1, i + 1): 
        if j % 3 == 0 and j % 5 == 0:
            print("Z", end=" ")
        elif j % 3 == 0: 
            print("X", end=" ")
        elif j % 5 == 0: 
            print("Y", end=" ")
        else: 
            print(j, end=" ")
    print()