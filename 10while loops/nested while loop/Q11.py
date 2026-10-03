# row=1
# n=5
# while n>=row:
#     column=0
#     while column<=5:
#         column+=1
#         # print(row*row,end="   ")
#         print(chr(64+row),end="   ")
#     print()
#     row+=1

# A   A   A   A   A   A   
# B   B   B   B   B   B   
# C   C   C   C   C   C   
# D   D   D   D   D   D   
# E   E   E   E   E   E 


row=0
n=5
while n>=row:
    column=0
    while column<=row:
        column+=1
        # print(row*row,end="   ")
        print(chr(64+column),end="   ")
    print()
    row+=1