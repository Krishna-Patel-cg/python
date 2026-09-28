
for i in range(1,7):
    units=int(input("Enter your electricity bill unit -> "))
    if units<=100:
        total=units*5
        print(total)
    elif units<=200:
        unit7=100*5+(units-100)*7
        print(total)
    elif units<=400:
        total=(100*5) +(100*7)+(units-200)*10
        print(total)
    else:
        total=(100*5)+(100*7)+(200*10)+(units-400)*15
        print(total)
        if total<1000:
           print("Low")
        elif 1000>=total>=3000:
           print("Medium")
        else:
            print("High")
