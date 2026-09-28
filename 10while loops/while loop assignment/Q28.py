row=1
# column=0   //yaha nahi rahega
n=int(input("Enter your number"))
while row <=n:
    coloumn=1
    while coloumn<=row:
        print("*",end="")
        coloumn+=1
    print()
    row+=1