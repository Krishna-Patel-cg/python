conpass=0
confail=0
congood=0
conexcellent=0
for i in range(10):
    mark=int(input("Enter your marks"))
    if mark<=35:
        confail+=1
        print("Fail")
    elif 35<mark<50: 
        conpass+=1
        print("pass")
    elif 50<mark<75:
        congood+=1
        print("Good")
    elif 75<mark<=100:
        conexcellent+=1
        print("Excellent")
    else:
        print("Go to back and inter your valid marks")
print("no of suject fail",confail)
print("no of subject pass",conpass)
print("no of subject good",congood)
print("no of subject excellent",conexcellent)

        
     