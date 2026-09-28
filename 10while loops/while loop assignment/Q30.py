row=1
n=int(input("Enter your number"))
while row<=10:
    column=1
    while column<=1:
        column+=1
        print(n*row,end=" ")
        print((n-1)*row,end=" ")
        print((n-2)*row,end=" ")
        print((n-2)*row,end=" ")
        print((n-4)*row,end=" ")
        print((n-row)*row,end=" ")
    print()
    row+=1