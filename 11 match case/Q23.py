# account_type=input("Your bank account type choice \n 1. Saving \n  2.  Current \n ")
# withdrawal =int(input("Enter money"))
# while withdrawal !=0:
#     match account_type:
#         case "1":
#             print("Saving Account  \n Widthdrawal Request Accept")
#         case _:
#             print("Invalid choice")

account_type = int(input("Enter account type: "))
match account_type:
    case 1:
        print("Savings Account")
        amount = float(input("Enter amount: "))
        if amount > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")
            
    case 2:
        print("Current Account")
        amount = float(input("Enter amount: "))
        if amount > 0:
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")
            
    case _:
        print("Invalid Account Type")