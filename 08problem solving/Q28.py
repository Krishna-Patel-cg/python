# person_1,age_1=map(int,input("Enter your name and age").split())
# person_2,age_2=map(int,input("Enter your name and age"))
# person_3,age_3=map(int,input("Enter your name and age"))
# if age_1>age_2 and age_1>age_3:
#     print(f" {person_1} is the youngest")
# elif age_2>age_1 and age_2>age_3:
#     print(f"{persson_2} is the youngest")
# else:
#     print(f"{person_3} is the youngest")

person_1=input("Enter your name")
age_1=int(input("Enter age"))
person_2=input("Enter your name")
age_2=int(input("enter age"))
person_3=input("Enter your name")
age_3=int(input("enter age"))
if age_1<age_2 and age_1<age_3:
    print(f" {person_1} is the youngest")
elif age_2<age_1 and age_2<age_3:
    print(f" {persson_2} is the youngest")
else:
    print(f"{person_3} is the youngest")