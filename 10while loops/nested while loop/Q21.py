# n=1
# row=1
# while row<=10:
#     n+=1
#     print((n)*row,end=" ")
#     row+=1
row=1
while row<=10:
    column=1
    while column<10:
        column+=1
        print(row*column ,end="\t")
    print()
    row+=1