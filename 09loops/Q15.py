num=int(input("Enter number"))
count=0
for i in range (1,num+1):
    if i>=1 and i%2==0:
        count+=1
print(count)