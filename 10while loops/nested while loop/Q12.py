row=1
n=5
while n>=row:
    column=0
    while column<=row-1:
        column+=1
        # print(row*row,end="   ")
        print(chr(64+row),end="   ")
    print()
    row+=1