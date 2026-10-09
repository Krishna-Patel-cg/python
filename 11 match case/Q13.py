day=input("Enter Day Name")
match day:
    case "Monday"|"Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case "Saturday" | "Sunday":
        print("Weekend")