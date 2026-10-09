category=int(input("Enter Category"))
match category:
    case 1:
        print("Account Balance")
    case 2:
            print("Mini Statement")
    case 3:
            print("Fund Transfer")
    case 4:
            print("Bill Payment")
    case 5:
            print("Customer Support")
    case _:
            print("Invalid")