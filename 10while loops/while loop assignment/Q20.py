table=1
add=0
num=int(input("Enter your number"))
while table<=10:
    print(num*table,end=" ")

    add+=num*table
    table+=1
print()
print(add)