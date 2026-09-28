# row=1
# n=int(input("Enter your number"))
# while row<=n:
#     column=1
#     while column<=row:
#         column+=1
#         print(row,end="")
#     print()
#     row+=1
# 1
# 22
# 333
# 4444
# 55555

row=1
n=int(input("Enter your number"))
while row<=n:
    column=0
    while column<=row-1:
        column+=1
        print(column,end="")
    print()
    row+=1