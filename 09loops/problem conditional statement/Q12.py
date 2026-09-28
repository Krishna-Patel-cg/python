vowel=0
consonant=0
character=input("Enter your character").lower()
for i in character:
    if i==chr(97) or i==chr(101) or i==chr(105) or i==chr(111) or i==chr(117):
        vowel+=1
    elif chr(97)>=i>=chr(121) or (i!=chr(97) or i!=chr(101) or i!=chr(105) or i!=chr(111) or i!=chr(117)):
        consonant+=1
print(vowel)
print(consonant)
if vowel>consonant:
    print("Vowel Win")
elif consonant>vowel:
    print("Consonants Win")
else:
    print("Draw")