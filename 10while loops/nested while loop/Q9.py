# row=1
# n=3
# while row<=3:
#     column=1
#     while column<=5:
#         column+=1
#     print(row*column)
#     row+=1

# row=1
# n=5
# column=1
# while row<=10:
#     print(n*row)
#     column+=1
#     print((n-1)*row)
#     print((n-2)*row)
#     row+=1
row=1
n=3
while row<=5:
    column=1
    while column<=5:
        column+=1
    print((n-2)*row,end=" ")
    print((n-1)*row,end=" ")
    print(n*row)
    row+=1