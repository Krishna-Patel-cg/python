choice=int(input("Choice Your option (1.  °C to F \n 2.  F to °C)"))
convert=float(input("Enter Temp.."))
match choice:
    case 1:
        print(f"{convert*1.8} F")
    case 2:
        print(f"{(convert-32)/1.8}")