level=input("Enter Your Level")
match level:
    case "Bronze" | "Silver":
        print("Basic Membership")
    case "Gold" | "Platinum":
            print("Premium Membership")