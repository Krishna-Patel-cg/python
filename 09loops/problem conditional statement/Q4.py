# lowercase=0
# uppercase=0
# number=0
# special_charecter=0
# password=input("Enter your pasword").split()[:9]
# for i in password:
#     if chr(65)<=i<=chr(90) and chr(97)<=i<=chr(122) and '0'<=i<='9':
#         lowercase+=1
#         uppercase+=1
#         number+=1
#         special_charecter+=1
#         if lowercase==2 and uppercase==2 and number==2 and  special_charecter==2:
#             print("Strong password")
#         elif lowercase==1 and uppercase==2 and number==4 and special_charecter==1:
#             print("Medium")
#         else:
#             lowercase==1 and uppercase==0 and number==7
#             print("low")
#         # print(lowercase)

lowercase = 0
uppercase = 0
number = 0
special_charecter = 0

password = input("Enter your password: ")

for i in password:
    if chr(65) <= i <= chr(90):
        uppercase += 1
    elif chr(97) <= i <= chr(122):
        lowercase += 1
    elif '0' <= i <= '9':
        number += 1
    else:
        special_charecter += 1
count = 0
if len(password) >= 8:
    count += 1
if lowercase >=1:
    count += 1
if uppercase >= 1:
    count += 1
if number >= 1:
    count += 1
if special_charecter >= 1:
    count += 1
if count == 5:
    print("Strong password")
elif count >= 3:
    print("Medium")
else:
    print("Weak")