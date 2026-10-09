payment_method=input("Enter payment method")
match payment_method:
    case "upi":
        print("UPI Payment Selected")
    case "card":
            print("card Payment Selected")
    case "cash":
            print("Cash Payment Selected")
    case "wallet":
            print("UPI Payment Selected")
    case _:
            print("Invalid Selected")