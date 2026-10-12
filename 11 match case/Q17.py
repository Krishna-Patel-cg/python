account_type=input("Enter Account Type")
match account_type:
    case "Saving":
        check=int(input("Enter your choice"))
        match check:
            case 1:
                print("Check Balance")
            case 2:
                print("Deposit")
            case 3:
                print("Withdraw")

match account_type:
    case "Current":
        check=int(input("Enter your choice"))
        match check:
            case 1:
                print("Check Balance")
            case 2:
                print("Deposit")
            case 3:
                print("Withdraw")
    case _:
        print("Invalid type")