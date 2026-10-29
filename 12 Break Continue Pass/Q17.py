str=input("enter  string")
count=0
for i in str:
    if i=="a" or i=="e" or i=="o" or i=="i" or i=="u":
        continue
    count+=1
    print(i)
print(count)