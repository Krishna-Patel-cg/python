# password=input("Enter your number")
uppercase=0
lowercase=0
digit=0
special_character=0
password=input("Enter your password")
for i in password:
    if 'A'>=i>='Z':
        uppercase+=1
    elif 'a'>=i>='z':
        lowercase+=1
    elif '0'>=i>='9':
        digit+=1
    else:
        special_character+=1

print(uppercase)
print(lowercase)
print(digit)
print(special_character)