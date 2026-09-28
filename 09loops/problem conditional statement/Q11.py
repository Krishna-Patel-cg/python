charcount=0
digitcount=0
underscore=0
invalidcharacter=0
username=input("Enter your name")
for i in username:
    charcount+=1
    if '0'<=i<='9':
        digitcount+=1
    elif i == "_":
         underscore+=1
    else:
        invalidcharacter+=1 

print(len(username))
print(digitcount)
print(charcount)
print(underscore)
print(invalidcharacter)