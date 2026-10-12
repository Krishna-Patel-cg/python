food_type=input("Enter Account Type")
match food_type:
    case "Vegetarian":
        check=int(input("Enter your choice"))
        match check:
            case 1:
                print("Paneer")
            case 2:
                print("Dal")
            case 3:
                print("Veg Biryani")

match food_type:
    case "Non-Vegetarian":
        check=int(input("Enter your choice"))
        match check:
            case 1:
                print("Chicken Biryani")
            case 2:
                print("Chicken Curry")
            case 3:
                print("Fish Fry")
    case _:
        print("Invalid type")