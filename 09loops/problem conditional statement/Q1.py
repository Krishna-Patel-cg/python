uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0
password=input("Enter your password")
for i in password:
    if 'A' <= i <= 'Z':
        upperase+=1 
    elif 'a' <= i <= 'z':
        lowercase+=1
    elif '0' <= i <= '9':
        digits+=1
    elif i==0:
        spaces+=1
    else:
        special+=1
print(f"NUmber of Upper case {uppercase}")
print(f"NUmber of lower case {lowercase}")
print(f"NUmber of digit case {digits}")
print(f"NUmber of spaces case {spaces}")
print(f"NUmber of Special case {special}")