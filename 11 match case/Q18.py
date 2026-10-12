category_type=input("Enter Account Type")
match category_type:
    case "Electronics":
        check=int(input("Enter your choice"))
        match check:
            case 1:
                print("Mobile")
            case 2:
                print("Laptop")
            case 3:
                print("Headphones")

match category_type:
    case "Clothing":
        check=int(input("Enter your choice"))
        match check:
            case 1:
                print("Shirt")
            case 2:
                print("Jeans")
            case 3:
                print("Shoes")
    case _:
        print("Invalid type")