count=0
even_count=0
num=int(input("Enter your number"))
while num>=count:
    # if num%2==0:
    print(count,end=" ")
    even_count+=count
    count+=2
print()
print("total sum even number",even_count)