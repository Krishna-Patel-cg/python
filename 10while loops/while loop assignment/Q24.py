
string=input("Enter your character")
count1=0
number_a=0
while count1<len(string):
    print(string[count1],end=" ")
    if string[count1]=='a':
        number_a+=1
    count1+=1
print(number_a)