lip_year=int(input("Enter years"))
if lip_year%4==0 and lip_year%100!=0:
    print(f"{lip_year} is leap year")
else:
    print(f"{lip_year} not leap year")