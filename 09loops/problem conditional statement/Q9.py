vowel=0
consonant=0
digit=0
special_character=0
string=input("Enter your number").lower()
for i in range(0,1):
    if i=='a' or i=='o' or i=='e'  or i=='i'  or i=='u':
        vowel+=1
        print("Vowel")
    elif 0<=i<=9:
        digit+=1
        if int(i)%2==0:
            print("even")
        else:
            print("odd")
        print(digit)
    elif ('a' <= i <= 'z') and (i!='a' or i!='e' or i!='i' or i!='o' or i!='u'):
        consonant+=1
        print("Consonants")
    else:
        special_character+=1
        print("Special")
print(vowel)
print(consonant)
print(digit)
print(special_character)