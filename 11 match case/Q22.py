choice=int(input("Choose your choice \n 1. Km to m \n 2. m to Km \n 3. Kilograms to Gram \n 4. Gram to Kilograms  \n fill your choice "))
value=int(input("Enter your value"))
match choice:
    case 1:
        print(f"{value*1000}meters" )
    case 2:
        print(f"{value/1000} KM")
    case 3:
        print(f"{value*1000} grams")
    case 4:
        print(f"{value/1000} Kg")