vowel=0
consonant=0
digit=0
special_character=0
sentence=input("Enter your character").lower()
for i in sentence:
    if i=='a'  or i=='e' or i=='i' or i=='o' or i=='u':
        vowel+=1
    elif ('a' <= i <= 'z') and (i!='a' or i!='e' or i!='i' or i!='o' or i!='u'):
        consonant+=1
    elif '0'<=i<='9':
        digit+=1
    else:
        special_character+=1
print(f"vowel points -> {vowel*2}")
print(f"consonant point -> {consonant*1}")
print(f"digit points -> {digit*3}")
print(f"special charecter points -> {special_character*4}")